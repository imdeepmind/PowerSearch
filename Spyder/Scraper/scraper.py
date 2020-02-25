import requests

from bs4 import BeautifulSoup

from logger.logger import logger

class Scrapper:
  """
    The Scrapper class in responsible for scrapping websites and extracting the title tag, meta description tag and all the anchor tags

  """

  def __init__(self, retry=3):
    """
      Constructor of the class Scrapper, used to setting up the Scrapper class

      Params:
        retry: Int
          Number of retry for downloading websites over the internet, the value need to be a number greater that 0, default and recommended value is 3

    """
    super().__init__()

    if type(retry) not in [int]:
      raise ValueError("The value for retry needed to be of type integer")

    if retry < 1:
      raise ValueError("The value for retry needed to be greater number bigger then 0")

    self.retry = retry
  
  def __load_url(self, url):
    count = 0
    success = False
    data = None

    while count < self.retry and not success:
      count += 1

      logger.info("Trying to load content from the URL: {}".format(url))
      r = requests.get(url)

      if r.ok:
        data = r.text
        success = True
        logger.info("Success downloaded the url: {}".format(url))
      else:
        raise ValueError("Not getting correct response from the target server, URL: {} Status Code: {}".format(url, r.status_code))
    
    return data

  def __extract_data(self, data, url):
    logger.info('Extracting data from the url: {}'.format(url))
    title = ''
    description = ''
    urls = []

    soup = BeautifulSoup(data, 'lxml')

    title = soup.find('title').text

    description_tag = soup.find('meta', attrs={'name': 'description'})
    if description_tag:
      description = description_tag['content']

    for a in soup.find_all('a'):
      link = a['href']
      urls.append(link)

    return title, description, urls
  
  def scrap(self, url):
    """
      This method in the class Scrapper is responsible for scrapping the websites.

      Params:
        url: string
          URL of the website, that needed to be scrapped

    """
    logger.info('URL received {}'.format(url))

    if type(url) not in [str]:
      raise ValueError("The value for url needed to be of type string")

    if len(url) < 1:
      raise ValueError("No URL provided")

    data = self.__load_url(url)
    title, description, urls = self.__extract_data(data, url)

    return title, description, urls  