import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atd_emailutil",
    version="0.0.1",
    author="City of Austin",
    author_email="transportation.data@austintexas.gov",
    description="Python utilities for sending emails with a gmail account.",
    install_requires=[
      'yagmail',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cityofaustin/atd-data-utils-email",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", 
    ),
)
