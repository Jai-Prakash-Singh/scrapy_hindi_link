from scrapy.spider import BaseSpider
from scrapy.selector import Selector


class DmozSpider(BaseSpider):
    name = "direc-link"
    allowed_domains = ["hindilinks4u.net"]
    start_urls = [ "http://www.hindilinks4u.net/"]

    def parse(self, response):
        sel = Selector(response)
        dlink  =  sel.xpath("/html/body/div/div[7]/div/ul/li[6]/ul/li/a/@href").extract()
        f = open("direc_link","w+")
        print >>f, ",".join(dlink)
        f.close()
