# -*- coding: utf-8 -*-
from scrapy import Spider, Request



class NewscrapperSpider(Spider):
    name = 'newscrapper'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:

            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()



            yield  {
                'Text': text,
                'Author': author,
                'Tags': tags
            }
            #
            # job.update(good_quotes)

            next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()

            absolute_path = response.urljoin(next_page)

            yield Request(absolute_path)









        # yield {
        #     'H1 Tag': h1,
        #     'Tags':tag
        # }
