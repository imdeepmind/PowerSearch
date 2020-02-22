import requests
import bs4

from logger import logger

class Scrapper:
  def __init__(self, retry=3):
    super().__init__()
    self.retry = retry
  
  def __load_url(self, url):
    count = 0
    success = False
    data = None

    while count < self.retry and not success:
      count += 1
      try:
        logger.info("Trying to load content from the URL: {}".format(url))
        r = requests.get(url)

        if r.ok:
          data = r.text
          success = True
          logger.info("Success downloaded the url: {}".format(url))
        else:
          raise ValueError("Not getting correct response from the target server, URL: {} Status Code: {}".format(url, r.status_code))
      
      except ValueError as ex:
        logger.error("Something is wrong with the url {}".format(url))

      except Exception as ex:
        logger.exception("Something went wrong")
    
    return data
  
  def scrap(self, url):
    data = self.__load_url(url)
    print(data)

scrapper = Scrapper()
scrapper.scrap("https://imdeepmind.com")

  