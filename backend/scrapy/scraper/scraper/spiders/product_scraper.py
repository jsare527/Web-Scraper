import scrapy
import urllib
from datetime import datetime
from ..items import GenericItem



class AmazonSpider(scrapy.Spider):
    name = "amazon_spider"

    def start_requests(self):

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
        }

        
        url = 'https://www.amazon.com/s?' + urllib.parse.urlencode({'k': self.category})
        yield scrapy.Request(url=url, callback=self.parse, headers=HEADERS)

    def parse(self, response):
        sections = response.css("div.a-section")
        for section in sections:
            item = GenericItem()
            item['title'] = section.css("h2 a span::text").extract()
            item['price'] = section.css("span.a-offscreen::text").extract()
            item['img'] = section.css("img.s-image::attr(src)").extract()
            yield item


class NewEggSpider(scrapy.Spider):
    name = "new_egg_spider"

    def start_requests(self):

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
        }

        
        url = 'https://www.newegg.com/p/pl?' + urllib.parse.urlencode({'d': self.category})
        yield scrapy.Request(url=url, callback=self.parse, meta={"proxy": "http://jeyyjdjc-rotate:zozi8si4to6q@p.webshare.io:80/"}, headers=HEADERS)

    def parse(self, response):
        sections = response.css("div.item-cell div.item-container")
        for section in sections:
            item = GenericItem()
            item['title'] = section.css("div.item-info a.item-title::text").extract()
            item['price'] = section.css("div.item-action ul.price li.price-current strong::text").extract()
            item['img'] = section.css("a.item-img img::attr(src)").extract()
            yield item