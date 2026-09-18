import os
import glob

latex_dir = r"d:\Study\SoftSec\lab2_testing_verification\latex"
chapters_dir = os.path.join(latex_dir, "Chapters")
os.makedirs(chapters_dir, exist_ok=True)

# Xoá các file tex hiện tại trong Chapters
for f in glob.glob(os.path.join(chapters_dir, "*.tex")):
    os.remove(f)

# Cấu trúc main.tex mới
main_content = r"""\documentclass{Phenikaa-report}

\begin{document}

\input{Tittle/bia} \clearpage

\pagenumbering{roman}   % La Mã cho phần đầu
\input{Chapters/00_tom_tat}
\newpage
\tableofcontents
\newpage

\pagenumbering{arabic}  % Ả Rập cho nội dung chính
\input{Chapters/01_gioi_thieu}
\input{Chapters/02_kien_thuc_nen_tang}
\input{Chapters/03_dac_ta_he_thong}
\input{Chapters/04_kiem_thu_hop_den}
\input{Chapters/05_kiem_thu_hop_trang}
\input{Chapters/06_kiem_thu_tu_dong}
\input{Chapters/07_thao_luan}
\input{Chapters/08_tai_lieu_tham_khao}

\end{document}
"""
with open(os.path.join(latex_dir, "main.tex"), "w", encoding="utf-8") as f:
    f.write(main_content)

# 00_tom_tat.tex
c00 = r"""\section*{Tóm tắt nội dung}
\addcontentsline{toc}{section}{Tóm tắt nội dung}
Báo cáo này trình bày kết quả thực hiện Bài thực hành 02 thuộc học phần An toàn phần mềm. Trọng tâm của bài thực hành là áp dụng các kỹ thuật kiểm thử phần mềm kinh điển bao gồm kiểm thử hộp đen (black-box testing) dựa trên đặc tả và kiểm thử hộp trắng (white-box testing) dựa trên cấu trúc mã nguồn. Đối tượng kiểm thử là hàm \texttt{validate\_pin()} thuộc Module Auth của hệ thống SecureSys.

Thông qua việc vận dụng các kỹ thuật Phân vùng tương đương (Equivalence Partitioning) và Phân tích giá trị biên (Boundary Value Analysis), một bộ test case hộp đen hoàn chỉnh đã được xây dựng và thực thi tự động qua \texttt{ctypes}. Tiếp đó, công cụ \texttt{gcov} được sử dụng để phân tích độ phủ mã (code coverage), từ đó phát hiện các nhánh mã chưa được kiểm thử và tiến hành bổ sung test case hộp trắng nhằm nâng cao độ phủ lên mức tối đa (98.48\%). Báo cáo cũng thảo luận về khía cạnh an toàn bảo mật liên quan đến thứ tự kiểm tra các luồng điều kiện trong mã nguồn.
"""

# 01_gioi_thieu.tex
c01 = r"""\section{Giới thiệu}
\subsection{Mục tiêu học tập}
Quá trình thực hành hướng tới việc giúp sinh viên đạt được các mục tiêu sau:
\begin{itemize}
    \item Phân biệt rõ ràng giữa kiểm thử hộp đen (dựa trên đặc tả, không can thiệp mã nguồn) và kiểm thử hộp trắng (dựa trên luồng thực thi của mã nguồn).
    \item Áp dụng thành thạo hai kỹ thuật thiết kế test kinh điển: Equivalence Partitioning (EP) và Boundary Value Analysis (BVA).
    \item Biết cách sử dụng công cụ \texttt{gcov} để đo độ phủ mã (code coverage) trong ngôn ngữ C và diễn giải ý nghĩa của các dòng lệnh ''chưa được kiểm thử''.
    \item Nắm vững kỹ thuật gọi hàm thư viện C từ Python thông qua \texttt{ctypes} để xây dựng công cụ kiểm thử tự động đa ngôn ngữ.
    \item Hiểu được nguyên lý quan trọng trong kiểm thử bảo mật: Việc đạt 100\% test PASS ở kiểm thử hộp đen không đồng nghĩa với việc mã nguồn đã được bao phủ 100\% (luôn tiềm ẩn các đoạn mã chết hoặc rẽ nhánh lỗi chưa được kiểm tra).
\end{itemize}

\subsection{Yêu cầu hoàn thiện của bài lab}
Theo tài liệu hướng dẫn, bài thực hành yêu cầu sinh viên hoàn thành các nội dung (Deliverables) sau:
\begin{enumerate}
    \item Lập bảng thiết kế test tự làm (áp dụng EP và BVA).
    \item Thực thi và nộp log chạy \texttt{black\_box\_tester.py} (18/18 PASS) cùng \texttt{white\_box\_coverage.py} (báo cáo \% coverage ban đầu và danh sách các dòng chưa phủ).
    \item Cung cấp đoạn mã bổ sung (Diff code) cho ít nhất 2 test case mới nhằm tăng độ phủ mã, kèm theo log kết quả coverage mới.
    \item Trả lời câu hỏi phân tích bảo mật: Hệ thống có còn an toàn không nếu đảo thứ tự kiểm tra \texttt{failed\_attempts >= 3} xuống sau kiểm tra độ dài PIN.
\end{enumerate}
"""

# 02_kien_thuc_nen_tang.tex
c02 = r"""\section{Kiến thức nền tảng}
\subsection{Kiểm thử hộp đen và Hộp trắng}
\begin{itemize}
    \item \textbf{Kiểm thử hộp đen (Black-box Testing):} Là phương pháp kiểm thử dựa hoàn toàn vào yêu cầu và đặc tả (specification) của phần mềm. Người kiểm thử không cần biết cấu trúc bên trong hay mã nguồn của chương trình, chỉ quan tâm đến đầu vào (Input) và đầu ra (Output).
    \item \textbf{Kiểm thử hộp trắng (White-box Testing):} Trái ngược với hộp đen, phương pháp này đòi hỏi người kiểm thử phải am hiểu mã nguồn. Việc thiết kế test case dựa trên việc duyệt qua các câu lệnh, các nhánh điều kiện (if/else, switch) và các luồng dữ liệu bên trong để đảm bảo mọi đoạn code đều được thực thi ít nhất một lần.
\end{itemize}

\subsection{Kỹ thuật thiết kế Test Case}
Dựa trên tiêu chuẩn ISTQB, hai kỹ thuật phổ biến nhất được sử dụng trong bài là:
\begin{itemize}
    \item \textbf{Equivalence Partitioning (EP - Phân vùng tương đương):} Chia miền đầu vào thành các lớp tương đương sao cho hành vi của phần mềm đối với mọi giá trị trong cùng một lớp là như nhau. Ta chỉ cần chọn một giá trị đại diện cho mỗi lớp để kiểm thử, giúp giảm thiểu số lượng test case mà vẫn đảm bảo tính toàn vẹn.
    \item \textbf{Boundary Value Analysis (BVA - Phân tích giá trị biên):} Bổ trợ cho kỹ thuật EP, BVA tập trung vào việc kiểm thử tại các giá trị ranh giới (biên) của các phân vùng tương đương. Đây là nơi thường xuyên xảy ra lỗi lập trình nhất (ví dụ: lỗi off-by-one như dùng \texttt{<} thay vì \texttt{<=}).
\end{itemize}
"""

# 03_dac_ta_he_thong.tex
c03 = r"""\section{Đặc tả hệ thống (Module Auth)}
Bài toán yêu cầu kiểm thử hàm xác thực \texttt{validate\_pin(const char *pin, int failed\_attempts)}. Đây là một module cốt lõi trong hệ thống SecureSys. Hàm nhận vào chuỗi mã PIN do người dùng nhập và số lần đã nhập sai trước đó.

Quy tắc nghiệp vụ (Business Rules) được đặc tả như sau:
\begin{enumerate}
    \item \textbf{Khóa tài khoản:} Nếu số lần nhập sai (\texttt{failed\_attempts}) đạt từ 3 lần trở lên, tài khoản sẽ bị khóa. Trả về lỗi \textbf{ACCOUNT\_LOCKED}.
    \item \textbf{Kiểm tra độ dài:} Mã PIN hợp lệ phải có độ dài chính xác là 6 ký tự. Nếu sai, trả về lỗi \textbf{WRONG\_LENGTH}.
    \item \textbf{Kiểm tra định dạng:} Toàn bộ 6 ký tự phải là chữ số (từ '0' đến '9'). Nếu chứa ký tự chữ, khoảng trắng hoặc ký tự đặc biệt, trả về lỗi \textbf{NON\_DIGIT}.
    \item \textbf{Chính sách mật khẩu yếu:} Từ chối các mã PIN là dãy số tăng hoặc giảm liên tiếp (ví dụ: 123456, 654321). Trả về lỗi \textbf{SEQUENTIAL\_WEAK}.
    \item \textbf{Xử lý ngoại lệ:} Đầu vào \texttt{NULL} phải được phòng thủ, trả về lỗi \textbf{NULL\_INPUT}.
\end{enumerate}

Nếu vượt qua toàn bộ các lớp kiểm tra trên, hàm trả về kết quả \textbf{OK}.
"""

# 04_kiem_thu_hop_den.tex
c04 = r"""\section{Kiểm thử Hộp đen (Black-box Testing)}

\subsection{Thiết kế Test Case (áp dụng EP và BVA)}
Dựa vào đặc tả hệ thống tại phần trước, bảng thiết kế test case được xây dựng như sau:

\begin{table}[H]
    \centering
\begin{tabularx}{\textwidth}{|p{2.6cm}|p{2cm}|c|p{3.4cm}|X|}
        \hline
        \textbf{Kỹ thuật} & \textbf{Mã PIN} & \textbf{Lần sai} & \textbf{Kỳ vọng (Expected)} & \textbf{Lý do / Mục đích} \\ \hline
        \multicolumn{5}{|c|}{\textbf{Lớp tương đương (EP)}} \\ \hline
        EP-valid & 482913 & 0 & OK & PIN hợp lệ hoàn toàn \\ \hline
        EP-invalid-length & 482 \newline 48291378 \newline (chuỗi rỗng) & 0 & WRONG\_LENGTH & Quá ngắn, quá dài hoặc không nhập gì \\ \hline
        EP-invalid-char & 48a913 \newline 48 913 \newline -89213 & 0 & NON\_DIGIT & Chứa ký tự chữ, khoảng trắng, ký hiệu âm \\ \hline
        Business-rule & 123456 \newline 654321 & 0 & SEQUENTIAL\_WEAK & Dãy số tiến, dãy số lùi liên tiếp \\ \hline
        \multicolumn{5}{|c|}{\textbf{Phân tích giá trị biên (BVA)}} \\ \hline
        BVA-length & 48291 (5) \newline 482913 (6) \newline 4829137 (7) & 0 & WRONG\_LENGTH \newline OK \newline WRONG\_LENGTH & Biên dưới (thiếu 1), chính xác tại biên, biên trên (thừa 1) \\ \hline
        BVA-lockout & 482913 & 2 \newline 3 \newline 4 & OK \newline ACCOUNT\_LOCKED \newline ACCOUNT\_LOCKED & Biên dưới chưa khóa (2), ngay tại ngưỡng khóa (3), vượt ngưỡng khóa (4) \\ \hline
        \multicolumn{5}{|c|}{\textbf{Trường hợp ngoại lệ (Special Value)}} \\ \hline
        Defensive & NULL & 0 & NULL\_INPUT & Truyền con trỏ NULL để kiểm tra tính phòng thủ \\ \hline
    \end{tabularx}
    \caption{Bảng thiết kế test case hộp đen theo phương pháp EP và BVA}
\end{table}

\subsection{Thực thi kiểm thử tự động}
Tổng cộng 18 test case ở trên được lập trình tự động trong script \texttt{python/black\_box\_tester.py}. Script này sẽ biên dịch mã C thành thư viện dùng chung (\texttt{.so}) và sử dụng \texttt{ctypes} để truyền tham số vào hàm \texttt{validate\_pin}.

Lệnh chạy kiểm thử hộp đen:
\begin{lstlisting}[language=bash]
> python python/black_box_tester.py
\end{lstlisting}

Kết quả log kiểm thử:
\begin{lstlisting}[language=bash]
[PASS] (EP-valid              ) pin=482913   failed=0 expected=OK               actual=OK
[PASS] (EP-valid              ) pin=739284   failed=1 expected=OK               actual=OK
[PASS] (EP-invalid-length     ) pin=482      failed=0 expected=WRONG_LENGTH     actual=WRONG_LENGTH
[PASS] (EP-invalid-length     ) pin=48291378 failed=0 expected=WRONG_LENGTH     actual=WRONG_LENGTH
[PASS] (EP-invalid-length     ) pin=         failed=0 expected=WRONG_LENGTH     actual=WRONG_LENGTH
[PASS] (BVA-length-boundary   ) pin=48291    failed=0 expected=WRONG_LENGTH     actual=WRONG_LENGTH
[PASS] (BVA-length-boundary   ) pin=482913   failed=0 expected=OK               actual=OK
[PASS] (BVA-length-boundary   ) pin=4829137  failed=0 expected=WRONG_LENGTH     actual=WRONG_LENGTH
[PASS] (EP-invalid-charclass  ) pin=48a913   failed=0 expected=NON_DIGIT        actual=NON_DIGIT
[PASS] (EP-invalid-charclass  ) pin=48 913   failed=0 expected=NON_DIGIT        actual=NON_DIGIT
[PASS] (EP-invalid-charclass  ) pin=-89213   failed=0 expected=NON_DIGIT        actual=NON_DIGIT
[PASS] (business-rule         ) pin=123456   failed=0 expected=SEQUENTIAL_WEAK  actual=SEQUENTIAL_WEAK
[PASS] (business-rule         ) pin=654321   failed=0 expected=SEQUENTIAL_WEAK  actual=SEQUENTIAL_WEAK
[PASS] (business-rule         ) pin=112233   failed=0 expected=OK               actual=OK
[PASS] (BVA-lockout-boundary  ) pin=482913   failed=2 expected=OK               actual=OK
[PASS] (BVA-lockout-boundary  ) pin=482913   failed=3 expected=ACCOUNT_LOCKED   actual=ACCOUNT_LOCKED
[PASS] (BVA-lockout-boundary  ) pin=482913   failed=4 expected=ACCOUNT_LOCKED   actual=ACCOUNT_LOCKED
[PASS] (special-value         ) pin=NULL     failed=0 expected=NULL_INPUT       actual=NULL_INPUT

Tong: 18/18 test PASS
Ket qua da luu: D:\Study\SoftSec\lab2_testing_verification\dataset\black_box_test_results.csv
\end{lstlisting}

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{Images/log_black_box.png}
    \caption{Hình ảnh thực thi script kiểm thử hộp đen}
\end{figure}

\textbf{Nhận xét:} Bộ test case đã bao phủ toàn bộ các kịch bản của đặc tả. 18/18 test case đều \textbf{PASS}, khẳng định module Auth hoạt động đúng đắn theo yêu cầu nghiệp vụ.
"""

# 05_kiem_thu_hop_trang.tex
c05 = r"""\section{Kiểm thử Hộp trắng và Đo độ phủ mã (Code Coverage)}
Dù kiểm thử hộp đen đạt 100\% thành công, ta vẫn cần phân tích hộp trắng thông qua công cụ \texttt{gcov} để xác minh xem có dòng mã nào trong source code C chưa được thực thi qua hay không.

\subsection{Độ phủ ban đầu khi chỉ dùng Test Case Hộp đen}
Khi chạy script \texttt{white\_box\_coverage.py} lần đầu với bộ 18 test case hộp đen, kết quả thu được là:

\begin{lstlisting}[language=bash]
=== KET QUA DO PHU MA (Statement Coverage qua gcov) ===
So dong co the thuc thi : 66
So dong da duoc chay    : 61
Ty le phu (coverage)    : 92.42%

Cac dong CHUA duoc kiem thu (can bo sung test case hop trang):
  Dong 84: default: return "UNKNOWN";
  Dong 93: fprintf(stderr, "Cach dung: %s <test_cases.csv>\n", argv[0]);
  Dong 94: return 1;
  Dong 98: fprintf(stderr, "[LOI] Khong mo duoc file: %s\n", argv[1]);
  Dong 99: return 1;
\end{lstlisting}

\textbf{Phân tích nguyên nhân:} Coverage chỉ đạt 92.42\% dù test hộp đen đã PASS 100\% vì tập test hộp đen chỉ tập trung vào logic nghiệp vụ của hàm \texttt{validate\_pin}. Trong khi đó, file \texttt{pin\_validator.c} còn chứa hàm \texttt{main} dùng làm CLI. Các dòng chưa phủ là các rẽ nhánh báo lỗi cấu hình CLI (chạy không truyền tham số, hoặc truyền sai tên file CSV). Các rẽ nhánh lỗi hạ tầng này không bao giờ được chạm tới khi ta chạy test case hợp lệ.

\subsection{Bổ sung Test Case Hộp trắng để tăng độ phủ}
Để khắc phục điểm mù này, cần chủ động thiết kế thêm 2 test case nhắm thẳng vào các điều kiện rẽ nhánh lỗi trong CLI. Thay vì thêm vào hàm sinh test nghiệp vụ, ta bổ sung lệnh thực thi trực tiếp tiến trình CLI với các tham số cố tình gây lỗi.

\textbf{Diff code bổ sung vào file \texttt{python/white\_box\_coverage.py}:}
\begin{lstlisting}[language=Python]
@@ -97,6 +97,13 @@
     output = run_cli_with_dataset(tmp_csv)
     print(output)
 
+    # --- BO SUNG TEST CASE HOP TRANG ---
+    # 1. Goi CLI thieu tham so (de phu nhanh argc < 2)
+    subprocess.run([os.path.join(C_DIR, "pin_validator_cli")], cwd=C_DIR, capture_output=True)
+    # 2. Goi CLI voi file khong ton tai (de phu nhanh !fp)
+    subprocess.run([os.path.join(C_DIR, "pin_validator_cli"), "non_existent_file.csv"], cwd=C_DIR, capture_output=True)
+    # -----------------------------------
+
     cov = compute_branch_coverage()
     print("=== KET QUA DO PHU MA (Statement Coverage qua gcov) ===")
     print(f"So dong co the thuc thi : {cov['lines_total']}")
\end{lstlisting}

\subsection{Kết quả độ phủ mã sau tối ưu}
Sau khi đưa thêm hai rẽ nhánh thử nghiệm lỗi CLI, ta chạy lại script để đo lường.

Lệnh thực thi đo độ phủ mã:
\begin{lstlisting}[language=bash]
> python python/white_box_coverage.py
\end{lstlisting}

Kết quả log:
\begin{lstlisting}[language=bash]
=== KET QUA DO PHU MA (Statement Coverage qua gcov) ===
So dong co the thuc thi : 66
So dong da duoc chay    : 65
Ty le phu (coverage)    : 98.48%

Cac dong CHUA duoc kiem thu (can bo sung test case hop trang):
  Dong 84: default: return "UNKNOWN";
\end{lstlisting}

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{Images/log_white_box.png}
    \caption{Hình ảnh kết quả đo độ phủ mã gcov sau tối ưu}
\end{figure}

\textbf{Nhận xét quan trọng:} Độ phủ mã đã tăng thành công từ 92.42\% lên \textbf{98.48\%}. Dòng mã duy nhất (dòng 84) không thể bao phủ là nhánh \texttt{default} trong khối \texttt{switch case}. Đây là đoạn mã phòng thủ (Defensive Programming), thực tế không bao giờ được gọi đến thông qua CLI bởi hàm \texttt{validate\_pin} chỉ trả về 6 giá trị Enum đã biết trước. Mức 98.48\% được xem là hoàn hảo đối với mã nguồn này.
"""

# 06_kiem_thu_tu_dong.tex
c06 = r"""\section{Tổng hợp Kết quả Kiểm thử Tự động}
Dự án cung cấp một script Python thực hiện kiểm chứng tổng thể (Continuous Testing) để đảm bảo không có bài test nào bị vỡ (regression). Script \texttt{tests/test\_pin\_validator.py} tiến hành gọi tự động và chấm điểm cho 3 mục tiêu: (1) Bộ hộp đen toàn bộ PASS, (2) Coverage phải lớn hơn mức sàn 90\%, (3) Biên khóa tài khoản hoạt động bình thường.

Lệnh chạy kiểm thử tự động:
\begin{lstlisting}[language=bash]
> python tests/test_pin_validator.py
\end{lstlisting}

Kết quả log:
\begin{lstlisting}[language=bash]
[PASS] test_black_box_suite_all_pass
[PASS] test_white_box_coverage_meets_threshold
[PASS] test_account_lockout_boundary

3/3 test da PASS
\end{lstlisting}

\begin{figure}[H]
    \centering
    \includegraphics[width=\textwidth]{Images/log_auto_test.png}
    \caption{Kết quả chạy bộ kiểm thử tự động hoàn chỉnh}
\end{figure}

\textbf{Kết luận:} 3/3 bài test tự động đã PASS thành công, đánh dấu việc hoàn thiện trọn vẹn toàn bộ các mục tiêu đặt ra của bài Lab.
"""

# 07_thao_luan.tex
c07 = r"""\section{Thảo luận vấn đề bảo mật}

\subsection{Câu hỏi phân tích}
Nếu lập trình viên vô tình \textbf{đảo thứ tự kiểm tra} trong hàm \texttt{validate\_pin}: đưa khối mã kiểm tra \texttt{failed\_attempts >= 3} xuống \textbf{sau} khối kiểm tra độ dài PIN (nhánh rẽ \texttt{WRONG\_LENGTH}), thì hệ thống có còn an toàn không?

\begin{lstlisting}[language=C, caption={Minh họa đoạn mã sai lệch thứ tự kiểm tra}]
PinResult validate_pin(const char *pin, int failed_attempts) {
    if (pin == NULL) return PIN_ERR_NULL_INPUT;
    
    /* SAI LAM: Kiem tra cau truc truoc khi kiem tra trang thai khoa */
    size_t len = strnlen(pin, PIN_LEN + 1);
    if (len != PIN_LEN) return PIN_ERR_WRONG_LENGTH;
    
    if (failed_attempts >= 3) return PIN_ERR_ACCOUNT_LOCKED;
    /* ... */
}
\end{lstlisting}

\subsection{Trả lời và Chứng minh}
Hệ thống \textbf{HOÀN TOÀN KHÔNG AN TOÀN}. Nếu đảo ngược trình tự như trên, module Auth đã vi phạm nguyên tắc bảo mật cơ bản: Một tài khoản bị khóa phải ngay lập tức bị từ chối phục vụ mọi loại yêu cầu (từ chối phân tích Payload).

\textbf{Minh họa bằng Test Case cụ thể:}
\begin{itemize}
    \item \textbf{Input:} Gửi mã \texttt{pin = "482"} (sai độ dài, chỉ có 3 số) và \texttt{failed\_attempts = 4} (tài khoản đáng lẽ đã bị khóa).
    \item \textbf{Kỳ vọng an toàn (Expected):} Hệ thống phải lập tức trả về \textbf{ACCOUNT\_LOCKED} và không xử lý gì thêm.
    \item \textbf{Hành vi thực tế (Actual):} Hệ thống sẽ nhận diện độ dài sai trước và thoát ra bằng lỗi \textbf{WRONG\_LENGTH}. Tính năng khóa tài khoản hoàn toàn bị qua mặt.
\end{itemize}

\textbf{Lỗ hổng bảo mật sinh ra:}
Kẻ tấn công có thể lợi dụng lỗi rò rỉ thông tin (Information Leakage) này để thăm dò đặc tả của hệ thống (ví dụ dò tìm xem hệ thống yêu cầu độ dài mật khẩu là bao nhiêu) ngay cả khi tài khoản của chúng đã bị liệt vào danh sách khóa. Hơn thế nữa, việc máy chủ tiếp tục tính toán, xử lý độ dài chuỗi từ một nguồn tin cậy bị khóa có thể dẫn đến rủi ro tràn bộ đệm (Buffer Overflow) hoặc tiêu tốn tài nguyên (DoS) nếu chuỗi đầu vào độc hại đủ lớn.
"""

# 08_tai_lieu_tham_khao.tex
c08 = r"""\section{Tài liệu tham khảo}
\begin{itemize}
    \item Đề cương CSE703093 – An toàn phần mềm, Chương 1 (1.3, 1.4).
    \item ISTQB Foundation Level Syllabus - Các kỹ thuật thiết kế test case (EP, BVA).
    \item Tài liệu hướng dẫn sử dụng \texttt{gcov} - GNU Compiler Collection (GCC).
\end{itemize}
"""

files = {
    "Chapters/00_tom_tat.tex": c00,
    "Chapters/01_gioi_thieu.tex": c01,
    "Chapters/02_kien_thuc_nen_tang.tex": c02,
    "Chapters/03_dac_ta_he_thong.tex": c03,
    "Chapters/04_kiem_thu_hop_den.tex": c04,
    "Chapters/05_kiem_thu_hop_trang.tex": c05,
    "Chapters/06_kiem_thu_tu_dong.tex": c06,
    "Chapters/07_thao_luan.tex": c07,
    "Chapters/08_tai_lieu_tham_khao.tex": c08,
}

for rel_path, content in files.items():
    full_path = os.path.join(latex_dir, rel_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.replace(r"\textbf{", r"\textit{").strip() + "\n")
