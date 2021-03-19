#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0", "colorama>=0.4", "watchdog>=2.0", "emoji>=1.2"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Sotunde Abiodun Oladimeji",
    author_email="sotundeabiodun00@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python Sync Dotenv is a Python package for synchronizing .env files  across projects.",
    entry_points={
        "console_scripts": [
            "py-sync-dotenv=py_sync_dotenv.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="py_sync_dotenv",
    name="py_sync_dotenv",
    packages=find_packages(include=["py_sync_dotenv", "py_sync_dotenv.*"]),
    setup_requires=setup_requirements,
    long_description_content_type="text/x-rst",
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/IamAbbey/py_sync_dotenv",
    version="0.1.1",
    zip_safe=False,
)
