\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{Phenikaa-report}[2026/04/08 Class bao cao tong ket de tai Phenikaa]

\LoadClass[12pt, oneside]{article}

% --- Tiếng Việt & font ---
\RequirePackage[utf8]{inputenc}
\RequirePackage[T5]{fontenc}
\RequirePackage{vntex}

% Load amsmath TRƯỚC txfonts để tránh conflict \iint, \iiint
\RequirePackage{amsmath,amssymb}
\RequirePackage{txfonts}

\AtBeginDocument{\fontsize{13pt}{17pt}\selectfont}

% --- Lề: A4, trái 3cm, còn lại 2cm ---
\RequirePackage[
  a4paper,
  top=2cm,
  bottom=2cm,
  left=3cm,
  right=2cm
]{geometry}

\RequirePackage{setspace}
\setstretch{1.3}

% --- Header và Footer ---
\RequirePackage{fancyhdr}
\setlength{\headheight}{14.5pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{An toàn phần mềm-1-1-26(N01)}
\fancyhead[R]{Lab3: Secure Memory \& Risk Assessment}
\fancyfoot[L]{SVTH: Nguyễn Xuân Mạnh}
\fancyfoot[R]{Trang \thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

% Áp dụng cho trang đầu mỗi section (plain mặc định)
\fancypagestyle{plain}{%
  \fancyhf{}
  \fancyhead[L]{An toàn phần mềm-1-1-26(N01)}
    \fancyhead[R]{Lab3: Secure Memory \& Risk Assessment}
  \fancyfoot[L]{SVTH: Nguyễn Xuân Mạnh}
  \fancyfoot[R]{Trang \thepage}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\footrulewidth}{0.4pt}
}

% --- Đồ họa & bảng ---
\RequirePackage{graphicx}
\RequirePackage{tabularx}
\RequirePackage{colortbl}
\RequirePackage{xcolor}
\RequirePackage{booktabs}
\RequirePackage{longtable}

\graphicspath{{Images/}}

% Xóa triệt để khoảng cách thừa giữa ảnh và caption
\RequirePackage{caption}
\captionsetup[figure]{skip=2pt}
\setlength{\abovecaptionskip}{2pt}
\setlength{\belowcaptionskip}{0pt}

% --- Cấu hình code blocks (listings) ---
\RequirePackage{listings}
\lstset{
    basicstyle=\ttfamily\footnotesize,
    backgroundcolor=\color{gray!10},
    frame=single,
    rulecolor=\color{gray!30},
    keywordstyle=\color{black}\bfseries,
    commentstyle=\color{black}\itshape,
    stringstyle=\color{black},
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    numbersep=8pt,
    showstringspaces=false,
    breaklines=true,
    breakatwhitespace=false,
    tabsize=4,
    captionpos=b,
    aboveskip=1em,
    belowskip=1em,
    extendedchars=true,
    literate={á}{{\'a}}1 {à}{{\`a}}1 {ã}{{\~a}}1 {ạ}{{\d{a}}}1 {ả}{{\h{a}}}1 {ă}{{\u{a}}}1 {ắ}{{\'{\u{a}}}}1 {ằ}{{\`{\u{a}}}}1 {ẵ}{{\~{\u{a}}}}1 {ặ}{{\d{\u{a}}}}1 {ẳ}{{\h{\u{a}}}}1 {â}{{\^a}}1 {ấ}{{\'{\^a}}}1 {ầ}{{\`{\^a}}}1 {ẫ}{{\~{\^a}}}1 {ậ}{{\d{\^a}}}1 {ẩ}{{\h{\^a}}}1 {đ}{{\dj}}1 {é}{{\'e}}1 {è}{{\`e}}1 {ẽ}{{\~e}}1 {ẹ}{{\d{e}}}1 {ẻ}{{\h{e}}}1 {ê}{{\^e}}1 {ế}{{\'{\^e}}}1 {ề}{{\`{\^e}}}1 {ễ}{{\~{\^e}}}1 {ệ}{{\d{\^e}}}1 {ể}{{\h{\^e}}}1 {í}{{\'i}}1 {ì}{{\`i}}1 {ĩ}{{\~i}}1 {ị}{{\d{i}}}1 {ỉ}{{\h{i}}}1 {ó}{{\'o}}1 {ò}{{\`o}}1 {õ}{{\~o}}1 {ọ}{{\d{o}}}1 {ỏ}{{\h{o}}}1 {ô}{{\^o}}1 {ố}{{\'{\^o}}}1 {ồ}{{\`{\^o}}}1 {ỗ}{{\~{\^o}}}1 {ộ}{{\d{\^o}}}1 {ổ}{{\h{\^o}}}1 {ơ}{{\textornaments o}}1 {ớ}{{\'{\textornaments o}}}1 {ờ}{{\`{\textornaments o}}}1 {ỡ}{{\~{\textornaments o}}}1 {ợ}{{\d{\textornaments o}}}1 {ở}{{\h{\textornaments o}}}1 {ú}{{\'u}}1 {ù}{{\`u}}1 {ũ}{{\~u}}1 {ụ}{{\d{u}}}1 {ủ}{{\h{u}}}1 {ư}{{\textornaments u}}1 {ứ}{{\'{\textornaments u}}}1 {ừ}{{\`{\textornaments u}}}1 {ữ}{{\~{\textornaments u}}}1 {ự}{{\d{\textornaments u}}}1 {ử}{{\h{\textornaments u}}}1 {ý}{{\'y}}1 {ỳ}{{\`y}}1 {ỹ}{{\~y}}1 {ỵ}{{\d{y}}}1 {ỷ}{{\h{y}}}1 {Đ}{{\DJ}}1
}

% --- Tiện ích ---
\RequirePackage{tikz}
\usetikzlibrary{calc}
\RequirePackage{indentfirst}
\RequirePackage{hyperref}
\RequirePackage{enumitem}
\RequirePackage{float}

% --- Biểu đồ ---
\RequirePackage{pgfplots}
\pgfplotsset{compat=1.18}

\hypersetup{
  colorlinks=false,
  pdfborder={0 0 0},
}

% --- Gạch đầu dòng dùng dấu gạch ngang ---
\setlist[itemize,1]{label=--}
\setlist[itemize,2]{label=--}
\setlist[itemize,3]{label=--}

% --- Cỡ chữ tiêu đề section = 13pt (đồng bộ với nội dung) ---
\RequirePackage{titlesec}
\titleformat{\section}
  {\fontsize{13pt}{17pt}\selectfont\bfseries}
  {\thesection}{1em}{}
\titleformat{\subsection}
  {\fontsize{13pt}{17pt}\selectfont\bfseries}
  {\thesubsection}{1em}{}
\titleformat{\subsubsection}
  {\fontsize{13pt}{17pt}\selectfont\bfseries}
  {\thesubsubsection}{1em}{}
\titlespacing*{\section}{0pt}{12pt}{6pt}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}
\titlespacing*{\subsubsection}{0pt}{8pt}{4pt}

% --- Vẽ khung viền trang bìa ---
\newcommand{\drawborder}{%
  \begin{tikzpicture}[overlay, remember picture]
    \draw[line width=1pt]
      ($(current page.north west)+(2.7cm,-1.5cm)$)
      rectangle
      ($(current page.south east)+(-1.5cm,1.5cm)$);
    \draw[line width=2.5pt]
      ($(current page.north west)+(2.9cm,-1.7cm)$)
      rectangle
      ($(current page.south east)+(-1.7cm,1.7cm)$);
  \end{tikzpicture}%
}

% --- Tiêu đề trường dùng trong trang bìa ---
\newcommand{\schoolheader}{%
  \begin{center}
    {\fontsize{13pt}{16pt}\selectfont\textbf{ĐẠI HỌC PHENIKAA}}\\[2pt]
    {\fontsize{14pt}{17pt}\selectfont\textbf{TRƯỜNG CÔNG NGHỆ THÔNG TIN PHENIKAA}}\\[4pt]
    \rule{3cm}{0.6pt}
  \end{center}%
}

% --- Cấu hình Mục lục đẹp hơn ---
\RequirePackage{tocloft}
% Căn giữa và in hoa tiêu đề các danh mục
\renewcommand{\cfttoctitlefont}{\hfill\fontsize{14pt}{17pt}\selectfont\bfseries}
\renewcommand{\cftaftertoctitle}{\hfill}
\renewcommand{\cftlottitlefont}{\hfill\fontsize{14pt}{17pt}\selectfont\bfseries}
\renewcommand{\cftafterlottitle}{\hfill}
\renewcommand{\cftloftitlefont}{\hfill\fontsize{14pt}{17pt}\selectfont\bfseries}
\renewcommand{\cftafterloftitle}{\hfill}

% Tắt in đậm cho section trong mục lục
\renewcommand{\cftsecfont}{\normalfont}
\renewcommand{\cftsecpagefont}{\normalfont}

% Thêm nét đứt cho tiêu đề section trong mục lục
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}

% Dãn dòng giữa các section trong mục lục cho thoáng
\setlength{\cftbeforesecskip}{6pt}
