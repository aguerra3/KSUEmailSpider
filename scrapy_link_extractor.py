# scrapy_link_extractor.py
import scrapy
from scrapy.linkextractors import LinkExtractor
  
  
class QuoteSpider(scrapy.Spider):
    name = "OuoteSpider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
  
    def parse(self, response):
        link_extractor = LinkExtractor()
        links = link_extractor.extract_links(response)
  
        for link in links:
            yield {"url": link.url, "text": link.text}