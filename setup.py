import os
from pathlib import Path
import sys

from skbuild import setup

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# プラットフォームに応じてmanylinuxタグを設定する
if sys.platform.startswith("linux"):
    machine = os.uname().machine
    if machine == "x86_64":
        manylinux_tag = "manylinux2014_x86_64"
    elif machine == "aarch64":
        manylinux_tag = "manylinux2014_aarch64"
    else:
        raise ValueError(f"Unsupported machine: {machine}")
else:
    manylinux_tag = None

setup(
    name="pcl-python",
    packages=["pypcl"],
    version="0.0.1",
    description="Point Cloud Library for Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Hiroyuki Shimatani",
    url="https://github.com/turingmotors/PyPcl",
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        f"Platform :: {manylinux_tag}" if manylinux_tag else "",
    ],
)
