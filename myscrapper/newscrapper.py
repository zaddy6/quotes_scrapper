# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.loader import ItemLoader

from myscrapper.myscrapper.items import MyscrapperItem


class NewscrapperSpider(Spider):
    name = 'newscrapper'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=MyscrapperItem(), response=response)
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:

            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            l.add_value('text', text)
            l.add_value('author', author)
            l.add_value('tags', tags)

            # yield  {
            #     'Text': text,
            #     'Author': author,
            #     'Tags': tags
            # }
            #
            # job.update(good_quotes)

            next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()

            absolute_path = response.urljoin(next_page)

            yield Request(absolute_path)

            return l.load_item()







        # yield {
        #     'H1 Tag': h1,
        #     'Tags':tag
        # }
