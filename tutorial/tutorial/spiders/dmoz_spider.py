import scrapy
from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//ul[@class="directory-url"]/li'):
            item = TutorialItem()
            item['title'] = sel.xpath('a/text()').extract()[0]
            item['link'] = sel.xpath('a/@href').extract()[0]
            item['desc'] = sel.xpath('text()').extract()[1].strip()[2:]
            yield
            # print 'Title:{0}\nLink:{1}\nDesc:{2}'.format(item['title'], item['link'], item['desc'])
            # print '-------------------------------------------'