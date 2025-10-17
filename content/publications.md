---
title: Publications
toc: false
---

<style>
/* Override Hextra's container constraints */
body:has(.publications-section) .hx-max-w-screen-3xl,
body:has(.publications-section) .hextra-max-page-width,
body:has(.publications-section) main > div {
  max-width: 100% !important;
  width: 100% !important;
}

body:has(.publications-section) article {
  max-width: 100% !important;
  width: 100% !important;
  padding-left: 2rem !important;
  padding-right: 2rem !important;
}

.publications-section {
  max-width: 100% !important;
  width: 100% !important;
  margin: 0 auto;
  padding: 0;
  margin-top: -1rem !important;
}

.year-section {
  margin-bottom: 4rem;
}

.year-section:first-of-type {
  margin-top: -2rem !important;
}

.year-header {
  font-size: 2.25rem;
  font-weight: 800;
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 3px solid transparent;
  border-image: linear-gradient(90deg, #4f46e5, #7c3aed, #db2777) 1;
  display: inline-block;
  position: relative;
  letter-spacing: -0.02em;
}

.dark .year-header {
  background: linear-gradient(135deg, #818cf8 0%, #a78bfa 50%, #f472b6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.publication-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(229, 231, 235, 0.2);
  border-radius: 16px;
  padding: 2rem;
  margin-bottom: 1.75rem;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
}

.publication-card:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: 0 0 20px 5px rgba(79, 70, 229, 0.15),
              0 0 40px 10px rgba(124, 58, 237, 0.1),
              0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: rgba(79, 70, 229, 0.4);
  background: rgba(255, 255, 255, 0.06);
}

.dark .publication-card {
  background: rgba(30, 41, 59, 0.4);
  border-color: rgba(51, 65, 85, 0.5);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.dark .publication-card:hover {
  border-color: rgba(129, 140, 248, 0.5);
  box-shadow: 0 0 25px 8px rgba(99, 102, 241, 0.2),
              0 0 50px 15px rgba(139, 92, 246, 0.15),
              0 4px 12px rgba(0, 0, 0, 0.4);
  background: rgba(30, 41, 59, 0.6);
}

.pub-type-badge {
  display: inline-block;
  padding: 0.375rem 1rem;
  font-size: 0.75rem;
  font-weight: 700;
  border-radius: 20px;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.75px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.pub-type-badge:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.pub-type-conference {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
  color: #1e40af;
  border: 1px solid #93c5fd;
}

.dark .pub-type-conference {
  background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
  color: #93c5fd;
  border: 1px solid #3b82f6;
}

.pub-type-journal {
  background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
  color: #166534;
  border: 1px solid #86efac;
}

.dark .pub-type-journal {
  background: linear-gradient(135deg, #14532d 0%, #166534 100%);
  color: #86efac;
  border: 1px solid #22c55e;
}

.pub-type-workshop {
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  color: #92400e;
  border: 1px solid #fcd34d;
}

.dark .pub-type-workshop {
  background: linear-gradient(135deg, #78350f 0%, #92400e 100%);
  color: #fde68a;
  border: 1px solid #f59e0b;
}

.pub-type-preprint {
  background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);
  color: #6b21a8;
  border: 1px solid #d8b4fe;
}

.dark .pub-type-preprint {
  background: linear-gradient(135deg, #581c87 0%, #6b21a8 100%);
  color: #e9d5ff;
  border: 1px solid #a855f7;
}

.pub-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.75rem;
  line-height: 1.45;
  letter-spacing: -0.01em;
}

.dark .pub-title {
  color: #f1f5f9;
}

.pub-authors {
  font-size: 1rem;
  color: #64748b;
  margin-bottom: 0.625rem;
  line-height: 1.7;
  font-weight: 400;
}

.dark .pub-authors {
  color: #94a3b8;
}

.pub-authors .author-highlight {
  font-weight: 700;
  color: #4f46e5;
  position: relative;
  transition: all 0.3s ease;
}

.publication-card:hover .pub-authors .author-highlight {
  color: #7c3aed;
}

.dark .pub-authors .author-highlight {
  color: #818cf8;
}

.dark .publication-card:hover .pub-authors .author-highlight {
  color: #a78bfa;
}

.pub-venue {
  font-size: 0.95rem;
  color: #475569;
  margin-bottom: 0.75rem;
  font-style: italic;
  line-height: 1.6;
  padding: 0.75rem 1rem;
  background: rgba(79, 70, 229, 0.03);
  border-left: 3px solid rgba(79, 70, 229, 0.2);
  border-radius: 6px;
  transition: all 0.3s ease;
}

.publication-card:hover .pub-venue {
  background: rgba(79, 70, 229, 0.06);
  border-left-color: rgba(79, 70, 229, 0.4);
}

.dark .pub-venue {
  color: #cbd5e1;
  background: rgba(129, 140, 248, 0.05);
  border-left-color: rgba(129, 140, 248, 0.25);
}

.dark .publication-card:hover .pub-venue {
  background: rgba(129, 140, 248, 0.08);
  border-left-color: rgba(129, 140, 248, 0.4);
}

.pub-venue strong {
  font-weight: 700;
  color: #1e293b;
  font-style: normal;
}

.dark .pub-venue strong {
  color: #e2e8f0;
}

.pub-links {
  display: flex;
  gap: 0.875rem;
  flex-wrap: wrap;
  margin-top: 1.25rem;
}

.pub-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 10px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  border: 2px solid transparent;
  position: relative;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.pub-link::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.pub-link:hover::before {
  opacity: 1;
}

.pub-link-pdf {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: white;
  border-color: #b91c1c;
}

.pub-link-pdf:hover {
  background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 16px rgba(239, 68, 68, 0.4),
              0 4px 8px rgba(239, 68, 68, 0.25);
}

.pub-link-code {
  background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
  color: white;
  border-color: #4338ca;
}

.pub-link-code:hover {
  background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 16px rgba(99, 102, 241, 0.4),
              0 4px 8px rgba(99, 102, 241, 0.25);
}

.pub-link-slides {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border-color: #047857;
}

.pub-link-slides:hover {
  background: linear-gradient(135deg, #059669 0%, #047857 100%);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 16px rgba(16, 185, 129, 0.4),
              0 4px 8px rgba(16, 185, 129, 0.25);
}

.pub-link-video {
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  color: white;
  border-color: #b45309;
}

.pub-link-video:hover {
  background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 16px rgba(245, 158, 11, 0.4),
              0 4px 8px rgba(245, 158, 11, 0.25);
}

.pub-link-doi {
  background: linear-gradient(135deg, #64748b 0%, #475569 100%);
  color: white;
  border-color: #334155;
}

.pub-link-doi:hover {
  background: linear-gradient(135deg, #475569 0%, #334155 100%);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 16px rgba(100, 116, 139, 0.4),
              0 4px 8px rgba(100, 116, 139, 0.25);
}

.pub-link:active {
  transform: translateY(-1px) scale(1.02);
}

.pub-award {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.375rem 0.75rem;
  background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
  color: #78350f;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 6px;
  margin-top: 0.75rem;
}

.dark .pub-award {
  background: linear-gradient(135deg, #92400e 0%, #78350f 100%);
  color: #fde68a;
}
</style>

<div class="year-section">
  <h2 class="year-header">2025</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Johnny can’t revoke consent either: measuring compliance of consent revocation on the web</h3>
    <p class="pub-authors">
      <span class="author-highlight">GP Kancherla</span>, N Bielova, C Santos, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>Proceedings on Privacy Enhancing Technologies</strong>, 2025, 2025
    </p>
    <div class="pub-links">
      <a href="https://petsymposium.org/popets/2025/popets-2025-0133.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:dhFuZR0502QC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">How Usable is Consent Withdrawal on the Web? UI Requirements and Expert Evaluation</h3>
    <p class="pub-authors">
      S Ahuja, <span class="author-highlight">GP Kancherla</span>, CT Santos, N Bielova, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>2025/10/7</strong>, 2025
    </p>
    <div class="pub-links">
      <a href="https://hal.science/hal-05302086v1/file/APVP_25__Usability_Consent_Withdrawal.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:_Qo2XoVZTnwC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Least Privilege Access for Persistent Storage Mechanisms in Web Browsers</h3>
    <p class="pub-authors">
      <span class="author-highlight">GP Kancherla</span>, D Goel, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>Proceedings of the ACM on Web Conference 2025</strong>, 4832-4840,  2025, 2025
    </p>
    <div class="pub-links">
      <a href="https://dl.acm.org/doi/pdf/10.1145/3696410.3714887" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:QIV2ME_5wuYC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">A Unified Browser-Based Consent Management Framework</h3>
    <p class="pub-authors">
      <span class="author-highlight">GP Kancherla</span>, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>2025 IEEE/ACM 47th International Conference on Software Engineering: New …</strong>, 2025, 2025
    </p>
    <div class="pub-links">
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:hFOr9nPyWt4C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">On the Prevalence and Usage of Commit Signing on GitHub: A Longitudinal and Cross-Domain Study</h3>
    <p class="pub-authors">
      A Sharma, <span class="author-highlight">S Karmakar</span>, <span class="author-highlight">GP Kancherla</span>, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>arXiv preprint arXiv:2504.19215</strong>, 2025, 2025
    </p>
    <div class="pub-links">
      <a href="https://arxiv.org/pdf/2504.19215" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:-f6ydRqryjwC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Worst-Case Response Time Analysis for Periodic Programs with Nested Locks</h3>
    <p class="pub-authors">
      HM Ramolia, SS Kanawade, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>Proceedings of the 18th Innovations in Software Engineering Conference</strong>, 1-6,  2025, 2025
    </p>
    <div class="pub-links">
      <a href="https://dl.acm.org/doi/pdf/10.1145/3717383.3717392" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:hC7cP41nSMkC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2024</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Online Authentication Habits of Indian Users</h3>
    <p class="pub-authors">
      P Choudhary, <span class="author-highlight">S Das</span>, MP Potta, P Das, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>2024 Conference on Building a Secure &amp; Empowered Cyberspace (BuildSEC)</strong>, 66-73,  2024, 2024
    </p>
    <div class="pub-links">
      <a href="https://arxiv.org/pdf/2501.14330" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:IWHjjKOFINEC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Web Privacy Perceptions Amongst Indian Users</h3>
    <p class="pub-authors">
      <span class="author-highlight">G Priyadarsini</span>, A Saxena, A Dey, Prakriti, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>International Conference on Information Systems Security</strong>, 289-309,  2024, 2024
    </p>
    <div class="pub-links">
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:ZeXyd9-uunAC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2023</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Towards Usable Security Analysis Tools for {Trigger-Action} Programming</h3>
    <p class="pub-authors">
      MK McCall, E Zeng, FH Shezan, M Yang, L Bauer, <span class="author-highlight">A Bichhawat</span>, C Cobb, ...
    </p>
    <p class="pub-venue"><strong>Nineteenth Symposium on Usable Privacy and Security (SOUPS 2023)</strong>, 301-320,  2023, 2023
    </p>
    <div class="pub-links">
      <a href="https://www.usenix.org/system/files/soups2023-mccall.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:M3ejUd6NZC8C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Layered Symbolic Security Analysis in</h3>
    <p class="pub-authors">
      K Bhargavan, <span class="author-highlight">A Bichhawat</span>, P Hosseyni, R Küsters, K Pruiksma, ...
    </p>
    <p class="pub-venue"><strong>European Symposium on Research in Computer Security</strong>, 3-21,  2023, 2023
    </p>
    <div class="pub-links">
      <a href="https://elib.uni-stuttgart.de/bitstreams/c91e5288-7d38-40c6-849b-d0bc54e09cb4/download" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:Wp0gIr-vW9MC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Tainted Secure Multi-Execution to Restrict Attacker Influence</h3>
    <p class="pub-authors">
      MK McCall, <span class="author-highlight">A Bichhawat</span>, L Jia
    </p>
    <p class="pub-venue"><strong>Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications …</strong>, 2023, 2023
    </p>
    <div class="pub-links">
      <a href="https://dl.acm.org/doi/pdf/10.1145/3576915.3623110" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:mVmsd5A6BfQC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2022</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Noise: A library of verified high-performance secure channel protocol implementations</h3>
    <p class="pub-authors">
      S Ho, J Protzenko, <span class="author-highlight">A Bichhawat</span>, K Bhargavan
    </p>
    <p class="pub-venue"><strong>2022 IEEE Symposium on Security and Privacy (SP)</strong>, 107-124,  2022, 2022
    </p>
    <div class="pub-links">
      <a href="https://inria.hal.science/hal-03946578/document" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:3fE2CSJIrl8C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Compositional information flow monitoring for reactive programs</h3>
    <p class="pub-authors">
      MK McCall, <span class="author-highlight">A Bichhawat</span>, L Jia
    </p>
    <p class="pub-venue"><strong>2022 IEEE 7th European Symposium on Security and Privacy (EuroS&amp;P)</strong>, 467-486,  2022, 2022
    </p>
    <div class="pub-links">
      <a href="https://par.nsf.gov/servlets/purl/10385222" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:kNdYIx-mwKoC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2021</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">DY*: A Modular Symbolic Verification Framework for Executable Cryptographic Protocol Code</h3>
    <p class="pub-authors">
      K Bhargavan, <span class="author-highlight">A Bichhawat</span>, QH Do, P Hosseyni, R Küsters, G Schmitz, ...
    </p>
    <p class="pub-venue"><strong>2021 IEEE European Symposium on Security and Privacy (EuroS&amp;P)</strong>, 523-542,  2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://inria.hal.science/hal-03178425/file/dy-star-eurosp21.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:_FxGoFyzp5QC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">An in-depth symbolic security analysis of the ACME standard</h3>
    <p class="pub-authors">
      K Bhargavan, <span class="author-highlight">A Bichhawat</span>, QH Do, P Hosseyni, R Küsters, G Schmitz, ...
    </p>
    <p class="pub-venue"><strong>Proceedings of the 2021 ACM SIGSAC conference on computer and communications …</strong>, 2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://eprint.iacr.org/2021/1457.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:Se3iqnhoufwC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">SAFETAP: An efficient incremental analyzer for trigger-action programs</h3>
    <p class="pub-authors">
      MK McCall, FH Shezan, <span class="author-highlight">A Bichhawat</span>, C Cobb, L Jia, Y Tian, C Grace, ...
    </p>
    <p class="pub-venue"><strong>Carnegie Mellon University</strong>, 2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://kilthub.cmu.edu/articles/report/SafeTAP_An_Efficient_Incremental_Analyzer_for_Trigger-Action_Programs/14792271/1/files/28433025.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:WF5omc3nYNoC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Gradual security types and gradual guarantees</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, MK McCall, L Jia
    </p>
    <p class="pub-venue"><strong>2021 IEEE 34th Computer Security Foundations Symposium (CSF)</strong>, 1-16,  2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://par.nsf.gov/servlets/purl/10385221" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:ufrVoPGSRksC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">A Tutorial-Style Introduction to</h3>
    <p class="pub-authors">
      K Bhargavan, <span class="author-highlight">A Bichhawat</span>, QH Do, P Hosseyni, R Küsters, G Schmitz, ...
    </p>
    <p class="pub-venue"><strong>Protocols</strong>, Strands,  and Logic: Essays Dedicated to Joshua Guttman on the …,  2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://publ.sec.uni-stuttgart.de/bhargavanbichhavatdohosseynikuestersschmitzwuertele-guttmanfest-2021.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:YsMSGLbcyi4C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Permissive runtime information flow control in the presence of exceptions</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, V Rajani, D Garg, C Hammer
    </p>
    <p class="pub-venue"><strong>Journal of Computer Security 29 (4)</strong>, 361-401,  2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://people.mpi-sws.org/~dg/papers/jcs21.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:zYLM7Y9cAGgC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">DY⋆ Code Repository</h3>
    <p class="pub-authors">
      K Bhargavan, <span class="author-highlight">A Bichhawat</span>, QH Do, P Hosseyni, R Küsters, G Schmitz, ...
    </p>
    <p class="pub-venue"><strong>URL: https://github. com/reprosec/dolev-yao-star</strong>, 2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:Y0pCki6q_DkC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Automating Audit with Policy Inference</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, M Fredrikson, J Yang
    </p>
    <p class="pub-venue"><strong>2021 IEEE 34th Computer Security Foundations Symposium (CSF)</strong>, 1-16,  2021, 2021
    </p>
    <div class="pub-links">
      <a href="https://www.cs.cmu.edu/~abichhaw/fullpublication/CSF21.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:UebtZRa9Y70C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2020</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Contextual and granular policy enforcement in database-backed applications</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, M Fredrikson, J Yang, A Trehan
    </p>
    <p class="pub-venue"><strong>Proceedings of the 15th ACM Asia Conference on Computer and Communications …</strong>, 2020, 2020
    </p>
    <div class="pub-links">
      <a href="https://dl.acm.org/doi/pdf/10.1145/3320269.3384759" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:u-x6o8ySG0sC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">First-order Gradual Information Flow Types with Gradual Guarantees</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, MK McCall, L Jia
    </p>
    <p class="pub-venue"><strong>arXiv preprint arXiv:2003.12819</strong>, 2020, 2020
    </p>
    <div class="pub-links">
      <a href="https://arxiv.org/pdf/2003.12819" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:u5HHmVD_uO8C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2017</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">WebPol: Fine-grained information flow policies for web browsers</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, V Rajani, J Jain, D Garg, C Hammer
    </p>
    <p class="pub-venue"><strong>European Symposium on Research in Computer Security</strong>, 242-259,  2017, 2017
    </p>
    <div class="pub-links">
      <a href="https://arxiv.org/pdf/1706.06932" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:d1gkVwhDpl0C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Practical dynamic information flow control</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>Saarländische Universitäts-und Landesbibliothek</strong>, 2017, 2017
    </p>
    <div class="pub-links">
      <a href="https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/27103/1/thesis.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:2osOgNQ5qMEC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2015</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Information flow control for event handling and the DOM in web browsers</h3>
    <p class="pub-authors">
      V Rajani, <span class="author-highlight">A Bichhawat</span>, D Garg, C Hammer
    </p>
    <p class="pub-venue"><strong>2015 IEEE 28th Computer Security Foundations Symposium</strong>, 366-379,  2015, 2015
    </p>
    <div class="pub-links">
      <a href="https://people.mpi-sws.org/~dg/papers/csf15-ifc-full.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:hqOjcs7Dif8C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Post-dominator analysis for precisely handling implicit flows</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>2015 IEEE/ACM 37th IEEE International Conference on Software Engineering 2 …</strong>, 2015, 2015
    </p>
    <div class="pub-links">
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:8k81kl-MbHgC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2014</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Information flow control in WebKit’s JavaScript bytecode</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, V Rajani, D Garg, C Hammer
    </p>
    <p class="pub-venue"><strong>International conference on principles of security and trust</strong>, 159-178,  2014, 2014
    </p>
    <div class="pub-links">
      <a href="https://arxiv.org/pdf/1401.4339" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:LkGwnXOMwfcC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Generalizing permissive-upgrade in dynamic information flow analysis</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, V Rajani, D Garg, C Hammer
    </p>
    <p class="pub-venue"><strong>Proceedings of the Ninth Workshop on Programming Languages and Analysis for …</strong>, 2014, 2014
    </p>
    <div class="pub-links">
      <a href="https://arxiv.org/pdf/1506.03950" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:Tyk-4Ss8FVUC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Exception handling for dynamic information flow control</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>Companion Proceedings of the 36th International Conference on Software …</strong>, 2014, 2014
    </p>
    <div class="pub-links">
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:5nxA0vEk-isC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2011</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Security architecture for virtual machines</h3>
    <p class="pub-authors">
      U Tupakula, V Varadharajan, <span class="author-highlight">A Bichhawat</span>
    </p>
    <p class="pub-venue"><strong>International Conference on Algorithms and Architectures for Parallel …</strong>, 2011, 2011
    </p>
    <div class="pub-links">
      <a href="https://www.academia.edu/download/47964836/Security_architecture_for_virtual_machines.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:qjMakFHDy7sC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Proactive Fault Tolerance Technique for a Mobile Grid Environment</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, RC Joshi
    </p>
    <p class="pub-venue"><strong>International Conference on Advances in Computing and Communication</strong>, 96-101,  2011, 2011
    </p>
    <div class="pub-links">
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:roLk4NBRz8UC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">2010</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">A survey on issues in mobile grid computing</h3>
    <p class="pub-authors">
      <span class="author-highlight">A Bichhawat</span>, RC Joshi
    </p>
    <p class="pub-venue"><strong>Int J Recent Trends Eng. Technol 4 (2)</strong>, 2010, 2010
    </p>
    <div class="pub-links">
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:eQOLeE2rZwMC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

<div class="year-section">
  <h2 class="year-header">Misc.</h2>
  
  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Restricting Attacker Influence in Reactive Programs with Dynamic Secrets</h3>
    <p class="pub-authors">
      MK McCall, <span class="author-highlight">A Bichhawat</span>, L Jia
    </p>
    <p class="pub-venue"><strong>Carnegie Mellon University</strong>, 0
    </p>
    <div class="pub-links">
      <a href="https://kilthub.cmu.edu/articles/report/Restricting_Attacker_Influence_in_Reactive_Programs_with_Dynamic_Secrets/22296628/1/files/39675085.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:4TOpqqG69KYC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Poster: Security in Web-Based Workflows</h3>
    <p class="pub-authors">
      T Bauereiß, <span class="author-highlight">A Bichhawat</span>, I Bolosteanu, P Faymonville, B Finkbeiner, ...
    </p>
    <p class="pub-venue"><em>Publication venue information not available</em>
    </p>
    <div class="pub-links">
      <a href="https://www.ieee-security.org/TC/SP2015/posters/paper_60.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:W7OEmFMy1HYC" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>


  <div class="publication-card">
    <span class="pub-type-badge pub-type-conference">Conference</span>
    <h3 class="pub-title">Status Report: Formal Analysis of Web Security</h3>
    <p class="pub-authors">
      K Bhargavan, <span class="author-highlight">A Bichhawat</span>, QH Do, D Fett, R Küsters, G Schmitz
    </p>
    <p class="pub-venue"><em>Publication venue information not available</em>
    </p>
    <div class="pub-links">
      <a href="https://st.fbk.eu/assets/areas/events/OSW2018/osw2018_paper_1.pdf" target="_blank" class="pub-link pub-link-pdf">📄 PDF</a>
      <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=JX0CWckAAAAJ&amp;pagesize=100&amp;citation_for_view=JX0CWckAAAAJ:IjCSPb-OGe4C" target="_blank" class="pub-link pub-link-doi">🔗 Google Scholar</a>
    </div>
  </div>

</div>

