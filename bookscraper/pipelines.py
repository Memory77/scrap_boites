# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ExemplePipeline:
 
    def process_item(self, item, spider):

        # value = item['telephone']
        # if value == 'Modifier ces informations':
        #     value = ''


        adapter = ItemAdapter(item)
        value_tel = adapter.get('telephone')

        # if value_tel == 'Modifier ces informations':
        #     value_tel = ""

        adapter['telephone'] = [cat for cat in adapter['telephone'] if cat.lower() != 'Modifier ces informations']
        adapter['telephone'] = ''.join(adapter['telephone'])
        
        # adapter = ItemAdapter(item)
        # value_tel = adapter.get('telephone')
        # if value_tel:
        #     value_tel = value_tel.replace('tel:','') 
        #     adapter['telephone'] = int(value_tel)
        # adapter = ItemAdapter(item)
        # value_tel = adapter.get('telephone')
        # if value_tel == "Modifier ces information":
        #     value_tel = None
        # else:
        #     adapter['telephone'] = int(value_tel)
     
        return item