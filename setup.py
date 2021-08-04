import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pybinanceapi",
    version="0.1.3",
    description="Python Wrapper for the Binance API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nogira/py-binance-api",
    author="nogira",
    license="MIT",
    packages=["pybinanceapi"],
    include_package_data=True,
)