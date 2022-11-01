import setuptools

# Auxiliary function
def read_file(filename: str) -> str:
    """
    Return the content of a file.

    Parameters
    ----------
        filename (str) path to the file
    
    Returns
    -------
        (str) file content
    """
    with open(filename, "r", encoding="utf-8") as fh_read:
        content = fh_read.read()
    return content

# Read file contents
long_description: str = read_file("README.md")


# Metadata
setuptools.setup(
    name="file_organiser",
    version="1.0.0-alpha",
    author="",
    author_email="",
    maintainer="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
    },
    download_url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(
        where="src",
        exclude="tests"
    ),
    python_requires=">=3.8",
    install_requires=open('requirements.txt', 'r').read().split('\n'),
    # For CLI
    entry_points={
        'console_scripts': []
    }
)