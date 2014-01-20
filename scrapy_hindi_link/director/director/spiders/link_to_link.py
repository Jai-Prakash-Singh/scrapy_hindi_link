

# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


from random import choice
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys
from bs4 import BeautifulSoup

from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import re
from selenium import selenium
import time
import sys

ip_list = ["117.41.182.188:8080", "189.85.65.30:8080", "210.101.131.232:8080", "190.36.27.195:8080",
          "41.221.216.237:8080","94.154.222.127:8080", "184.168.55.226:80", "194.141.96.229:8080"]



class DmozSpider(BaseSpider):
    name = "link_to_link"

    allowed_domains = ["hindilinks4u.net"]
    f = open("movie2_watch_link")
    start_urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(f.read())) 
    f.close()

    #start_urls = ['http://www.filmshowonline.net/videos/149965/']

    def __init__(self):
        #ip_port = choice(ip_list)
        #prox = "--proxy=%s"%ip_port
        #service_args = [prox,'--proxy-type=socks5',]
        #self.driver = webdriver.PhantomJS(service_args =service_args)
        self.driver = webdriver.PhantomJS()
        

    def __del__(self):
        self.driver.close()


     

    def parse(self, response):
        
        driver = self.driver
        wait = WebDriverWait(driver, 3)
        driver.get(str(response.url))
 
        wait.until(lambda driver: driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td"))

        try:
            data = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td")
            result = data.find_element_by_tag_name("iframe").get_attribute("src")
            #driver.close()

        except:
            data = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td")
            result = data.find_element_by_tag_name("embed").get_attribute("src")
           
        f = open("link_2_link", "a+")
        print >>f, ','.join([str(response.url), result])
        print str(response.url), result

