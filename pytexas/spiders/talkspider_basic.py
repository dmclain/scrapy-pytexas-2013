from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from pytexas.items import PytexasItem

class TalkspiderBasicSpider(BaseSpider):
    name = "talkspider_basic"
    allowed_domains = ["www2.pytexas.org"]
    start_urls = ['http://www.pytexas.org/2013/schedule/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        dls = hxs.select('///dl')
        for dl in dls:
            times = dl.select('dt/text()').extract()
            titles = dl.select('dd/a/text()').extract()
            for time, title in zip(times, titles):
                title = title.strip()
                yield PytexasItem(title=title, time=time)
