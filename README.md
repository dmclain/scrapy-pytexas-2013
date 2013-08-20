scrapy-pytexas-2013
===================

This code was used in the presentation I gave at PyTexas 2013 in College Station, TX.

The important files are:: 
/spiders/talkspider_basic - parse a single page and yield a series of items
/spiders/talkspider_crawl - use CrawlSpider to go to individual talk pages and generate items there
/spiders/talkspider_advanced - starting from the schedule page, generate requests for later pages and pass information using request.meta
