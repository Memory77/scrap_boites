# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ExemplePipeline:
 
    def process_item(self, item, spider):
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