import unittest

from Scraper import Scraper

class TestScraper(unittest.TestCase):
  def test_Scraper_constructor(self):
    self.assertRaises(ValueError, Scraper, 'hello')
    self.assertRaises(ValueError, Scraper, [])
    self.assertRaises(ValueError, Scraper, False)
    self.assertRaises(ValueError, Scraper, -5)
    self.assertRaises(ValueError, Scraper, -98j)
    self.assertRaises(ValueError, Scraper, 5.32)
  
  def test_Scraper_scrap(self):
    Scraper = Scraper(3)
    self.assertRaises(ValueError, Scraper.scrap, 12)
    self.assertRaises(ValueError, Scraper.scrap, [])
    self.assertRaises(ValueError, Scraper.scrap, False)
    self.assertIs(type(Scraper.scrap('https://imdeepmind.com')), tuple)
    self.assertIs(type(Scraper.scrap('https://facebook.com')), tuple)
    self.assertIs(type(Scraper.scrap('https://google.com')), tuple)
    self.assertIs(type(Scraper.scrap('https://microsoft.com')), tuple)
    self.assertIs(type(Scraper.scrap('https://wikipedia.org')), tuple)

    self.assertRaises(Exception, Scraper.scrap, 'https://wikipedasdasdkjia.org')
    self.assertRaises(Exception, Scraper.scrap, 'https://tryuio.comad')
    
