# Scrapy settings for director project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'director'

SPIDER_MODULES = ['director.spiders']
NEWSPIDER_MODULE = 'director.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'director (+http://www.yourdomain.com)'


DOWNLOADER_MIDDLEWARES = {'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
                          'director.proxy_middle.ProxyMiddleware': 120,
                         }
