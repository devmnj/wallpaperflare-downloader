# wallspyder

Set of wallpaper download automation scripts using selenium package and Webdriver. You can search 
and download wall paper in a single line of brilliant python code,using the appropriate
classes.

# Websites Included

There are plenty of website which make available awesome wallpapers , but only following websites are available

1. http://wallpaperflare.com
2. http://pexels.com    -- Free stock images 
3. http://unsplash.com -- Free stock images

# How to use 

Go head, clone or install the package and just use the appropriate object to search and download 
images.

## On Windows

In Windows you can just install the pacakge from github git with `pip` command as follows

```python
Install the package
pip install git+https://github.com/manojap/wallspyder.git

from wallspyder import pexels
from wallspyder import flareDownloader

wallpaperflare.search('python').download(30)
pexels.search('fruits').download()
```

## On Linux or Mac

On linux and Mac you need to clone the repo and install requirements

```python
clone the repo

git clone https://github.com/manojap/wallspyder.git

pip install -r requirements.txt

from wallspyder import pexels
from wallspyder import flareDownloader

wallpaperflare.search('python').download(30)
pexels.search('fruits').download()
```

# Default Save location  - Firefox

Make sure your save location is set to `default [Firefox]` or do it for the `first time`, after the 
automation process begins and pop up window for file action.

# Delaying download

`Use delay` for wait some time for loading downloading button in slower internet connection

```python
cars = flareDownloader('cars').download(delay=100)
```

Even though I included the Firefox and chrome support.I recommend Chrome for `pexels` like sites 

# Future 

More site will be included in the upcoming. Welcome to join me on this humble effort

Have some picture sites in mind, i can scrap it, let me know.