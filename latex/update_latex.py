import os

latex_dir = r"d:\Study\SoftSec\lab2_testing_verification\latex"

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

Tổng cộng 18 test case được sinh tự động trong \texttt{python/black\_box\_tester.py}.

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
    \caption{Hình ảnh terminal khi chạy kiểm thử hộp đen}
\end{figure}

Kết quả đạt 18/18 PASS khi gọi qua \texttt{ctypes} vào thư viện C.
"""

c04 = r"""\section{Đo độ phủ mã hộp trắng}
Biên dịch với \texttt{gcc --coverage}, chạy driver CLI đọc trực tiếp bộ test hộp đen, sau đó phân tích báo cáo \texttt{gcov}.

Lệnh thực thi đo độ phủ mã:
\begin{lstlisting}[language=bash]
> python python/white_box_coverage.py
\end{lstlisting}

Kết quả log đo độ phủ mã (sau khi đã bổ sung test case hộp trắng):
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
    \caption{Hình ảnh terminal kết quả đo độ phủ mã gcov}
\end{figure}

\begin{table}[H]
    \centering
    \begin{tabular}{|l|l|}
        \hline
        \textbf{Chỉ số} & \textbf{Giá trị} \\ \hline
        Số dòng có thể thực thi & 66 \\ \hline
        Số dòng đã được chạy & 65 \\ \hline
        Tỷ lệ phủ (coverage) & 98.48\% \\ \hline
    \end{tabular}
    \caption{Kết quả đo độ phủ mã (Code Coverage)}
\end{table}

\textbf{Nhận xét quan trọng:} bộ test hộp đen ban đầu chỉ đạt 92.42\% coverage do thiếu các trường hợp xử lý lỗi CLI. Sau khi bổ sung thêm 2 lệnh gọi CLI (thiếu tham số và sai tên file) trực tiếp trong script, coverage đã tăng lên \textbf{98.48\%}. Dòng mã duy nhất không thể phủ tới là nhánh \texttt{default} mang tính chất phòng thủ trong \texttt{switch case}.

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
    \caption{Hình ảnh terminal kết quả kiểm thử tự động}
\end{figure}

\textbf{Kết luận:} 3/3 bài test đã PASS thành công, thỏa mãn mọi yêu cầu của Lab.
"""

files = {
    "Chapters/03_thiet_ke_test.tex": c03,
    "Chapters/04_do_do_phu_ma.tex": c04,
    "Chapters/05_ket_qua_kiem_thu.tex": c05,
}

for rel_path, content in files.items():
    full_path = os.path.join(latex_dir, rel_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
