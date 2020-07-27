import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wallspyder", # Replace with your own username
    version="0.0.1",
    author="MANOJ AP",
    author_email="manojap@outlook.com",
    description="A collection of  selenium automation scripts for downloading Wallpapers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manojap/wallspyder",
    packages=setuptools.find_packages(),
    install_requires=['webdriver_manager','selenium'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
