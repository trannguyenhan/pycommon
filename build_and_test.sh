#!/bin/bash
# Script để build và test package pycommon

set -e

echo "=== Building pycommon package ==="

# Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 không được tìm thấy"
    exit 1
fi

# Cài đặt build tools nếu chưa có
echo "Installing build tools..."
pip3 install --upgrade build twine wheel 2>/dev/null || pip install --upgrade build twine wheel

# Xóa các build cũ
echo "Cleaning old builds..."
rm -rf build/ dist/ *.egg-info/

# Build package
echo "Building package..."
python3 -m build

echo ""
echo "=== Build completed successfully! ==="
echo "Package files are in dist/ directory:"
ls -lh dist/

echo ""
echo "=== To install locally: ==="
echo "pip install dist/pycommon-1.0.0-py3-none-any.whl"
echo ""
echo "=== To test installation: ==="
echo "pip install -e ."
echo "python test_package.py"
echo ""
echo "=== To upload to PyPI (test): ==="
echo "twine upload --repository-url https://test.pypi.org/legacy/ dist/*"
echo ""
echo "=== To upload to PyPI (production): ==="
echo "twine upload dist/*"

