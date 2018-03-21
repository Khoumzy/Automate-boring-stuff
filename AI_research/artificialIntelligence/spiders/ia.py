

from artificialIntelligence.items import ArtificialintelligenceItem

import scrapy
import re

class ArtificialIntelligence(scrapy.Spider):

	name = "ia"

	# First Start Url
	start_urls = ['https://arxiv.org/list/cs.AI/recent']

	"""We have several articles spread over different pages
		This function will allow you to retrieve all 
		links that lead to these pages"""
	
	def parse(self, response):
		for href in response.xpath("//div[contains(@id, 'content')]//div[contains(@id, 'dlpage')]//small//a/@href").extract():
			# add the scheme, eg https://
			url  = "https://arxiv.org" + href
			yield scrapy.Request(url, callback=self.parse_dir_contents)


	def parse_dir_contents(self, response):

		item =  ArtificialintelligenceItem()

		item['url'] = response.xpath("//div[contains(@id, 'content')]//div[contains(@id, 'dlpage')]//dt/span[contains(@class, 'list-identifier')]/a[contains(@title, 'Download PDF')]/@href").extract()


		for url in item['url']:

			link_download = "https://arxiv.org" + url

			# Save all links in a file 
			fichier = open('../../Download/urls.txt','a')

			fichier.write(link_download + "\n")

		yield item