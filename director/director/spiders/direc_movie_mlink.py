
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys

class DmozSpider(BaseSpider):
    name = "direc_movie_mlink"
    allowed_domains = ["hindilinks4u.net"]
    f = open("direc_link") 
    
    avail_urls = f.read().replace("\n","").split(",")
    print len(avail_urls)
    
    f.close()
    start_urls = avail_urls[:]
  
     

    def parse(self, response):
        start = response.url.find("=")
        director_name = response.url[start+1:]

        sel = Selector(response)
        direc_movie_mlink  = sel.xpath('/html/body/div/div[6]/ul/li[5]/div')
        #sys.exit()
        for l in direc_movie_mlink:
            movie__link = str(l.xpath("a/@href").extract()[0])
            movie_name = str(l.xpath("a/text()").extract()[0])
            

            f = open("direc_movie_mlink","a+")
            print >>f, ", ".join([director_name, movie_name, movie__link])
            print [director_name, movie_name, movie__link]
            f.close()
           
        
