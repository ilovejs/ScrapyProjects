from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from task1.items import LivingSocialDeal

class LivingSocialSpider(BaseSpider):
    """Spider for regularly updated livingsocial.com site, San Francisco Page"""
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["http://www.livingsocial.com/cities/15-san-francisco"]

    deals_list_xpath = '//li[@dealid]'
    item_fields = {'title': './/div[@class="deal-details"]/h2[@itemprop="name"]/text()',
                   'link': './/a/@href',
                   'description': './/div[@class="deal-details"]/h3[@itemprop="seller"]/text()',
                   'category': './/a/div[@class="deal-image"]/p[@class="deal-category"]/text()',
                   'location': './/div[@class="deal-details"]/p[@class="location"]/text()',
                   'original_price': './/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/text()',
                   'price': './/div[@class="deal-prices"]/div[@class="deal-price"]/text()'}

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
