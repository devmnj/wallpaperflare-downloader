import setuptools
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'README.md')

with open(my_file, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wallspider",  # Replace with your own username
    version="0.0.1",
    author="Manoj",
    author_email="manojap@outlook.com",
    description="Wallpaper downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manojap/wallspyder",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
