# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PokeItem(scrapy.Item):
    nom_localisation = scrapy.Field()
    description = scrapy.Field()
    salarie_nombre = scrapy.Field()
    telephone = scrapy.Field()


  
