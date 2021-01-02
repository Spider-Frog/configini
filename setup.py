import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configini",
    version="0.3",
    author="SpiderFrog",
    author_email="germanspiderfrog@gmail.com",
    description="Small package to easily parse an .ini file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spider-Frog/configini",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
