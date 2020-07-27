import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="wallbay",
    version="1.0.0",
    author="Manoj A.P",
    author_email="manojap@outlook.com",
    description="Wallpaper downloading bots",
    license="BSD",
    keywords="wallpaper,download,stock images",
    url="http://github.com/manojap/wallspyder",
    packages=['wallbay'],
    long_description=read('readme.md'),
    install_requires=['selenium', 'webdriver-manager'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Fun",
        "License :: OSI Approved :: BSD License",
    ],
)
