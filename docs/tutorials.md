You can download almost any thing from the list  of sites using appropriate 
modules.

### Wallpaperflare.com
  
The search class let you search and download wallpapers. It automatically download and install necessary
webdriver for your system. 
````
pip install git+http://github.com/manojap/wallspyder.git

from wallsyder import wallpaperflare

wallpaperflare.search('flowers').download()

````
### Pexels.com
This is one of the leading source for designing and web development. Install the wallspyder and enjoy quality pexels offers.

````
pip install git+http://github.com/manojap/wallspyder.git

from wallsyder import pexels

pexels.search('flowers').download()

```` 
### unsplash.com
Unsplash is one of my favorite which has more artistic content and I personally contribute many pitures to the community.
I have slitely different methods for unplash.
- Find - for search image by terms
- filter_by_tag - find images using tags

````
pip install git+http://github.com/manojap/wallspyder.git

from wallspyder import unsplash

unsplash.search().filter_by_tag('travel')
unsplash.search().filter_by_tag('women')

```` 
### Not working
If the above steps don't make it for just clone the repo use it or use a lite version from PYPI 
```python
git clone http://github.com/manojap/wallspyder.git
pip install -r requirements.txt
```
### pip and Wallspyder
 Do you know , can directly install a working version of this package from PYPI using
 
 ```python
pip install wallspyder
```

