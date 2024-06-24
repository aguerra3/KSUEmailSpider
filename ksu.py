import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import re

page_count = 0
class ksu(CrawlSpider):
    name = "ksuSpider"
    
    allowed_domains = ["kennesaw.edu"]
    start_urls = ["https://www.kennesaw.edu"]

    fetch_links = LinkExtractor(restrict_css='a:link')

    rule_link = Rule(fetch_links,callback='parse_item', follow=True)
    rules = (

         rule_link,
     )
   
    def parse_item(self, response):
        global page_count 
        page_count += 1
        html_text = str(response.text)
        email_list = re.findall('\w+@\w+\.{1}\w+', html_text)
        email_list = set(email_list)
        entry = {
        "pageid" : page_count,
        "url": response.url,
        "title": response.css("head > title ::text").get(),
        "body": response.xpath('//body//p//text()').extract(),
        "emails": email_list
        }

        
        yield entry
    



