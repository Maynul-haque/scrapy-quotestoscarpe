import scrapy
from ..items import QuotestutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com']
    page_number = 2
    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):

        items = QuotestutorialItem()

        all_div_quotes=response.css('div.quote')

        for quotes in all_div_quotes:
            title=quotes.css('span.text::text').extract()
            author=quotes.css('small.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        #using the next button
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        #using pagination
        next_page = "https://quotes.toscrape.com/page/"+str(QuotesSpider.page_number)+"/"
        
        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
            