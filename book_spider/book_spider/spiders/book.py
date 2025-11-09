import scrapy

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.xpath('//article[@class="product_pod"]')

        for book in books:
            title = book.xpath('.//h3/a/@title').get()
            price = book.xpath('.//p[@class="price_color"]/text()').get()
            availability = ''.join(book.xpath('.//p[contains(@class,"instock")]/text()').getall()).strip()
            rating_class = book.xpath('.//p[contains(@class,"star-rating")]/@class').get()
            link = book.xpath('.//h3/a/@href').get()
            image = book.xpath('.//div[@class="image_container"]/a/img/@src').get()
            alt_text = book.xpath('.//div[@class="image_container"]/a/img/@alt').get()

            # Clean and convert rating
            rating = rating_class.replace("star-rating", "").strip() if rating_class else None
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating_num = rating_map.get(rating, None)

            # Join absolute URLs
            product_link = response.urljoin(link)
            image_url = response.urljoin(image)

            print(f"\nTitle: {title}")
            print(f"Price: {price}")
            print(f"Availability: {availability}")
            print(f"Rating: {rating} ({rating_num})")
            print(f"Link: {product_link}")
            print(f"Image: {image_url}")
            print(f"Alt Text: {alt_text}")

            yield {
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "rating_value": rating_num,
                "product_link": product_link,
                "image_url": image_url,
                "altText": alt_text,
            }

        # Follow pagination
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
