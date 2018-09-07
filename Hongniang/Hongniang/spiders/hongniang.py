# -*- coding: utf-8 -*-
import scrapy
import re
from Hongniang.items import HongniangItem
pat = re.compile('(\d+)')
pat_id=re.compile('id/(\d+)')
pat_page= re.compile(r'page=(\d+)')
class HongniangSpider(scrapy.Spider):
    name = 'hongniang'
    # allowed_domains = ['hongniang.com']
    # page = 1
    url = 'http://www.hongniang.com/index/search?sort=0&wh=0&sex=0&starage=0&province=0&city=0&marriage=0&edu=0&income=0&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0&page='
    start_urls = [url+'1']
    

    def parse(self, response):
        print(response.url,response.status)
        page = int(pat_page.findall(response.url)[0])
        if response.status ==200:
            count = 0
            root = response.xpath("//li[@class='pin']")
            for each in root:
                img_num = int(each.xpath("./div[@class='pin_img']/span/text()").extract()[0])
                count+=img_num
                if img_num>0:
                    user_url = 'http://www.hongniang.com'+each.xpath("./div[@class='pin_img']/a/@href").extract()[0]
                    item = HongniangItem()
                    item['user_id'] = pat_id.findall(user_url)[0]
                    age = each.xpath("./div[@class='xx']/span[1]/text()").extract()[0]
                    item['age'] = pat.search(age).group()
                    if img_num==1:
                        image_url = each.xpath("./div[@class='pin_img']/a/img/@src").extract()
                        if 'man' in image_url[0]:
                            yield scrapy.Request(url=user_url,meta={'item':item},callback=self.parse_item)
                        else:
                            item['image_url'] = image_url
                            yield item
                            
    
                    else:
                        yield scrapy.Request(url=user_url,meta={'item':item},callback=self.parse_item)
            
            if count>0 or page<40000:

                page+=1
                next_url = self.url+str(page)
                # print(count,self.page,next_url)
                yield scrapy.Request(url=next_url,callback=self.parse)
                
        elif response.status==504:       
            yield scrapy.Request(response.url,callback=self.parse,dont_filter=True)          

    def parse_item(self,response):
        item = response.meta['item']
        image_url = response.xpath("//ul[@id='tFocus-pic']/li/img/@src").extract()
        item['image_url'] = image_url
        yield item