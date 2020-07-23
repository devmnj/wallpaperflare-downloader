import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Downloader for Wallpaperflare.com

class flareDownloader:
    base_url = []
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def __init__(self, search, browser='Firefox'):
        base_urls = []
        if browser != 'Firefox':
            self.browser = webdriver.Chrome(ChromeDriverManager().install())


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

    def download(self, delay=20):
        count = 0
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

    def __del__(self):
        self.browser.close()
        print('Completed')
        quit()
