import scrapy
from scrapy.http import FormRequest
import urllib
from items import quotesItem

class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    
    start_urls = [
        'http://quotes.toscrape.com/login'
        ]
    #LOGIN NA PAGINA QUOTES
    def parse(self, response):
        
        token = response.css('form input::attr(value)') .extract()
        return FormRequest.from_response(response, formdata={
            'token': token, 
            'username': 'myra',
            'password': 'myra123'
        }, callback=self.scraper)
        
    #INICIO DA FUNÇÃO E EXTRAÇÃO DE DADOS
    def scraper(self, response):
        custom_settings = {
        'FEEDS' : {
            'file://page-1.csv' : { 
                'format' : 'csv',
                'store_empty' : True
            }
        },
        'FEED_EXPORT_ENCODING' : 'utf-8',
        'FEED_EXPORT_FIELDS' : ['author', 'quote']
    }
        items = quotesItem()
        

        all_quotes = response.css('div.quote')
        
        for div in all_quotes:
            quote = div.css('.text::text').extract()
            authors = div.css('.author::text').extract()
            tags = div.css('.tags a::text').extract()

            items['quote'] = quote
            items['author'] = authors
            items['tags'] = tags

            yield items

        next_page = response.css('.next a::attr(href)').get()
        #CALLBACK PARA
        if next_page is not None:
            yield response.follow(next_page, callback=self.scraper)