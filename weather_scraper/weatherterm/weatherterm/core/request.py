import os
from selenium import webdriver

class Request:
    def __init__(self, base_url):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) #disables console logging which is outputting unrelated warning messages

        self._chromedriver_path = os.path.join(os.curdir, 'chromedriver/chromedriver.exe')
        self._base_url = base_url
        #self._driver = webdriver.Chrome(self._chromedriver_path)
        self._driver = webdriver.Chrome(self._chromedriver_path, chrome_options=chrome_options)

    def fetch_data(self, day, long, lat):
        if (day != 'fiveday'): #website URL no longer uses fiveday, so this is a quick patch for that
            url = self._base_url.format(day=day, lat=lat, long=long)
        else:
            url = self._base_url.format(day='tenday', lat=lat, long=long)
        self._driver.get(url)

        if (self._driver.title == '404 Not Found'):
            error_message = ('Could not find the area that you were searching for')
            raise Exception(error_message)

        return self._driver.page_source, self._driver
