import os
from pathlib import Path
import sys

from skbuild import setup

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pcl-python",
    packages=["pypcl"],
    version="0.0.2",
    description="Python binding for Point Cloud Library (PCL)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Hiroyuki Shimatani",
    url="https://github.com/turingmotors/PyPcl",
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        f"Architecture :: {os.uname().machine}",
    ],
)
