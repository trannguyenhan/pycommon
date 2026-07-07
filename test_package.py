#!/usr/bin/env python
"""
Script test để kiểm tra package sau khi cài đặt
"""
try:
    import pycommon
    print("✓ Import pycommon thành công!")
    print(f"  Version: {pycommon.__version__}")
    print(f"  Available functions: {pycommon.__all__}")
    
    # Test name_to_code
    result = pycommon.name_to_code("Nguyễn Văn A")
    print(f"✓ name_to_code test: '{result}'")
    assert result == "NGUYEN_VAN_A", f"Expected 'NGUYEN_VAN_A', got '{result}'"
    
    print("\n✓ Tất cả tests đều pass!")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("  Hãy cài đặt package trước: pip install -e .")
except Exception as e:
    print(f"✗ Error: {e}")

