from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import BaseSpider
from pytexas.items import PytexasItem

class TalkspiderAdvancedSpider(BaseSpider):
    name = 'talkspider_advanced'
    allowed_domains = ['www.pytexas.org']
    start_urls = ['http://www.pytexas.org/2013/schedule/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        dls = hxs.select('///dl')
        for dl in dls:
            times = dl.select('dt/text()').extract()
            titles = dl.select('dd/a/text()').extract()
            hrefs = dl.select('dd/a/@href').extract()
            for time, title, href in zip(times, titles, hrefs):
                title = title.strip()
                yield Request(
                    url=''.join(('http://www.pytexas.org', href)),
                    callback=self.parse_item,
                    meta={'time': time, 'title': title}
                )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = PytexasItem()
        item['title'] = response.meta['title']
        item['time'] = response.meta['time']
        item['speaker'] = hxs.select('//*/div[@class="span6"]/h3/text()').extract()[0]
        item['description'] = '\n'.join(hxs.select('//*/div[@class="span6"]/p/text()').extract())
        return item
