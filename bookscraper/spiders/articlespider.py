import scrapy
from bookscraper.items import PokeItem 

class ExempleSpider(scrapy.Spider):
    name = 'offres'
    allowed_domains = ['labonneboite.pole-emploi.fr']
    start_urls = ['https://labonneboite.pole-emploi.fr/entreprises?j=%C3%89tudes+et+d%C3%A9veloppement+informatique&l=Valenciennes+59300&naf=&h=1&d=50&sort=smart&ij=&occupation=etudes-et-developpement-informatique&lat=50.358552&lon=3.510438&departments=']

    
    #fonction doit s'occuper de parcourir la liste des produits sur chaque page et de suivre le lien de chaque produit
    #pour obtenir plus de détails.
    def parse(self, response):
        pokemons = response.css('div.lbb-bright-container')
       
        for pokemon in pokemons: 
            nom_localisation = pokemon.css('.lbb-result__header h3 span::text').getall()
            description = pokemon.css('.lbb-result__header div.grid-col-8 h4::text').get()
            salarie_nombre = pokemon.css('.lbb-result__header div.grid-col-8 p::text').get()
            telephone = pokemon.css('div.lbb-result__details .grid-col-4 p a::text').get()
            # for pokemon in pokemons_content:
            #     telephone = pokemon.css('div.lbb-result__details .grid-col-4 p a::text').get()
                
            
            poke_item = PokeItem()
            
            poke_item['nom_localisation'] = nom_localisation
            poke_item['description'] = description
            poke_item['salarie_nombre'] = salarie_nombre
            poke_item['telephone'] = telephone

            yield poke_item

              # Pagination
            active_page = response.css('li.page-item.active').get()
            next_page_link = response.css('li.page-item.active + li a::attr(href)').get()
            
            # Si la page active n'est pas la dernière, passer à la page suivante
            if active_page and not next_page_link:
                next_page_link = response.css('li.page-item.active + li + li a::attr(href)').get()

            if next_page_link:
                next_page_url = response.urljoin(next_page_link)
                yield scrapy.Request(next_page_url, callback=self.parse)

 
