# import scrapy
# from product_scraper.items import Product
# import traceback

# class EcomSpider(scrapy.Spider):
#     name = 'ecom_spider'
#     myBaseUrl = 'https://www.amazon.in/realme-Feather-Segment-Charging-Slimmest/dp/B0C45N5VPT/ref=sr_1_2?_encoding=UTF8&refinements=p_36%3A1318505031%2Cp_n_condition-type%3A8609960031&s=electronics&sr=1-2&th=1'
#     start_urls = []
#     # allowed_domains = ['clever-lichterman-044f16.netlify.app']

#     def __init__(self, category='', **kwargs):
#         super(EcomSpider, self).__init__(**kwargs)
#         self.myBaseUrl = category
#         self.start_urls.append(self.myBaseUrl)
#         self.start_urls = [kwargs.get('url')]  # Set start_urls from the command line argument

#     def parse(self, response):
#         price = response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]/text()').get()
#         print()
#         result = {
#             'price' : price
#         }
#         yield result


# # import scrapy
# # from scrapy import Request
# # from scrapy.spiders import CrawlSpider, Rule
# # from scrapy.linkextractors import LinkExtractor

# # class EcomSpider(scrapy.Spider):
# #     name = 'ecom_spider'
# #     # allowed_domains = ["amazon.in"]
# #     myBaseUrl = ''
# #     start_urls = []
    # def __init__(self, category='', **kwargs): # The category variable will have the input URL.
    #     self.myBaseUrl = category
    #     self.start_urls.append(self.myBaseUrl)
    #     super(EcomSpider, self).__init__(**kwargs)
    
# #     custom_settings = {'FEED_URI': 'tutorial/outputfile.json', 'CLOSESPIDER_TIMEOUT' : 15}
# #     def parse(self, response):
#         # price = response.xpath('//*[@id="buyPriceBox"]/div[2]/div[1]/div[1]/div[1]/span[1]/span/text()').get()
#         # print()
#         # result = {
#         #     'price' : price
#         # }
#         # yield price
import scrapy

class MyItem(scrapy.Item):
    names = scrapy.Field()
    reviewerLink = scrapy.Field()
    reviewTitles = scrapy.Field()
    price = scrapy.Field()
    lprice = scrapy.Field()
    rev = scrapy.Field()
    title = scrapy.Field()
    disc = scrapy.Field()
    reviewBody = scrapy.Field()
    verifiedPurchase = scrapy.Field()
    postDate = scrapy.Field()
    starRating = scrapy.Field()
    helpful = scrapy.Field()
    nextPage = scrapy.Field(default = 'null')

class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewspider'
    # allowed_domains = ["amazon.in"]
    start_urls = ["https://www.amazon.in/AppIe-A%C3%ADrpo%E1%B8%8Ds-Pro-Generation-Apple/dp/B0CSNWH7R5/ref=sr_1_3?keywords=apple+airpods&sr=8-3"]
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls.append(self.myBaseUrl)
        super(ReviewspiderSpider, self).__init__(**kwargs)

    def parse(self, response):
        # Scraping all the items for all the reviewers mentioned on that Page
        price = response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]/text()').get()
        lprice = response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span[2]/span/span[2]/text()').get()
        rev = response.xpath('//*[@id="cm_cr_dp_d_rating_histogram"]/div[2]/div/div[2]/div/span/span/text()').get()
        title = response.xpath('//*[@id="productTitle"]/text()').get()
        disc = response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/text()').get() 
        yield MyItem(price=price , lprice=lprice , rev=rev , title=title,disc=disc)