# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# items.py
import scrapy

class BookSpiderItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    rating = scrapy.Field()
    rating_value = scrapy.Field()
    product_link = scrapy.Field()
    image_url = scrapy.Field()
    alt_text = scrapy.Field()
