import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Downloader for pexels.com

class search:
    """ Class which provides search and download free stock images from
    www.pexels.com
    """
    photo_url = []
    browser = None
    chrome_opt = Options()

    def __init__(self, search, browser='Firefox', delay=2, head_less=False):

        """ Initialize the search for stock free images from pexels.com using
        selenium automation with Firefox or Chrome browser Driver


        :param search: search term
        :type search: str
        :param browser: configure browser for automation (default Firefox)
        :type browser: str (default Firefox)
        :param delay: delaying loading searched gallery, in seconds (default 2)
        :type delay: int
        :param head_less: mode of working, can run in the back ground in head_less mode (default False) -- coming soon
        :type delay: bool
        """

        try:
            base_urls = []
            if browser != 'Firefox':
                if head_less is True:
                    self.chrome_opt.add_argument('--headless')
                self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            else:
                self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

            self.browser.get(f'https://www.pexels.com/search/{search}')

            time.sleep(delay)
            print('You are using pexels.com - Free stock photos')
            result = self.browser.find_element_by_class_name('search__grid')

            photos = result.find_elements_by_class_name('photos')
            for p in photos:
                cols = p.find_elements_by_class_name('photos__column')
                for l1 in cols:
                    photo_divs = l1.find_elements_by_class_name('hide-featured-badge')
                    for f in photo_divs:
                        articles = f.find_elements_by_tag_name('article')
                        for ar in articles:
                            art_link = ar.find_elements_by_tag_name('a')
                            for a in art_link:
                                url = a.get_property('href')
                                if str(url).find('@') < 0 and str(url).find('download') < 0:
                                    self.photo_url.append(url)
        except:
            pass

    def download(self, delay=1):
        """
        Download stock photos from pexels.com

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
                    time.sleep(delay)
                    dn = self.browser.find_element_by_class_name('rd__button--download')
                    time.sleep(1)
                    dn.click()
                    time.sleep(3)
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
