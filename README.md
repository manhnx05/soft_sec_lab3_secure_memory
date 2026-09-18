# Lab 3 — Lập trình C An toàn: Quản lý Bộ nhớ & Đánh giá Rủi ro

**Chủ đề xuyên suốt:** SecureSys – Hệ thống Quản lý Truy cập và Giao dịch An toàn  
**Module con:** Inventory (Quản lý kho sách thư viện)  
**Ánh xạ đề cương:** Chương 2 — 2.1 Đánh giá rủi ro, 2.3 Lập trình C an toàn (Quản lý bộ nhớ)

---

## 1. Mục tiêu học tập

- Nhận diện và tái hiện 3 lớp lỗi bộ nhớ phổ biến trong C: **Buffer Overflow (CWE-121)**, **Use-After-Free (CWE-416)**, **Memory Leak (CWE-401)**.
- Sử dụng **AddressSanitizer (ASan)** để phát hiện lỗi bộ nhớ tại runtime.
- Sửa lỗi theo các nguyên tắc lập trình C an toàn: `snprintf` thay `strcpy`, đặt con trỏ `NULL` sau `free`, đảm bảo mọi `malloc` có `free` tương ứng.
- Áp dụng **mô hình đánh giá rủi ro** đơn giản hóa theo tinh thần CVSS để định lượng và xếp hạng mức độ nghiêm trọng.
- Hiểu rõ **giới hạn của ASan**: vì sao lỗi tràn bộ đệm bên trong một struct có thể không bị phát hiện.

---

## 2. Yêu cầu môi trường

| Thành phần | Phiên bản kiểm tra | Ghi chú |
|---|---|---|
| GCC | 16.x (MSYS2) | Cần có `-fsanitize=address` support |
| Python | 3.13+ | Dùng venv trong `.venv\` |
| Make | GNU Make (MSYS2) | Tuỳ chọn, có thể chạy lệnh thủ công |
| OS | Windows 10/11 + MSYS2 | Hoặc WSL2 Ubuntu |

> **Lưu ý Windows:** AddressSanitizer trên Windows yêu cầu GCC từ MSYS2/MinGW-w64.  
> LeakSanitizer (`detect_leaks=1`) chỉ hoạt động đầy đủ trên Linux/WSL2.  
> Trên Windows native, test leak có thể không báo lỗi — kết quả chuẩn lấy từ WSL2.

---

## 3. Cấu trúc thư mục

```
lab3_secure_memory\
├── c\
│   ├── vulnerable_inventory.c      # Mã nguồn có 3 lỗi cố ý
│   ├── secure_inventory.c          # Bản đã sửa
│   ├── vulnerable_inventory_noasan.exe  # Binary không có ASan (demo)
│   └── secure_inventory_noasan.exe
├── dataset\
│   ├── vulnerabilities.json             # Dataset 5 lỗ hổng + thuộc tính CVSS-lite
│   ├── risk_assessment_results.json     # Kết quả tính toán
│   └── expected_risk_baseline.json      # Baseline để kiểm thử
├── python\
│   └── risk_assessor.py            # Script đánh giá rủi ro
├── tests\
│   └── test_memory_safety.py       # Bộ kiểm thử tự động (8 test)
├── latex\                          # Báo cáo LaTeX
├── Makefile
└── README.md
```

---

## 4. Các bước thực hành

### Bước 1 — Thiết lập môi trường Python

```powershell
# Tạo virtual environment (chỉ làm 1 lần)
python -m venv .venv

# Kích hoạt venv
.\.venv\Scripts\Activate.ps1

# Cài đặt dependencies (nếu có requirements.txt)
# pip install -r requirements.txt
```

### Bước 2 — Biên dịch hai binary với AddressSanitizer

**Dùng Make (MSYS2 shell):**
```bash
make all
```

**Hoặc chạy thủ công trong PowerShell:**
```powershell
gcc -g -Wall -Wextra -fsanitize=address -o c\vulnerable_inventory c\vulnerable_inventory.c
gcc -g -Wall -Wextra -fsanitize=address -o c\secure_inventory    c\secure_inventory.c
```

### Bước 3 — Tái hiện từng lỗi trên bản vulnerable

**CWE-121: Heap Buffer Overflow**
```powershell
.\c\vulnerable_inventory.exe overflow "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
# Hoặc nếu binary không có .exe extension (MSYS2):
# ./c/vulnerable_inventory overflow "AAAA..."
```

**CWE-416: Use-After-Free**
```powershell
.\c\vulnerable_inventory.exe uaf
```

**CWE-401: Memory Leak** (cần WSL2 để LeakSanitizer hoạt động)
```powershell
# Trên WSL2 / Linux:
$env:ASAN_OPTIONS = "detect_leaks=1"
.\c\vulnerable_inventory leak
```

```bash
# Trên WSL2/Linux (khuyến nghị cho kịch bản leak):
ASAN_OPTIONS=detect_leaks=1 ./c/vulnerable_inventory leak
```

### Bước 4 — Xác nhận bản secure sạch lỗi

```powershell
.\c\secure_inventory.exe overflow "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
.\c\secure_inventory.exe uaf
# Cả hai phải kết thúc bình thường, không có ERROR trong output
```

### Bước 5 — Chạy đánh giá rủi ro

```powershell
# Kích hoạt venv nếu chưa kích hoạt
.\.venv\Scripts\Activate.ps1

python python\risk_assessor.py
# Kết quả lưu tại: dataset\risk_assessment_results.json
```

**Hoặc dùng Make:**
```bash
make risk-report
```

### Bước 6 — Chạy bộ kiểm thử tự động

```powershell
# Kích hoạt venv
.\.venv\Scripts\Activate.ps1

python tests\test_memory_safety.py
```

**Hoặc dùng Make (MSYS2 shell):**
```bash
make test
```

**Kết quả mong đợi:**
```
[PASS] test_vulnerable_overflow_detected
[PASS] test_vulnerable_uaf_detected
[PASS] test_vulnerable_leak_detected
[PASS] test_secure_overflow_clean
[PASS] test_secure_uaf_clean
[PASS] test_secure_leak_clean
[PASS] test_risk_assessment_matches_baseline
[PASS] test_critical_vuln_is_the_buffer_overflow

8/8 test da PASS
```

---

## 5. Sơ đồ luồng dữ liệu

```
c\vulnerable_inventory.c  --gcc -fsanitize=address-->  Binary có ASan
         |                                                    |
         | (chạy 3 kịch bản: overflow / uaf / leak)          v
         |                                       Báo cáo lỗi runtime (ASan)
         v
dataset\vulnerabilities.json  (mô tả CWE + thuộc tính CVSS-lite)
         |
         v
python\risk_assessor.py  (tính Exploitability + Impact subscore)
         |
         v
dataset\risk_assessment_results.json  <--so sánh-->  dataset\expected_risk_baseline.json
         |
         v
tests\test_memory_safety.py  (đối chiếu tự động ASan + điểm rủi ro)
```

---

## 6. Tóm tắt kết quả rủi ro

| ID | CWE | Tên lỗ hổng | Điểm | Mức độ |
|---|---|---|---|---|
| VULN-001 | CWE-121 | Buffer Overflow | 9.8 | CRITICAL |
| VULN-005 | CWE-134 | Format String Bug | 9.8 | CRITICAL |
| VULN-002 | CWE-416 | Use-After-Free | 6.9 | MEDIUM |
| VULN-003 | CWE-401 | Memory Leak | 5.4 | MEDIUM |
| VULN-004 | CWE-476 | NULL Pointer Dereference | 2.5 | LOW |

Thứ tự ưu tiên khắc phục: **VULN-001 → VULN-005 → VULN-002 → VULN-003 → VULN-004**

---

## 7. Dọn dẹp

```powershell
# Xoá binary đã biên dịch (PowerShell)
Remove-Item c\vulnerable_inventory, c\secure_inventory -ErrorAction SilentlyContinue

# Hoặc dùng Make (MSYS2):
# make clean
```

---

## 8. Tài liệu tham khảo

- Đề cương CSE703093 — An toàn phần mềm, Chương 2 (2.1, 2.3).
- MITRE, [CWE-121](https://cwe.mitre.org/data/definitions/121.html), [CWE-416](https://cwe.mitre.org/data/definitions/416.html), [CWE-401](https://cwe.mitre.org/data/definitions/401.html), [CWE-476](https://cwe.mitre.org/data/definitions/476.html), [CWE-134](https://cwe.mitre.org/data/definitions/134.html).
- Google, [AddressSanitizer: A Fast Address Sanity Checker](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37752.pdf).
- FIRST.org, [CVSS v3.1 Specification](https://www.first.org/cvss/specification-document).
