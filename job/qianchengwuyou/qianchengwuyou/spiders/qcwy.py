# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qianchengwuyou.items import *

class QcwySpider(CrawlSpider):
    name = 'qcwy'
    # allowed_domains = ['www.51job.com/']
    start_urls = ['https://search.51job.com/list/000000,000000,7700%252C7200%252C0100,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
]

    rules = (
        Rule(LinkExtractor(allow='jobs.51job.com',restrict_css='#resultList .el .t1 span a'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//*[@class="bk"]/a'))
    )

    def parse_item(self, response):
        item=QianchengwuyouItem()
        item["job_name"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()').extract_first()
        item["salary"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').extract_first().split('-')[0]+'k'
        item["degree"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[3]').extract_first()
        item["experience"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[2]').extract_first()
        item["category"] =response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div[1]/p[1]/a/text()').extract_first()
        item["address"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[1]').extract_first().split('-')[0]
        # item["company"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]/text()').extract_first()
        # item["demand"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[6]').extract_first()
        # item["want_numbers"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[4]').extract_first()
        # item["dateline"] =response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[5]').extract_first()
        # item["keyword"] =response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div[1]/p[2]/a[1]/text()').extract_first()
        # item["url"] =response.url
        yield item
