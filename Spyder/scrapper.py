import requests
import bs4

class Scrapper:
  def __init__(self, retry=3):
    super().__init__()
    self.retry = retry

  
  def __load_url(self, url):
    count = 0
    success = False
    error = None

    while count < self.retry and not success:
      try:
        r = requests.get(url)
        data = r.text
      except Exception as ex:
        pass
  
  def scrap(self, url):
    pass

  