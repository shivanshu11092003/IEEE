import scrapy

class CyberIncidentSpider(scrapy.Spider):
    name = 'cyber_incident'
    allowed_domains = ['timesofindia.indiatimes.com', 'economictimes.indiatimes.com', 'thehackernews.com']
    
    start_urls = [
        'https://timesofindia.indiatimes.com/topic/cybersecurity',
        'https://economictimes.indiatimes.com/news/cybersecurity',
        'https://thehackernews.com/search/label/Cyber%20Attack'
    ]

    def parse(self, response):
        """
        Parses the listing page, extracts article links, and follows each link.
        """
        # For each article, extract its link
        for article in response.css('a[href]::attr(href)').getall():
            # Follow the link to the article page
            yield response.follow(article, self.parse_article)

        # Follow the pagination links
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        """
        Parses the article detail page, extracts title, date, content, and URL.
        """
        yield {
            'title': response.css('h1::text').get(),  # Get the article title
            'link': response.url,  # Get the article URL
            'date': response.css('.publish-date::text').get(),  # Get the date (update selector if necessary)
            'content': ' '.join(response.css('p::text').getall()),  # Get all the paragraphs from the article
        }
