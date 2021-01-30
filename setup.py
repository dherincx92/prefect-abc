#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

VERSION = __version__ = "0.0.0"

AUTHOR = "Derek Herincx"
AUTHOR_EMAIL = "derek663@gmail.com"
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Programming Language :: Python :: 3.9.0",
]
INCLUDE_PACKAGE_DATA = True
INSTALL_REQUIRES = open("requirements.txt").read().splitlines()
KEYWORDS = "prefect abstract class flow data pipeline inheritance"
LONG_DESCRIPTION = open("README.md").read()

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=CLASSIFIERS,
    include_package_data=INCLUDE_PACKAGE_DATA,
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    long_description=LONG_DESCRIPTION,
    name="prefect-abstract-runner",
    packages=find_packages(include=["src", "src.*"]),
    python_requires=">=3.7",
    version=VERSION,
)
