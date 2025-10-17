---
title: "Subhrajit Das"
layout: "raw-html"
type: "people"
---
<!DOCTYPE html>
<html lang="en-us" class="m-auto "><head>
	<meta name="generator" content="Hugo 0.147.3"><script src="/fuss/people/subhrajit/livereload.js?mindelay=10&amp;v=2&amp;port=1313&amp;path=fuss/people/subhrajit/livereload" data-no-instant defer></script>
  <link rel="icon" href="/fuss/people/subhrajit/favicon.ico" type="image/x-icon" />
  
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    integrity="sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer"
  />
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/academicons@1.9.1/css/academicons.min.css"
  />
  <link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;400;500;600;700&display=swap"
  />

  
  
  <link href="/fuss/people/subhrajit/main.css" rel="stylesheet" />
  

  <style>
     
    body, h1, h2, h3, h4, h5, h6, p, span, div, a, li, td, th, 
    input, textarea, button, label, select {
      font-family: 'Comfortaa', cursive !important;
    }
    
     
    i.fas, i.far, i.fab, i.fal, i.fad, i.fa,
    i[class*="fa-"],
    i.ai, i[class*="ai-"],
    .fas::before, .far::before, .fab::before, .fal::before, .fad::before, .fa::before,
    [class*="fa-"]::before,
    .ai::before, [class*="ai-"]::before {
      font-family: "Font Awesome 5 Free", "Font Awesome 5 Brands", "Font Awesome 5 Pro", "Academicons" !important;
      font-weight: inherit !important;
    }
    
     
    .fas, .fas::before {
      font-weight: 900 !important;
    }
    .far, .far::before {
      font-weight: 400 !important;
    }
    .fab, .fab::before {
      font-family: "Font Awesome 5 Brands" !important;
      font-weight: 400 !important;
    }
    
     
    html {
      touch-action: manipulation;
      scroll-behavior: smooth;
    }

    .panel {
      max-height: 0;
      transition: 0.3s ease-out;
    }

    .profile-photo-container {
      img {
        max-width: 100%;
      }
    }
    
     
    .profile-section {
      padding: 1rem;
    }
    
    @media (max-width: 768px) {
      .profile-section {
        padding: 0.5rem;
        text-align: center;
      }
      
      .profile-section h1 {
        font-size: 1.5rem !important;
        line-height: 1.3;
      }
      
      .profile-section p {
        font-size: 0.9rem !important;
        line-height: 1.4;
        margin-bottom: 0.3rem !important;
      }
      
      .social-icons {
        justify-content: center;
        gap: 1rem;
      }
    }
    
    @media (max-width: 480px) {
      .profile-section h1 {
        font-size: 1.3rem !important;
      }
      
      .profile-section p {
        font-size: 0.85rem !important;
      }
    }
     
    .pagefind-ui__search-input {
      color: black;
      width: 100%;
      padding: 0.5em;
      border-radius: 0.25em;
      border: 1px solid gray;
    }
    .pagefind-ui__search-clear {
      display: none;
    }
    .dark .pagefind-ui__search-input {
      color: white;
      background-color: #322d2d;
      width: 100%;
      padding: 0.5em;
      border-radius: 0.25em;
      border: 1px solid gray;
    }
    .dark .pagefind-ui__search-input::placeholder {
      color: #8f8f8f;
    }
    .chevron {
      transition: 300ms linear rotate;
    }
    .active > .chevron {
      transform: rotate(90deg);
    }
  </style>

  <script>
    const expandAccordion = (elem) => {
      const allPanels = Array.from(document.querySelectorAll(".panel"));
      const allAccordion = Array.from(document.querySelectorAll(".accordion"));

      if (!elem.parentElement.classList.contains("active")) {
        allAccordion.forEach((acc) => {
          acc.classList.remove("active");
        });
        elem.parentElement.classList.add("active");
        allPanels.forEach(function (elem) {
          elem.style.maxHeight = null;
        });
        let activePanel = elem.parentElement.nextElementSibling;
        if (
          activePanel.id != "skill-panel" &&
          document.querySelector("#skill-panel")
        ) {
          let skillBars = Array.from(
            document.querySelectorAll("#skill-percent")
          );
          skillBars.forEach((elem) => {
            elem.style.width = "0";
          });
        }
        activePanel.style.maxHeight = activePanel.scrollHeight + "px";
      }
    };
  </script>

  <script>
    let html = document.querySelector("html");
    let theme = window.localStorage.getItem("theme");

    const setTheme = (theme) => {
      html.classList.remove("light");
      if (theme === "dark") {
        html.classList.add("dark");
        window.localStorage.setItem("theme", "dark");
      } else {
        html.classList.remove("dark");
        window.localStorage.setItem("theme", "light");
      }
      fixThemeToggleIcon(theme);
    };

    const fixThemeToggleIcon = (theme) => {
      let themeToggle = document.querySelector(".theme-toggle");
      if (themeToggle) {
        if (theme === "dark") {
          themeToggle.classList.remove("fa-moon");
          themeToggle.classList.add("fa-sun");
        } else {
          themeToggle.classList.remove("fa-sun");
          themeToggle.classList.add("fa-moon");
        }
      }
    };

    if (theme == null) {
      if (html.classList.contains("dark")) {
        theme = "dark";
      } else if (html.classList.contains("light")) {
        theme = "light";
      } else {
        const prefersDark = window.matchMedia(
          "(prefers-color-scheme: dark)"
        ).matches;
        if (prefersDark) {
          theme = "dark";
        } else {
          theme = "light";
        }
      }
    }

    setTheme(theme);

    const toggleTheme = () => {
      html.classList.contains("dark") ? setTheme("light") : setTheme("dark");
    };

    window.onload = () => {
      fixThemeToggleIcon(theme);

      let defaultActivePanel = document.querySelector(".accordion.active");
      if (defaultActivePanel) {
        defaultActivePanel.nextElementSibling.style.maxHeight =
          defaultActivePanel.nextElementSibling.scrollHeight + "px";
      }
    };

    window.onresize = () => {
      let defaultActivePanel = document.querySelector(".accordion.active");
      if (defaultActivePanel) {
        defaultActivePanel.nextElementSibling.style.maxHeight =
          defaultActivePanel.nextElementSibling.scrollHeight + "px";
      }
    };
  </script>
</head>
<body class="h-screen p-2 m-auto max-w-4xl flex flex-col">
    
    <header
  class="nav flex flex-row row py-2 mb-6 w-full border-b border-gray-700 dark:border-gray-300 justify-between"
>
  <div>
    <a class="nav-menu-item" href="http://localhost:1313/fuss/people/subhrajit/">Home</a>
    <a class="nav-menu-item" href="/files/cv_subhrajit.pdf">CV</a>
    <a class="nav-menu-item" href="/fuss/people/subhrajit/gallery">Gallery</a>
  </div>
  <div>
    <a class="mr-4" href="/fuss/people/subhrajit/search">
      <i class="fas fa-search"></i>
    </a>
    <i
      class="fas fa-sun theme-toggle text-blue-500 hover:text-blue-700 dark:text-yellow-300 dark:hover:text-yellow-500 cursor-pointer text-lg mr-9 sm:mr-0"
      onclick="toggleTheme()"
    ></i>
  </div>
</header>



    
    <main class="grow">
<div class="grid grid-cols-1 md:grid-cols-5 gap-2 sm py-2">
  <div class="col-span-2">
    <div class="bg-gray-300 dark:bg-darker drop-shadow-md p-2 rounded-t-lg">
      <div class="flex flex-col justify-center">
        <div
  class="w-full p-2 flex justify-center align-middle profile-photo-container"
>
  <img
    class="rounded-sm"
    src="/fuss/people/subhrajit/images/profile-pic.jpg"
    alt="Subhrajit Das"
  />
</div>

        <div class="px-2 text-center">
          <div class="profile-section text-center mb-4">
  <h1 class="mb-3 text-3xl md:text-4xl font-black">Subhrajit Das</h1>
  <div class="text-center">
    
    <p class="text-base md:text-lg text-gray-250 mb-1 leading-tight">Director&#39;s PhD Fellow</p>
    
    
    <p class="text-xs md:text-sm text-gray-250 mb-1 leading-tight">Computer Science &amp; Engineering</p>
    
    
    <p class="text-sm md:text-base text-gray-250 mb-1 leading-tight">IIT Gandhinagar, Gujarat</p>
    
    
    <p class="text-sm md:text-base text-gray-250 leading-tight">India</p>
    
  </div>
</div>
<div class="mb-4 flex flex-wrap justify-center social-icons">
  
  <div class="mx-2">
    <a class="text-2xl" href="https://www.linkedin.com/in/subhrajit-das-aaa879157/">
      <i class="mt-1 fab fa-linkedin-in"></i>
    </a>
  </div>
  
  <div class="mx-2">
    <a class="text-2xl" href="https://github.com/iamsubhrajit10">
      <i class="mt-1 fab fa-github"></i>
    </a>
  </div>
  
  <div class="mx-2">
    <a class="text-2xl" href="mailto:subhrajit.das@iitgn.ac.in">
      <i class="mt-1 fas fa-envelope"></i>
    </a>
  </div>
  
</div>

          
        </div>
      </div>
    </div>
    

  </div>
  <div class="col-span-3 relative">
    
    <div class="px-2">
      <h2 class="accordion active">
        
        <p
         
          onclick="expandAccordion(this)"
          style="cursor: pointer"
        >
          <i class="fas fa-user"></i>
          Bio</p>
      </h2>

      <div
        class="panel overflow-hidden px-2 ml-2"
        
      >
        <div class=""><p class="markdownify">
  Subhrajit Das is a Director&rsquo;s PhD Fellow in the <a href="https://cs.iitgn.ac.in/">Department of Computer Science and Engineering</a> at the <a href="https://iitgn.ac.in/">Indian Institute of Technology Gandhinagar</a>, advised by <a href="https://abhishek.people.iitgn.ac.in/">Prof. Abhishek Bichhawat</a>. His research domain is within computer systems, with current work focusing on optimizing the performance of large integer arithmetic using parallelization. He holds a Master of Technology in Computer Science and Engineering from the same institute. Before that, he earned a Master of Science in Computer Science from the <a href="https://klyuniv.ac.in/">University of Kalyani</a> and a Bachelor of Science (Honours) in Computer Science from the <a href="https://wbsu.ac.in/">West Bengal State University</a>.
</p>
</div>
      </div>
    </div>
    
    <div class="px-2">
      <h2 class="accordion">
        
        <p
         
          onclick="expandAccordion(this)"
          style="cursor: pointer"
        >
          <i class="fas fa-graduation-cap"></i>
          Education</p>
      </h2>

      <div
        class="panel overflow-hidden px-2 ml-2"
        
      >
        <div class="">

<h4 style="font-weight: bold;">Ph.D. in Computer Science and Engineering</h4>
<p >2025 - Present &middot; Indian Institute of Technology Gandhinagar, India</p>



<h4 style="font-weight: bold;">Master of Technology in Computer Science and Engineering</h4>
<p >2023 - 2025 &middot; Indian Institute of Technology Gandhinagar, India</p>



<h4 style="font-weight: bold;">Master of Science in Computer Science</h4>
<p >2021 - 2023 &middot; University of Kalyani, India</p>



<h4 style="font-weight: bold;">Bachelor of Science (Honours) in Computer Science</h4>
<p >2018 - 2021 &middot; Panihati Mahavidyalaya (West Bengal State University), India</p>

</div>
      </div>
    </div>
    
    <div class="px-2">
      <h2 class="accordion">
        
        <p
         
          onclick="expandAccordion(this)"
          style="cursor: pointer"
        >
          <i class="fas fa-project-diagram"></i>
          Projects</p>
      </h2>

      <div
        class="panel overflow-hidden px-2 ml-2"
        
      >
        <div class="">
<h4>
  <a href="https://iamsubhrajit10.me/files/DigitsOnTurbo-MTech-Thesis.pdf">DigitsOnTurbo: Accelerating Large Integer Arithmetic with Parallel Addition, Subtraction, and Vedic-Based Multiplication Using AVX512</a>
</h4>
<p class="markdownify indent-8"><p><strong>M.Tech. Thesis Work</strong></p>
<ul>
<li><strong>Advisor:</strong> <a href="https://abhishek.people.iitgn.ac.in/">Prof. Abhishek Bichhawat</a>, <strong>Co-advisor:</strong> <a href="https://homepages.inf.ed.ac.uk/ypatel/">Prof. Yuvraj Patel</a> (The University of Edinburgh)</li>
<li>Designed high-performance faster data-parallel algorithms for large integer addition and subtraction using <code>AVX512</code> for most cases.</li>
<li>Achieved average execution-time speedup of 2.06x for addition and 2.32x for subtraction (up to 131k bits) compared to the GNU Multiple-Precision Arithmetic Library (<code>GMP</code>).</li>
<li>Designed a faster Vedic-based multiplication algorithm for large integers using <code>AVX512-IFMA</code> for 256-bit operands, with execution-time speedup of 1.83x compared to the <code>GMP</code> library.</li>
<li>Additionally, designed approximate variants of the proposed algorithms for large integer addition and multiplication, achieving average execution-time speedup of 2.52x and 2.80x, respectively, compared to <code>GMP</code>.</li>
</ul></p>

<h4>
  <a href="https://iamsubhrajit10.me/files/msc_thesis.pdf">Studies on Various Maximal Covering Location Problems using Genetic and Artificial Bee Colony Algorithms</a>
</h4>
<p class="markdownify indent-8"><p><strong>M.Sc. Thesis Work</strong></p>
<ul>
<li><strong>Advisor:</strong> <a href="https://klyuniv.ac.in/professors/dr-priya-ranjan-sinha-mahapatra/">Prof. Priya Ranjan Sinha Mahapatra</a>, <strong>Co-advisor:</strong> <a href="https://www.soumenatta.com/">Dr. Soumen Atta</a></li>
<li>Designed and implemented an algorithm for solving maximal covering location problems using genetic and artificial bee colony algorithms.</li>
<li>Achieved optimal benchmark results with <code>CPLEX</code> in 50% of cases, reducing the average computational time to 85.83 seconds, compared to over 1000 seconds for previous models, with an average gap of just 0.01%.</li>
</ul></p>

<h4>
  <a href="https://iamsubhrajit10.me/files/bsc_project_report.pdf">Reversible Multiplier Accumulate Unit (B.Sc. Project)</a>
</h4>
<p class="markdownify indent-8"><p><strong>B.Sc. Project Work</strong></p>
<ul>
<li>Designed a multiplier accumulate unit using reversible gates for low power consumption and heat dissipation.</li>
</ul></p>

<h4>
  <a href="https://github.com/iamsubhrajit10/Instant-Payment-Gateway">Instant Payment Gateway (IPG)</a>
</h4>
<p class="markdownify indent-8"><p><strong>Team Contributor</strong></p>
<ul>
<li>Engineered an instant payment system using Parallel and Distributed Systems concepts.</li>
<li>Facilitated seamless and secure interoperability between parties, similar to UPI.</li>
<li>Implemented efficient transaction processing with load balancing, fault tolerance, and concurrency control to ensure high availability and scalability.</li>
</ul></p>

<h4>
  <a href="https://github.com/iamsubhrajit10/Parallel-Distributed-Systems/tree/main/TennisServe">TennisServe: A Parallel Game Matching Server with OpenMP &amp; MPI</a>
</h4>
<p class="markdownify indent-8"><p><strong>Individual Contributor</strong></p>
<ul>
<li>Developed a simulation of a tennis game matching server where multiple players send requests for games: singles, doubles, male, female, or mixed.</li>
<li>Utilized OpenMP threads to handle client requests and <code>MPI</code> calls for player communication.</li>
<li>Managed the availability of limited tennis courts (4 courts) to continuously match players&rsquo; requests.</li>
<li>Completed as part of the Parallel and Distributed Course at IIT Gandhinagar.</li>
</ul></p>

</div>
      </div>
    </div>
    
    <div class="px-2">
      <h2 class="accordion">
        
        <p
         
          onclick="expandAccordion(this)"
          style="cursor: pointer"
        >
          <i class="fas fa-briefcase"></i>
          Teaching Experience</p>
      </h2>

      <div
        class="panel overflow-hidden px-2 ml-2"
        
      >
        <div class="">
<h4 style="font-weight: bold;">Teaching Assistant</h4>
<p class="mb-0">
  Jul 2023 - <em>Present</em> &middot;  Indian Institute of Technology Gandhinagar, India 
</p>

<div class="prose prose-stone dark:prose-invert max-w-none">
<ul>
<li>Assisted for the courses such as <em>Distributed Systems and Cloud Computing</em>, <em>Computer &amp; Network Security</em>, <em>Compilers</em>, and <em>Data Structures and Algorithms - I</em>.</li>
</ul>

</div>



<h4 style="font-weight: bold;">Guest Lecture on RAID</h4>
<p class="mb-0">
  Apr 2025 &middot;  Indian Institute of Technology Gandhinagar, India 
</p>

<div class="prose prose-stone dark:prose-invert max-w-none">
<ul>
<li>Given a guest lecture on RAID for the course <em>Operating Systems (CS 330)</em>.</li>
</ul>

</div>



<h4 style="font-weight: bold;">Principal Instructor</h4>
<p class="mb-0">
  Nov 2024 &middot;  Indian Institute of Technology Gandhinagar, India 
</p>

<div class="prose prose-stone dark:prose-invert max-w-none">
<ul>
<li>Served as the Principal Instructor for a Short Course titled <em>“Code Profiling and Optimization”</em> during Semester-I, 2024-25.</li>
<li>Topics covered: compiler flags (GCC/ICX), debugging (GDB), performance tools (<code>timespec</code>, <code>rusage</code>, <code>rdtsc</code>), profiling tools (<code>perf</code>, <code>valgrind</code>), and optimization strategies (caching, memory, vectorization, parallelization).</li>
</ul>

</div>



</div>
      </div>
    </div>
    
    <div class="px-2">
      <h2 class="accordion">
        
        <p
         
          onclick="expandAccordion(this)"
          style="cursor: pointer"
        >
          <i class="fas fa-book"></i>
          Publications</p>
      </h2>

      <div
        class="panel overflow-hidden px-2 ml-2"
        
      >
        <div class="">
<div class="publication-item mb-4 p-3 border-left border-primary bg-light">
  <h6 class="publication-title font-weight-bold">Online Authentication Habits of Indian Users</h6>
  
  <p class="publication-authors text-muted mb-1">
    <em>Pratyush Choudhary, <strong>Subhrajit Das</strong>, Mukul Paras Potta, Prasuj Das, and Abhishek Bichhawat</em>
  </p>
  
  
  <p class="publication-conference mb-1">
    <strong>BuildSEC 2024</strong>
     &middot; New Delhi, India
     &middot; Dec, 2024
  </p>
  
  
  <p class="publication-link mb-0">
    <a href="https://ieeexplore.ieee.org/document/10874330" target="_blank" class="btn btn-sm btn-outline-primary">
      <i class="fas fa-external-link-alt"></i> View Publication
    </a>
  </p>
  
</div>
</div>
      </div>
    </div>
    
    <div class="px-2">
      <h2 class="accordion">
        
        <p
         
          onclick="expandAccordion(this)"
          style="cursor: pointer"
        >
          <i class="fas fa-award"></i>
          Achievements</p>
      </h2>

      <div
        class="panel overflow-hidden px-2 ml-2"
        
      >
        <div class="">
<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">January 2025</span>
  </div>
  <p class="achievement-description mb-0">Selected for the Director&#39;s PhD Fellowship at the Indian Institute of Technology Gandhinagar</p>
</div>

<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">December 2024</span>
  </div>
  <p class="achievement-description mb-0">Best Paper Award for the paper &#39;Online Authentication Habits of Indian Users&#39; at BuildSEC</p>
</div>

<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">July 2023</span>
  </div>
  <p class="achievement-description mb-0">Received Ministry of Education (MoE) Scholarship for pursuing a Master&#39;s at IIT Gandhinagar</p>
</div>

<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">March 2023</span>
  </div>
  <p class="achievement-description mb-0">Achieved an All India Rank of 530 (99.30 percentile) in the Graduate Aptitude Test in Engineering (GATE) Computer Science</p>
</div>

<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">March 2023</span>
  </div>
  <p class="achievement-description mb-0">Qualified for West Bengal (WB) State Eligibility Test (SET) Lecturership in Computer Science (top 6%)</p>
</div>

<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">December 2022</span>
  </div>
  <p class="achievement-description mb-0">Achieved the University Grants Commission (UGC) National Eligibility Test (NET) Junior Research Fellowship (JRF) (top 1%)</p>
</div>

<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">December 2022</span>
  </div>
  <p class="achievement-description mb-0">Qualified for UGC NET Lectureship in Computer Science (top 6%)</p>
</div>

<div class="achievement-item mb-1 p-2 border-left border-success bg-light">
  <div class="d-flex justify-content-between align-items-start mb-1">
    <span class="achievement-date badge badge-primary">March 2022</span>
  </div>
  <p class="achievement-description mb-0">Qualified the GATE 2022 CS examination (89.94 percentile)</p>
</div>
</div>
      </div>
    </div>
    
    <div class="px-2">
      <h2 class="accordion">
        
        <p
         
          onclick="expandAccordion(this)"
          style="cursor: pointer"
        >
          <i class="fas fa-heart"></i>
          Research Interests</p>
      </h2>

      <div
        class="panel overflow-hidden px-2 ml-2"
        
      >
        <div class=""><ul class="pl-0">
  
  <li class="list-unstyled mb-2">Performance and Usability in Systems Security</li>
  
</ul>
</div>
      </div>
    </div>
        
  </div>
</div>

    </main>
    
  </body>
</html>
