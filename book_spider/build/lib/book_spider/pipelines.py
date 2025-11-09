import sqlite3
from itemadapter import ItemAdapter

class BookSpiderPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('books.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                price TEXT,
                availability TEXT,
                rating TEXT,
                rating_value INTEGER,
                product_link TEXT,
                image_url TEXT,
                alt_text TEXT
            )
        ''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.c.execute('''
            INSERT INTO books (
                title, price, availability, rating, rating_value, product_link, image_url, alt_text
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            adapter.get('title'),
            adapter.get('price'),
            adapter.get('availability'),
            adapter.get('rating'),
            adapter.get('rating_value'),
            adapter.get('product_link'),
            adapter.get('image_url'),
            adapter.get('alt_text')
        ))
        self.conn.commit()
        return item
