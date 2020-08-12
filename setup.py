import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wallspider",  # Replace with your own username
    version="0.0.1",
    author="Manoj",
    author_email="manojap@outlook.com",
    description="Wallpaper downloader",
    long_description="A set of selenium bots for automate wallpaper/stock free image downloading",
    long_description_content_type="text/markdown",
    url="https://github.com/manojap/wallspyder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
