---
title: "How to Measure Performance of Your Code"
slug: "measure-your-code"
author: "subhrajit"
date: 2025-10-22T11:30:00+05:30
lastmod: 2025-10-22T11:30:00+05:30
description: "How to measure and profile your code using various tools and techniques."
keywords: ["Code Measurement", "Profiling", "Execution Time", "clock_gettime", "rdtsc", "getrusage", "Linux perf", "perf_event_open"]
draft: true
---

Measuring code performance accurately is crucial, especially when optimizing the existing algorithms or designing new ones. In this post, I’ll share my learnings of measuring code performance using various tools and techniques.

For measuring execution time, we can use the following techniques:

1. Wall Clock Time (`clock_gettime`)
2. Linux resource usage metrics (`getrusage`)

To measure raw Time Stamp Counter (or, ticks), on x86 architectures we can use:

1. `RDTSC` (Read Time-Stamp Counter)

Finally, to pinpoint performance bottlenecks, we can use the Linux `perf` tool; However, there are two ways to use it:

1. `perf` Command line tool
2. `perf_event_open` syscall for custom profiling code segments.

We will explore each of these methods in detail, with the help of an example C code snippet that we will measure using these techniques.
The naive function snippet we will use for measurement is as follows:

```c
int sum_of_two_arrays(int *array1, int *array2, int size)
{
    int total_sum = 0;
    int sum1 = 0, sum2 = 0;
    for (int i = 0; i < size; i++)
    {
        sum1 += array1[i];
    }
    for (int i = 0; i < size; i++)
    {
        sum2 += array2[i];
    }

    total_sum = sum1 + sum2;
    return total_sum;
}
```

## Wall Clock Time (clock_gettime)

The most popular way to measure code performance is by using wall clock time. The [`clock_gettime`](https://man7.org/linux/man-pages/man3/clock_gettime.3.html) function in Linux provides wall-clock time measurements with nanosecond precision. It can be used to measure the elapsed time for a specific code segment. While there are multiple clock types available, `CLOCK_MONOTONIC` is generally preferred for measuring elapsed time as it is not affected by system time changes. To use `clock_gettime`, we have to include the `<time.h>` header file.

### Usage

```c
// Include necessary headers and define variables
struct timespec start, end;
clock_gettime(CLOCK_MONOTONIC, &start);

// Code segment to measure
sum_of_two_arrays(array1, array2, size);

clock_gettime(CLOCK_MONOTONIC, &end);
long seconds = end.tv_sec - start.tv_sec;
long nanoseconds = end.tv_nsec - start.tv_nsec;
double elapsed = seconds + nanoseconds*1e-9;
printf("Elapsed time: %.9f seconds\n", elapsed);

```

### Output

```
Elapsed time: XXX
```

## getrusage
In linux systems, [`getrusage`](https://www.man7.org/linux/man-pages/man2/getrusage.2.html) is a system call that provides resource usage statistics for the calling process. It is used to measure the resources used by the process, like CPU time, memory usage, etc. We used this system call to measure the CPU time used by our code. POSIX.1 specifies `getrusage()`, but specifies only the fields `ru_utime` and `ru_stime`. And, for our benchmarking purposes, we can use `ru_utime` and `ru_stime` to measure the user CPU time and system CPU time, respectively.
The `getrusage` system call provides information about resource usage for a process, including user and system CPU time. The user CPU time represents the amount of CPU time spent in user mode, while the system CPU time represents the time spent in kernel mode. By measuring the user CPU time before and after executing a code segment, we can determine the CPU time consumed by that segment. To use `getrusage`, we need to include the `<sys/resource.h>` header file.

```c
// Function to measure CPU time in microseconds as a long double
static inline long double cputime()
{
    struct rusage rus;
    getrusage(RUSAGE_SELF, &rus);
    return rus.ru_utime.tv_sec * 1000000.0L + rus.ru_utime.tv_usec;
}
```

### Usage

```c
    // Include necessary headers and define variables
    long double start_time, end_time, cpu_time_used;
    start_time = cputime();

    // Code segment to measure
    sum_of_two_arrays(array1, array2, size);

    end_time = cputime();
    cpu_time_used = end_time - start_time;

    printf("CPU time used: %.3Lf microseconds\n", cpu_time_used);
```

## RDTSC

On the x86 architecture, the `RDTSC` (Read Time-Stamp Counter) instruction is a low-level way to measure the number of CPU ticks that have elapsed since the last reset. It provides a raw metric of code execution time, making it suitable for performance profiling. As `RDTSC` instruction measure the ticks that increments at a constant rate, regardless of CPU frequency scaling (e.g., Turbo Boost, power-saving states), the number of ticks per unit of real time will remain constant, even if the core's clock speed changes.
However, it is well-known that `RDTSC` does not provide accurate measurements in cases of code cross-contamination due to out-of-order execution. A white paper by Intel that explains how to measure ticks accurately using a combination of `CPUID`, `RDTSC`, and `RDTSCP` instructions. You can find the white paper here: [How to Benchmark Code Execution Times on Intel® IA-32 and IA-64 Instruction Set Architectures](https://cis.temple.edu/~qzeng/cis3207-spring18/files/ia-32-ia-64-benchmark-code-execution-paper.pdf). `RDTSCP` mitigates some of the out-of-order execution issues by serializing the instruction stream before reading the time-stamp counter.
The reason of using `CPUID` instruction (which generates an interrupt) before and after `RDTSC`/`RDTSCP` is to serialize the instruction stream, ensuring that all previous instructions have completed before reading the time-stamp counter. This helps to get a more accurate measurement of the code segment.

```c
static inline unsigned long long measure_rdtsc_start()
{
    unsigned cycles_low, cycles_high;
    unsigned long long ticks;
    asm volatile("CPUID\n\t"
                 "RDTSC\n\t"
                 "mov %%edx, %0\n\t"
                 "mov %%eax, %1\n\t" : "=r"(cycles_high), "=r"(cycles_low)::"%rax", "%rbx", "%rcx", "%rdx");
    ticks = (((unsigned long long)cycles_high << 32) | cycles_low);
    return ticks;
}
```

```c
// Inline function for measuring rdtscp ticks
static inline unsigned long long measure_rdtscp_end()
{
    unsigned cycles_low, cycles_high;
    unsigned long long ticks;
    asm volatile("RDTSCP\n\t"
                 "mov %%edx, %0\n\t"
                 "mov %%eax, %1\n\t"
                 "CPUID\n\t" : "=r"(cycles_high), "=r"(cycles_low)::"%rax",
                               "%rbx", "%rcx", "%rdx");
    ticks = (((unsigned long long)cycles_high << 32) | cycles_low);
    return ticks;
}
```

### Usage

```c
    // Include necessary headers and define variables
    unsigned long long start_ticks, end_ticks, ticks_taken;
    start_ticks = measure_rdtsc_start();
    sum = 0;
    for (int i = 0; i < 10000; i++)
    {
        sum += sum_of_two_arrays(array1, array2, N);
    }
    end_ticks = measure_rdtscp_end();

    ticks_taken = end_ticks - start_ticks;

    printf("Ticks taken: %llu\n", ticks_taken);
```

## Accuracy Considerations

The actual elapsed time will vary based on system load and other factors like CPU frequency scaling, context switching, etc. To get more accurate measurements, consider measuring the code segment multiple times --- create CDF plots to visualize the distribution of execution times or use statistical measures like 95% CI (Confidence Interval) mean to report the results. For execution time measurements, it's also important to minimize the impact of other processes running on the system. Running the measurements on a dedicated machine or using CPU affinity to bind the process to a specific core can help reduce variability.

I personally prefer averaging strategy of GMPBench to report the mean execution time of a given function. What it does is, it starts with a single iteration of the function and doubles the number of iterations until the total elapsed time exceeds a predefined threshold (e.g., 250 ms). Once the threshold is reached, it calculates the average time per iteration by dividing the total elapsed time by the number of iterations. This approach helps to ensure that the measurements are less affected by transient system load variations. Further, based on this computed mean time, it calculates throughput (operations per second) and reports that as the final performance metric.

Originally, GMPBench was designed to benchmark arbitrary-precision arithmetic operations in the GMP library, but the underlying methodology can be applied to measure the performance of any function or code segment.

Below you can find three different adapted macros of GMPBench style averaging strategy to measure execution time using `clock_gettime`, `RDTSC`, and `getrusage` respectively.

Whenever I report timing numbers, I prefer to run the GMPBench style averaging strategy for 20-30 times and report the 95% CI mean of the execution time or throughput numbers.

## Linux perf

The 'perf' tool in Linux is a powerful performance analysis tool that can measure various aspects of code performance, including CPU cycles, cache misses, and more. It provides a wealth of information but can be complex to use effectively.

In conclusion, accurately measuring code performance requires a combination of tools and techniques. By understanding the strengths and weaknesses of each method, you can gain valuable insights into your code's performance and identify areas for optimization.
