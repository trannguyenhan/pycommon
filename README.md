# pycommon

Thư viện các hàm tiện ích chung cho Python - hỗ trợ xử lý Word documents và chuỗi.

## Cài đặt

### Cài đặt từ PyPI (khi đã publish)

```bash
pip install pycommon
```

### Cài đặt từ source code

```bash
# Clone repository
git clone https://github.com/trannguyenhan/pycommon.git
cd pycommon

# Cài đặt
pip install .
```

### Cài đặt ở chế độ development

```bash
pip install -e .
```

## Sử dụng

### Import thư viện

```python
import pycommon
# hoặc import các hàm cụ thể
from pycommon import set_cell_background, set_table_borders, name_to_code
```

### Các hàm có sẵn

#### 1. Xử lý Word Documents

##### `set_cell_background(cell, color)`
Đặt màu nền cho một ô trong bảng Word.

```python
from docx import Document
from pycommon import set_cell_background

doc = Document()
table = doc.add_table(rows=1, cols=2)
cell = table.rows[0].cells[0]
set_cell_background(cell, 'D9D9D9')  # Màu xám nhạt
```

##### `set_table_borders(table)`
Thiết lập viền cho bảng Word (viền đen, đơn giản).

```python
from docx import Document
from pycommon import set_table_borders

doc = Document()
table = doc.add_table(rows=3, cols=3)
set_table_borders(table)
```

##### `append_doc(src_doc, dest_path)`
Nối nội dung từ document nguồn vào document đích.

```python
from docx import Document
from pycommon import append_doc

src_doc = Document('source.docx')
dest_doc = append_doc(src_doc, 'destination.docx')
dest_doc.save('merged.docx')
```

##### `add_heading(doc, text, style_text, FONT_NAME, FONT_SIZE, italic=False)`
Thêm heading vào document với định dạng tùy chỉnh.

```python
from docx import Document
from pycommon import add_heading

doc = Document()
add_heading(doc, "Tiêu đề", "Heading 1", "Times New Roman", 14, italic=False)
```

#### 2. Xử lý chuỗi

##### `name_to_code(name: str) -> str`
Chuyển đổi tên thành mã code (chữ hoa, không dấu, phân cách bằng dấu gạch dưới).

```python
from pycommon import name_to_code

code = name_to_code("Nguyễn Văn A")
print(code)  # Output: NGUYEN_VAN_A

code = name_to_code("Hà Nội - Việt Nam")
print(code)  # Output: HA_NOI_VIET_NAM
```

## Yêu cầu

- Python >= 3.7
- python-docx >= 0.8.11
- Unidecode >= 1.3.6

## Đóng gói và phát hành

### Build package

```bash
# Cài đặt build tools
pip install build twine

# Build package
python -m build
```

### Upload lên PyPI

```bash
# Upload lên PyPI test
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Upload lên PyPI chính thức
twine upload dist/*
```

## License

MIT License

## Tác giả

trannguyenhan
