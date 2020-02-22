import unittest

from scrapper import Scrapper

class TestScrapper(unittest.TestCase):
  def test_scrapper_constructor(self):
    self.assertRaises(ValueError, Scrapper, 'hello')
    self.assertRaises(ValueError, Scrapper, [])
    self.assertRaises(ValueError, Scrapper, False)
    self.assertRaises(ValueError, Scrapper, -5)
    self.assertRaises(ValueError, Scrapper, -98j)
    self.assertRaises(ValueError, Scrapper, 5.32)
  
  def test_scrapper_scrap(self):
    scrapper = Scrapper(3)
    self.assertRaises(ValueError, scrapper.scrap, 12)
    self.assertRaises(ValueError, scrapper.scrap, [])
    self.assertRaises(ValueError, scrapper.scrap, False)
    self.assertIs(type(scrapper.scrap('https://imdeepmind.com')), tuple)
    self.assertIs(type(scrapper.scrap('https://facebook.com')), tuple)
    self.assertIs(type(scrapper.scrap('https://google.com')), tuple)
    self.assertIs(type(scrapper.scrap('https://microsoft.com')), tuple)
    self.assertIs(type(scrapper.scrap('https://wikipedia.org')), tuple)

    self.assertRaises(Exception, scrapper.scrap, 'https://wikipedasdasdkjia.org')
    self.assertRaises(Exception, scrapper.scrap, 'https://tryuio.comad')
    
