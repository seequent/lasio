"""Setup script for lasio"""

import lasio
from setuptools import setup
import os

__init__file = './lasio/__init__.py'
with open(__init__file, 'r') as f:
    file_contents = f.read()

changed_file_contents = file_contents.replace('__version__ = version()', f'__version__ = \'{lasio.version()}\'')

with open(__init__file, 'w') as f:
    f.write(changed_file_contents)

EXTRA_REQS = ("pandas", "cchardet", "openpyxl")
TEST_REQS = (
    "pytest>=3.6",
    "pytest-cov",
    "coverage",
    "codecov",
    "pytest-benchmark",
    "black",
)

setup(
    name="lasio",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Read/write well data from Log ASCII Standard (LAS) files",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kinverarity1/lasio",
    author="Kent Inverarity",
    author_email="kinverarity@hotmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Filesystems",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords="science geophysics io",
    packages=("lasio",),
    python_requires=">=3",
    install_requires=("numpy",),
    extras_require={"all": EXTRA_REQS, "test": (EXTRA_REQS, TEST_REQS)},
    tests_require=(TEST_REQS),
    entry_points={
        "console_scripts": (
            "las2excel = lasio.excel:main",
            "las2excelbulk = lasio.excel:main_bulk",
            "lasversionconvert = lasio.convert_version:convert_version",
            "lasio = lasio:version",
        )
    },
)
