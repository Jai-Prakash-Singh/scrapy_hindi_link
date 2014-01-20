
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys
from bs4 import BeautifulSoup
from scrapy.selector import HtmlXPathSelector

class DmozSpider(BaseSpider):
    name = "direc_movie_mlink"
    allowed_domains = ["hindilinks4u.net"]
    f = open("direc_link") 
    
    avail_urls = f.read().replace("\n","").split(",")
    #print len(avail_urls)
    #print avail_urls
    #sys.exit()
    f.close()
    start_urls = avail_urls[:]
  
     

    def parse(self, response):
        #print response.body
        #sys.exit(0)
        start = response.url.find("=")
        director_name = response.url[start+1:]

        sel = Selector(response)
        direc_movie_mlink  = sel.xpath("/html/body/div/div[6]/ul/li").extract()
        direc_movie_mlink = str(direc_movie_mlink).strip('[]')
        soup = BeautifulSoup(direc_movie_mlink)
        movie_name_link = soup.find_all("a")
        
        for l in movie_name_link:
            movie_link = l.get("href")
            movie_name = l.get_text()
            
            
            f = open("direc_movie_mlink","a+")
            print >>f, ", ".join([director_name, movie_name, movie_link])
            print [director_name, movie_name, movie_link]
            f.close()
           
        
