---
layout: page
title: Resume
permalink: /resume/
---
---
title: "Michał Michalski"
subtitle: "CTO & Lead AI Software Engineer"
author: |
  Poznań, Poland • [michal@buyuk-dev.com](mailto:michal@buyuk-dev.com) • [buyuk-dev.com](https://buyuk-dev.com) • [calendar](https://calendly.com/buyuk) • +48 514 954 985
header-includes:
  - |
    ```{=latex}
    \usepackage{titling}
    \usepackage{fontspec}
    \defaultfontfeatures{Ligatures=TeX,Scale=MatchLowercase}
    % Fonts: SF Pro Text (body), SF Pro Display (headings)
    % Map bold to Semibold for cleaner weight; set italics explicitly.
    \setsansfont[
      BoldFont={SF Pro Text Semibold}
    ]{SF Pro Text}
    \newfontfamily\headingfont[
      UprightFont={SF Pro Display},
      BoldFont={SF Pro Display Semibold}
    ]{SF Pro Display}
    % Use sans family by default for a modern look
    \renewcommand{\familydefault}{\sfdefault}
    % Section headings use Display face with slight letter spacing
    \usepackage{sectsty}
    \allsectionsfont{\headingfont\bfseries\addfontfeatures{LetterSpace=1.2}}
    % Slight tracking for bold text to avoid fill-in at small sizes
    \DeclareTextFontCommand{\textbf}{\bfseries\addfontfeatures{LetterSpace=1.0}}
    % Line and paragraph spacing
    \usepackage{setspace}
    \setstretch{1.3}
    \setlength{\parskip}{0.6em}
    \setlength{\parindent}{0pt}
    % Tighter list spacing to reduce page length
    \usepackage{enumitem}
    \setlist[itemize]{topsep=0.25em,itemsep=0.2em,parsep=0em,partopsep=0em,leftmargin=1.2em}
    % Keep headings with following content to avoid widows/orphans
    \usepackage{needspace}
    \clubpenalty=10000
    \widowpenalty=10000
    \displaywidowpenalty=10000
    \usepackage[most]{tcolorbox}
    \usepackage{xparse}
    \makeatletter
    % capture subtitle text and expose as \@subtitle
    \newcommand{\@subtitle}{}
    \newcommand{\subtitle}[1]{\gdef\@subtitle{#1}}
    % centered compact title block with rule
    \renewcommand{\maketitle}{%
      \begin{center}
        {\LARGE\bfseries \@title\par}
        {\large\itshape \@subtitle\par}
        {\normalsize \@author\par}
      \end{center}\vspace{0.25em}%
      \begin{center}\rule{0.9\textwidth}{0.4pt}\end{center}}
    \makeatother
    % use sans-serif as default family for a cleaner look
    \renewcommand{\familydefault}{\sfdefault}
    % pastel tag colors for pill badges
    \definecolor{TagBlue}{HTML}{D1E4FF}
    \definecolor{TagTeal}{HTML}{CCF5F0}
    \definecolor{TagGreen}{HTML}{CDEFD6}
    \definecolor{TagYellow}{HTML}{FFE9B3}
    \definecolor{TagPink}{HTML}{FFD6E7}
    \definecolor{TagPurple}{HTML}{E2D6FF}
    \definecolor{TagOrange}{HTML}{FFD9C2}
    \definecolor{TagGray}{HTML}{E5E7EB}
    % \skillpill[Color]{Text} inline capsule
    \NewDocumentCommand{\skillpill}{ O{TagGray} m }{%
      \tcbox[
        on line,
        colback=#1,
        colframe=#1!60!black,
        boxrule=0.4pt,
        arc=8pt,
        left=8pt,right=8pt,top=3pt,bottom=3pt,
        boxsep=0pt,
        enhanced
      ]{\textsf{\footnotesize #2}}\hspace{4pt}}
    \newcommand{\pillcore}[1]{\skillpill[TagPurple]{#1}}% core AI
    \newcommand{\pilllang}[1]{\skillpill[TagBlue]{#1}}% languages
    \newcommand{\pillfw}[1]{\skillpill[TagTeal]{#1}}% frameworks/libs
    \newcommand{\pilldb}[1]{\skillpill[TagGreen]{#1}}% databases/cache
    \newcommand{\pillcloud}[1]{\skillpill[TagBlue]{#1}}% clouds
    \newcommand{\pilldev}[1]{\skillpill[TagOrange]{#1}}% devops/tooling
    % Role and Tech helpers
    \newcommand{\role}[3]{% company, title, dates
      \needspace{5\baselineskip}%
      \noindent\begin{minipage}[t]{0.72\textwidth}\textbf{#1} — \textit{#2}\end{minipage}%
      \hfill\begin{minipage}[t]{0.26\textwidth}\raggedleft #3\end{minipage}\\[-0.25em]}
    \newcommand{\tech}[1]{\textcolor{gray}{\footnotesize #1}}
    % Education helpers
    \newcommand{\edu}[3]{% university, department, dates
      \needspace{5\baselineskip}%
      \noindent\begin{minipage}[t]{0.72\textwidth}\textbf{#1} — \textit{#2}\end{minipage}%
      \hfill\begin{minipage}[t]{0.26\textwidth}\raggedleft #3\end{minipage}}
    ```
---

Hands‑on engineering leader building agentic automation, high‑throughput data pipelines, and production ready LLM systems. Co‑founded Fractile (acquired by T12); Currently leading \mbox{\href{https://www.intelliroom.ai/}{IntelliRoom}} - AI Due Diligence platform.

\vspace{0.9em}
\begin{center}
\begin{minipage}{0.9\textwidth}\centering
\pillcore{LangChain} \pilllang{Python} \pillfw{FastAPI} \pillcore{AI Agents} \pilldev{Docker} \pilldb{PostgreSQL} \pillcloud{Azure} \pillcore{LLMs} \pillfw{Flask} \pilllang{C++} \pilldb{Redis} \pilllang{JavaScript} \pillcloud{AWS} \pilldev{Linux} \pillfw{Vue} \pilldev{K8s} \pilllang{C\#} \pilldev{Prefect} \pillcore{RAG} \pilldev{Git}
\end{minipage}
\end{center}

## Work Experience

\role{T12 Inc}{CTO / Lead AI Software Engineer}{01.2025 – present}
\tech{LLM, LangChain, Python, JavaScript, FastAPI, Redis, PostgreSQL, MongoDB, AWS, Docker, K8s}

\begin{itemize}
\item Leading \mbox{\href{https://www.intelliroom.ai/}{IntelliRoom}} development - AI Due Diligence platform.
\item Productizing LLM techniques to improve accuracy/UX; preparing core IP (patent pending).
\item Optimizing infrastructure costs (cut AWS spending in half).
\end{itemize}


\role{Scalo}{Lead AI Software Engineer (Contract)}{03.2025 – present}
\tech{LLM, LangChain, Python, Flask, Prefect, Docker, Redis, PostgreSQL, Azure, Jira API}

\begin{itemize}
\item Built multi-source LLM‑agent pipeline automating reporting and project insights.
\item Unified ERP/CRM/PM ingestion with Prefect flows, Redis, and Azure.
\item Shipped LangChain + Flask services cutting manual report prep for PMs.
\end{itemize}


\role{Fractile sp. z o.o.}{Co-founder \& CTO / Lead Developer}{05.2024 – 03.2025}
\tech{LLM, GPT, LangChain, LlamaIndex, Python, FastAPI, Flask, Vue, Docker, K8s, PostgreSQL, Azure}

+ Built Agentic RAG platform for B2B customers (acquired).
+ Led R&D effort to develop novel methods and tools for improving AI agents.
+ Orchestrated Fractile's acquisition by T12 Inc and transitioned platform IP and roadmap.


\role{Microsoft}{Software Engineer II (FTE)}{05.2023 – 06.2024}
\tech{C\#, Azure, Service Fabric, Kusto, Cosmos DB, Event Hubs, ADLS Gen2, ChatGPT, Azure AI Services}

+ Delivered features and fixes for a large-scale distributed data processing service.
+ Led live‑site monitoring and on‑call, improving service reliability.
+ Mentored new hires; contributed ChatGPT/Azure OpenAI side project.

\role{P\&P Solutions}{Senior Software Engineer (Contract)}{01.2023 – 02.2024}
\tech{C++, Python}

+ Maintained and enhanced an airline optimization engine with advanced features.
+ Introduced Python/pytest E2E tests; standardized quality with Clang tools.
+ Prototyped a metaheuristic alternative to the core algorithm.


\role{Career Break}{newborn child}{10.2021 - 12.2022}


\role{ActiveVideo Engineering}{Senior Software Engineer (FTE)}{08.2020 – 09.2021}
\tech{C++, Python, Elasticsearch}

+ Built HTTP proxy for remote OpenGL rendering in AppCloud.
+ Created an end‑to‑end test framework improving reliability.


\role{Samsung Research and Development}{Software Engineer (Contract)}{09.2018 – 06.2020}
\tech{C++, JavaScript, Python, WebIDL, Doxygen, API design, JIRA, OpenCL, Bixby}

+ MediaController module owner for Tizen Web API; major contributor.
+ Shipped [EWIDL](https://ieeexplore.ieee.org/document/9240696) - documentation management system used in Tizen API.
+ Optimized ToF sensor software in flagship smartphone;


\role{Nokia}{Software Engineer (Contract)}{03.2017 – 08.2018}
\tech{C++, Python, TTCN3, Flask, SQLite, SQLAlchemy, Crucible/Fisheye API}

+ Developed LTE base‑station components with robust system tests.
+ Automated workflows; active in code reviews and SCRUM.


\role{Hewlett‑Packard Enterprise}{Designer / Backend C++ Developer (FTE)}{02.2016 – 02.2017}
\tech{C++, Python, Bash, Informatica}

+ Backend C++ for airline reservation systems; workflow automation.
+ Supported a Rolls‑Royce big‑data processing system.


\role{Zylia}{Research \& Development Software Engineer (Intern → FTE)}{06.2014 – 02.2016}
\tech{C++, Python, JavaScript, Django, Celery, AWS, GStreamer}

+ Built STB OS components and multimedia processing pipelines.
+ Researched audio algorithms; implemented H264 watermark decoder.


## Education

\edu{Poznań University of Technology}{Computer Science}{2012 – 2016}

+ B.Sc. Computer Science coursework completed without obtaining a degree.
