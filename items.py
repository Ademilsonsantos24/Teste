import scrapy


class quotesItem(scrapy.Item):
    
    source = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    quote = scrapy.Field()        