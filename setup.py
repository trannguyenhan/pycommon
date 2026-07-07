from setuptools import setup, find_packages
import os

# Đọc README để làm long_description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

setup(
    name='pycommon',
    version='1.0.0',
    description='Thư viện các hàm tiện ích chung cho Python - xử lý Word documents và chuỗi',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='trannguyenhan',
    author_email='',  # Thêm email nếu có
    url='https://github.com/trannguyenhan/pycommon',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    install_requires=[
        'python-docx>=0.8.11',
        'Unidecode>=1.3.6',
    ],
    keywords='word document docx utility common functions',
    project_urls={
        'Bug Reports': 'https://github.com/trannguyenhan/pycommon/issues',
        'Source': 'https://github.com/trannguyenhan/pycommon',
    },
)

