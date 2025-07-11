# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages  # type: ignore
import sys

sys.path.append("Browser")

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

packages = find_packages(exclude=["utest", "atest"])

package_data = {
    "": ["*"],
    "Browser": [
        "wrapper/index.js",
        "wrapper/package.json",
        "wrapper/package-lock.json",
        "wrapper/static/selector-finder.js",
    ],
}

install_requires = open(os.path.join("Browser", "requirements.txt")).readlines()

setup_kwargs = {
    "name": "robotframework-browser",
    "version": "19.6.2",
    "description": "Robot Framework Browser library powered by Playwright. Aiming for speed, reliability and visibility.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "author": "MarketSquare - Robot Framework community",
    "author_email": "mikko.korpela@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/MarketSquare/robotframework-browser",
    "packages": packages,
    "package_dir": {"": "."},
    "package_data": package_data,
    "include_package_data": True,
    "install_requires": install_requires,
    "extras_require": {
        "tidy": ["robotframework-tidy>=4.12.0"]
    },
    "entry_points": {"console_scripts": ["rfbrowser=Browser.entry.__main__:cli"]},
    "python_requires": ">=3.9,<4.0",
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
    ],
    "include_package_data": True,
}


setup(**setup_kwargs)
