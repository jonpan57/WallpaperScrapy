from .common import Spider


class Konachan(Spider):
    name = 'konachan'
    allowed_domains = ['konachan.com']
    start_urls = [
        'https://wallhaven.cc/api/v1/search'
    ]

    def parse(self, response):
        items = []
        data = response.json().get('data')
        for i in data:
            print(i['path'])
