from pathlib import Path

from skbuild import setup

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="PyPcl",
    version="0.0.1",
    description="Point Cloud Library for Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="hiroyuki shimatani",
    packages=["pypcl"],
    python_requires=">=3.11",
)
