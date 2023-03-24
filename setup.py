import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkdocstopandoc",                  # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Rosthouse",                     # Full name of the author
    description="A panflute filter for pandoc, which converts the specific markdown extensions of MKDocs",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',                # Minimum version requirement of the package
    py_modules=["mkdocstopandoc"],             # Name of the python package
    # Directory of the source code of the package
    entry_points={'console_scripts': ['mkdocstopandoc = mkdocstopandoc:main']},
    package_dir={'': 'src'},
    install_requires=[
        "panflute>=2.3.0"
    ]                     # Install other dependencies if any
)
