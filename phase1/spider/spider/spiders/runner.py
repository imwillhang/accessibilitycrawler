# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class RunnerSpider(scrapy.Spider):
    name = 'runner'
    allowed_domains = [
    	# 'cosmopolitan.com',
    	'engadget.com'
    	# 'espn.com', 
    	# 'nba.com'
    ]
    start_urls = [
    	#'http://www.cosmopolitan.com/',
        'https://www.engadget.com/'
    	# 'https://www.espn.com/', 
    	# 'https://www.nba.com/'
    ]
	
    def parse(self, response):
        links = response.css('a::attr(href)').extract()
        imgs = response.css('img').extract()
        for image in imgs:
        	soup = BeautifulSoup(image, 'html.parser')
        	has_alt = 'alt' in soup.img and len(soup.img['alt']) > 1
        	yield {
        		'has_alt': has_alt,
        		'src': soup.img['src'],
        		'page': response.url
        	}
        print(response.url)
        for next_page in links:
        	#if 'video' not in next_page and 'comments' not in next_page:
        	yield response.follow(next_page, callback=self.parse)