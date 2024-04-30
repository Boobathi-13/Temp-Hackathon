import scrapy

class MyItem(scrapy.Item):
    names = scrapy.Field()
    reviewerLink = scrapy.Field()
    reviewTitles = scrapy.Field()
    reviewBody = scrapy.Field()
    verifiedPurchase = scrapy.Field()
    postDate = scrapy.Field()
    starRating = scrapy.Field()
    helpful = scrapy.Field()
    nextPage = scrapy.Field(default = 'null')