import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Downloader for unsplash.com

class search:
    """ Class which provides search and download free stock images from
    www.unsplash.com
    """
    photo_url = []
    browser = None
    chrome_opt = Options()

    def __init__(self, br_name='Chrome'):
        """
        Initialize Unsplash bot

        :param br_name: configure browser for automation (default Chrome)
        :type br_name: str

        """
        base_urls = []
        if br_name != 'Chrome':
            self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def find(self, search, delay=2, head_less=False):

        """  Search for stock free images from unsplash.com using
         unsplash bot

        :param search: search term
        :type search: str
        :param delay: delaying loading searched gallery, in seconds (default 2)
        :type delay: int
        :param head_less: mode of working, can run in the back ground in head_less mode (default False) -- coming soon
        :type delay: bool
        """

        try:
            self.browser.get(f'https://www.unsplash.com/s/photos/{search}')

            time.sleep(delay)
            print('You are using unsplash.com - Free stock images')
            root = self.browser.find_elements_by_class_name('qztBA')
            for r in root:
                root2 = r.find_elements_by_tag_name('div')
                for d1 in root2:
                    div1 = d1.find_elements_by_class_name('nDTlD')
                    for d2 in div1:
                        fig = d2.find_elements_by_tag_name('figure')
                        for f in fig:
                            div3 = f.find_elements_by_class_name('_232xU')
                            for ar in div3:
                                div4 = ar.find_elements_by_class_name('_3A74U')
                                for d4 in div4:
                                    d5 = d4.find_elements_by_class_name('_1hIRM')
                                    for a in d5:
                                        link = a.find_elements_by_tag_name('a')
                                        x = link[0].get_property('href')
                                        self.photo_url.append(x)
            self.download()
        except:
            pass

    def filter_by_tag(self, tag, delay=2):

        """ Search for stock free images from unsplash.com using
        tag name


        :param tag: search tag
        :type tag: str

        :param delay: delaying loading searched gallery, in seconds (default 2)
        :type delay: int

        """

        try:

            self.browser.get(f'https://www.unsplash.com/t/{tag}')

            time.sleep(delay)
            print('You are using unsplash.com - Free stock images')
            root = self.browser.find_elements_by_class_name('qztBA')
            for r in root:
                root2 = r.find_elements_by_tag_name('div')
                for d1 in root2:
                    div1 = d1.find_elements_by_class_name('nDTlD')
                    for d2 in div1:
                        fig = d2.find_elements_by_tag_name('figure')
                        for f in fig:
                            div31 = f.find_elements_by_class_name('_6IG7')
                            for d4 in div31:
                                d5 = d4.find_elements_by_class_name('_1hIRM')
                                for a in d5:
                                    link = a.find_elements_by_tag_name('a')
                                    x = link[0].get_property('href')
                                    self.photo_url.append(x)
            self.download()
        except:
            pass

    def download(self, delay=1):
        """
        Download stock photos from unsplash.com

        :param delay: delaying download in second (default 1)
        :type  delay: int
        """
        if self.photo_url.__len__() > 0:
            count = 0
            print(f'Looking for possible ...{self.photo_url.__len__()} Wallpapers')
            for l1 in self.photo_url:
                try:
                    print(l1)
                    self.browser.get(l1)
                    proute = self.browser.find_elements_by_class_name('_2vsJm')
                    a = proute[0].find_elements_by_tag_name('a')
                    time.sleep(delay)
                    a[0].click()
                    count = count + 1

                except:
                    pass
            print(f'{count}  wallpapers downloaded')
        else:
            print('No photo found, slow internet connection may be')
            self.__del__()

    def __del__(self):
        try:
            self.browser.close()
            print('Completed')
            quit()
        except:
            pass
