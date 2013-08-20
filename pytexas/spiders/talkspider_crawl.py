from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from pytexas.items import PytexasItem

class TalkspiderCrawlSpider(CrawlSpider):
    name = 'talkspider_crawl'
    allowed_domains = ['www.pytexas.org']
    start_urls = ['http://www.pytexas.org/2013/talks/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/2013/talks/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #hxs = HtmlXPathSelector(response)
        l = XPathItemLoader(item=PytexasItem(), response=response)
        l.add_xpath('title', '//*/div[@class="span6"]/h2/text()')
        l.add_xpath('speaker', '//*/div[@class="span6"]/h3/text()')
        l.add_xpath('description', '//*/div[@class="span6"]/p[2]/text()')
        #l.add_value('last_updated', 'today') # you can also use literal values
        return l.load_item()

        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        #return i
