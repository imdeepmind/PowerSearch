import requests
import re

from bs4 import BeautifulSoup

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

  def __extract_correct_url(self, url, link):
    if re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', link):
      return link

    if url[-1] == '/' or link[0] == '/':
      return url + link

    return url + '/' + link

  def __extract_data(self, data, url):
    logger.info('Extracting data from the url: {}'.format(url))

    soup = BeautifulSoup(data, 'lxml')

    title = soup.find('title').text
    description = soup.find_all('meta', attrs={'name': 'description'})[0]['content']

    urls = []

    for a in soup.find_all('a'):
      link = a['href']
      urls.append(self.__extract_correct_url(url, link))

    return title, description, urls
  
  def scrap(self, url):
    data = self.__load_url(url)
    title, description, urls = self.__extract_data(data, url)

    return title, description, urls  