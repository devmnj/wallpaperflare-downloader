import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Downloader for Wallpaperflare.com


class search:
    """ Class which provides search and download wall paper appropriate for your
     screen resolution from  www.wallpaperflare.com
      """
    base_url = []
    browser = None

    def __init__(self, search, browser='Firefox'):

        """ Initialize the search for wallapaers from wallpaperflare.com


            :param search: search term
            :type search: str
            :param browser: configure browser for automation (default Firefox)
            :type browser: str (default Firefox)

            """

        try:

            base_urls = []
            if browser != 'Firefox':
                self.browser = webdriver.Chrome(ChromeDriverManager().install())
            else:
                self.browser= webdriver.Firefox(executable_path=GeckoDriverManager().install())

            self.browser.get(f'https://www.wallpaperflare.com/search?wallpaper={search}')
            time.sleep(3)
            ele = self.browser.find_elements_by_id('gallery')
            for e in ele:
                ol = e.find_elements_by_tag_name('li')
                for l in ol:
                    if l.get_attribute('itemprop') == 'associatedMedia':
                        fig = l.find_elements_by_tag_name('figure')
                        for f in fig:
                            lnk = f.find_elements_by_tag_name('a')
                            for d in lnk:
                                if d.get_attribute('rel') != 'license':
                                    url = d.get_property('href')
                                    self.base_url.append(url)
        except:
            pass

    def download(self, delay=20):
        """
               Download wallpapers from wallpaperflare.com

               :param delay: delaying download in second (default 20)
               :type  delay: int
               """
        count = 0

        if self.base_url.__len__() > 0:
            print(f'Looking for possible ...{self.base_url.__len__()} Wallpapers')
            for l1 in self.base_url:
                try:
                    self.browser.get(l1)
                    self.browser.find_element_by_id('cur_screen').click()
                    # wait for completely load the page
                    time.sleep(1)
                    url = self.browser.current_url

                    if str(url).find('/download/') >= 0:
                        self.browser.get(url)
                        time.sleep(delay)
                        print(f'Downloading ...{url}')
                        dl_link = self.browser.find_element_by_id('dld_result')
                        dl_link.click()
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

