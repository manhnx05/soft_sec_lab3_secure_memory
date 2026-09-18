import os
import glob

latex_dir = r"d:\Study\SoftSec\lab2_testing_verification\latex"
chapters_dir = os.path.join(latex_dir, "Chapters")
os.makedirs(chapters_dir, exist_ok=True)
os.makedirs(os.path.join(latex_dir, "Tittle"), exist_ok=True)

for f in glob.glob(os.path.join(chapters_dir, "*.tex")):
    os.remove(f)

bia_content = r"""\begin{titlepage}
	\drawborder
	\schoolheader

	\vspace{0.2cm}
	\begin{center}
		\includegraphics[width=0.38\textwidth]{logophenikaa-uni}
	\end{center}

	\vspace{0.5cm}
	\begin{center}
		{\fontsize{24pt}{28pt}\selectfont\textbf{BÀI THỰC HÀNH 02}}\\[8pt]
		{\fontsize{15pt}{19pt}\selectfont\textbf{KIỂM THỬ VÀ KIỂM CHỨNG PHẦN MỀM:\\ HỘP ĐEN \& HỘP TRẮNG}}
	\end{center}

	\vspace{0.5cm}
	\begin{center}
		{\fontsize{14pt}{18pt}\selectfont\textbf{Hệ thống SecureSys -- Module Auth (Xác thực PIN)}}\\[8pt]
		{\fontsize{14pt}{18pt}\selectfont\textbf{Học phần CSE703093 -- An toàn phần mềm}}
	\end{center}

	\vspace{0.8cm}

	\begin{flushleft}
		\hspace{2.5cm}\begin{tabular}{@{}l @{\hspace{0.5cm}} l}
			\textbf{Sinh viên thực hiện:} & Nguyễn Xuân Mạnh \\[4pt]
			\textbf{Mã sinh viên:} & 23010102 \\[4pt]
			\textbf{Lớp:}                 & K17 -- KTPM\_EL1 \\[4pt]
			\textbf{Khoa:}                & Hệ thống thông tin \\[16pt]
			\textbf{Giảng viên hướng dẫn:}&
			\begin{tabular}[t]{@{}l}
				ThS. Vũ Quang Dũng
			\end{tabular}
		\end{tabular}
	\end{flushleft}

	\vfill
	\begin{center}
		\textbf{Hà Nội, ngày 8 tháng 7 năm 2026}
	\end{center}
\end{titlepage}
"""

main_content = r"""\documentclass{Phenikaa-report}

\begin{document}

\input{Tittle/bia} \clearpage

\pagenumbering{roman}   % La Mã cho phần đầu

\input{Chapters/00_tom_tat}
\newpage

\tableofcontents
\newpage

\pagenumbering{arabic}  % Ả Rập cho nội dung chính

\input{Chapters/01_kien_thuc_nen_tang}
\input{Chapters/02_dac_ta_ham}
\input{Chapters/03_thiet_ke_test}
\input{Chapters/04_do_do_phu_ma}
\input{Chapters/05_ket_qua_kiem_thu}
\input{Chapters/06_muc_tieu_yeu_cau}
\input{Chapters/07_cau_hoi}
\input{Chapters/08_tai_lieu_tham_khao}

\end{document}
"""

tom_tat = r"""\section*{Tóm tắt nội dung}
\addcontentsline{toc}{section}{Tóm tắt nội dung}
Bài thực hành áp dụng hai phương pháp kiểm thử kinh điển: kiểm thử hộp đen (black-box, dựa trên đặc tả) và kiểm thử hộp trắng (white-box, dựa trên cấu trúc mã nguồn) lên hàm \texttt{validate\_pin()} của module Auth. Sinh viên thiết kế test theo kỹ thuật Equivalence Partitioning và Boundary Value Analysis, sau đó đo độ phủ mã bằng \texttt{gcov} để phát hiện khoảng trống kiểm thử.
"""

c01 = r"""\section{Kiến thức nền tảng}
\begin{itemize}
    \item \textbf{Kiểm thử hộp đen:} thiết kế test chỉ dựa vào đặc tả (specification), không xem mã nguồn.
    \item \textbf{Kiểm thử hộp trắng:} thiết kế/đánh giá test dựa trên cấu trúc mã nguồn (câu lệnh, nhánh, đường đi).
    \item \textbf{Equivalence Partitioning (EP):} chia miền đầu vào thành các lớp tương đương, chỉ cần 1 đại diện mỗi lớp.
    \item \textbf{Boundary Value Analysis (BVA):} kiểm tra riêng các giá trị biên (ranh giới giữa các lớp tương đương).
\end{itemize}
"""

c02 = r"""\section{Đặc tả hàm cần kiểm thử}
Hàm \texttt{validate\_pin(pin, failed\_attempts)} (module Auth) kiểm tra mã PIN theo quy tắc:
\begin{itemize}
    \item Độ dài đúng 6 ký tự, toàn bộ là chữ số.
    \item Từ chối PIN ''yếu'' (dãy tăng/giảm liên tục, ví dụ 123456).
    \item Khóa tài khoản (\texttt{ACCOUNT\_LOCKED}) sau 3 lần nhập sai liên tiếp.
\end{itemize}
"""

c03 = r"""\section{Thiết kế test hộp đen (EP + BVA)}
\begin{table}[H]
    \centering
    \begin{tabular}{|l|l|l|l|l|}
        \hline
        \textbf{Kỹ thuật} & \textbf{PIN} & \textbf{Lần sai} & \textbf{Kỳ vọng} & \textbf{Lý do} \\ \hline
        EP-valid & 482913 & 0 & OK & PIN hợp lệ \\ \hline
        EP-invalidlength & 482 & 0 & WRONG\_LENGTH & Quá ngắn \\ \hline
        BVA-length & 48291 / 482913 / 4829137 & 0 & WRONG/OK/WRONG & Biên 5/6/7 ký tự \\ \hline
        EP-charclass & 48a913 & 0 & NON\_DIGIT & Ký tự chữ \\ \hline
        businessrule & 123456 & 0 & SEQUENTIAL\_WEAK & Dãy tăng \\ \hline
        BVA-lockout & -- & 2/3/4 & OK/LOCKED/LOCKED & Biên số lần sai \\ \hline
        specialvalue & NULL & 0 & NULL\_INPUT & Con trỏ NULL (phòng thủ) \\ \hline
    \end{tabular}
    \caption{Thiết kế test hộp đen theo EP và BVA}
\end{table}

Tổng cộng 18 test case được sinh tự động trong \texttt{python/black\_box\_tester.py}, kết quả: 18/18 PASS khi gọi qua \texttt{ctypes} vào thư viện C.
"""

c04 = r"""\section{Đo độ phủ mã hộp trắng}
Biên dịch với \texttt{gcc --coverage}, chạy driver CLI đọc trực tiếp bộ test hộp đen, sau đó phân tích báo cáo \texttt{gcov}:

\begin{table}[H]
    \centering
    \begin{tabular}{|l|l|}
        \hline
        \textbf{Chỉ số} & \textbf{Giá trị} \\ \hline
        Số dòng có thể thực thi & 66 \\ \hline
        Số dòng đã được chạy & 61 \\ \hline
        Tỷ lệ phủ (coverage) & 92.42\% \\ \hline
    \end{tabular}
    \caption{Kết quả đo độ phủ mã (Code Coverage)}
\end{table}

\textbf{Nhận xét quan trọng:} bộ test hộp đen đạt 18/18 PASS (100\%) nhưng chỉ đạt 92.42\% coverage. Các dòng chưa phủ là nhánh xử lý lỗi CLI (\texttt{argc < 2}, \texttt{fopen} thất bại) – những nhánh nằm ngoài phạm vi test hộp đen dựa trên đặc tả nghiệp vụ, đòi hỏi test riêng ở tầng tích hợp/CLI.

\begin{lstlisting}[language=C, caption={Thứ tự kiểm tra quan trọng trong validate\_pin() (trích pin\_validator.c)}]
PinResult validate_pin(const char *pin, int failed_attempts) {
    if (pin == NULL) return PIN_ERR_NULL_INPUT;
    if (failed_attempts >= 3) return PIN_ERR_ACCOUNT_LOCKED;
    size_t len = strnlen(pin, PIN_LEN + 1);
    if (len != PIN_LEN) return PIN_ERR_WRONG_LENGTH;
    /* ... */
}
\end{lstlisting}
"""

c05 = r"""\section{Kết quả kiểm thử tự động}
Script \texttt{tests/test\_pin\_validator.py} thực hiện 3 test: bộ hộp đen toàn bộ PASS, coverage đạt ngưỡng tối thiểu 90\%, và kiểm tra riêng biên khóa tài khoản.
\newline
\textbf{Kết quả:} 3/3 test PASS.
"""

c06 = r"""\section{Mục tiêu và Yêu cầu}

\subsection*{Mục tiêu học tập}
\begin{itemize}
    \item Phân biệt kiểm thử hộp đen và hộp trắng.
    \item Áp dụng Equivalence Partitioning và Boundary Value Analysis.
    \item Đo và diễn giải độ phủ mã bằng \texttt{gcov}.
    \item Gọi hàm C từ Python bằng \texttt{ctypes}.
\end{itemize}

\subsection*{Yêu cầu hoàn thiện}
\begin{enumerate}
    \item Bảng thiết kế test tự làm (EP + BVA) trước khi xem code mẫu.
    \item Log chạy 18/18 PASS và báo cáo coverage.
    \item Diff bổ sung $\ge$ 2 test case tăng coverage.
    \item Trả lời câu hỏi về thứ tự kiểm tra \texttt{failed\_attempts}.
\end{enumerate}

\subsection*{Yêu cầu kết quả}
Script \texttt{tests/test\_pin\_validator.py} toàn bộ PASS, bao gồm ngưỡng coverage tối thiểu 90\%.
"""

c07 = r"""\section{Câu hỏi thảo luận}
\textbf{Câu hỏi:} Nếu đảo thứ tự kiểm tra \texttt{failed\_attempts >= 3} xuống sau kiểm tra độ dài PIN, hệ thống có còn an toàn không? Minh họa bằng một test case cụ thể.
\vspace{0.5cm}
\newline
\textbf{Trả lời:} Không an toàn. Nếu đảo ngược kiểm tra, kẻ tấn công có thể thăm dò độ dài mã PIN ngay cả khi tài khoản đã bị khóa. Ví dụ test case: \texttt{pin = "482", failed\_attempts = 4}. Kỳ vọng đúng là \texttt{ACCOUNT\_LOCKED} nhưng thực tế hệ thống sẽ trả về \texttt{WRONG\_LENGTH}, làm rò rỉ thông tin về chính sách xác thực và vô hiệu hóa một phần tính năng khóa tài khoản.
"""

c08 = r"""\section{Tài liệu tham khảo}
\begin{itemize}
    \item Đề cương CSE703093 – An toàn phần mềm, Chương 1 (1.3, 1.4).
    \item ISTQB Foundation Level Syllabus.
\end{itemize}
"""

files = {
    "Tittle/bia.tex": bia_content,
    "main.tex": main_content,
    "Chapters/00_tom_tat.tex": tom_tat,
    "Chapters/01_kien_thuc_nen_tang.tex": c01,
    "Chapters/02_dac_ta_ham.tex": c02,
    "Chapters/03_thiet_ke_test.tex": c03,
    "Chapters/04_do_do_phu_ma.tex": c04,
    "Chapters/05_ket_qua_kiem_thu.tex": c05,
    "Chapters/06_muc_tieu_yeu_cau.tex": c06,
    "Chapters/07_cau_hoi.tex": c07,
    "Chapters/08_tai_lieu_tham_khao.tex": c08,
}

for rel_path, content in files.items():
    full_path = os.path.join(latex_dir, rel_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
