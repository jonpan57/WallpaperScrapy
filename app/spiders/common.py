import scrapy


class Spider(scrapy.Spider):
    name = ''
    allowed_domains = []
    start_urls = []

    def parse(self, response):
        pass



