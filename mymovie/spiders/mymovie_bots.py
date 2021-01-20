import scrapy
from mymovie.items import MymovieItem

def remove_space(descs:list) -> list:
    result = []
    #공백 제거
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0:
            result.append(descs[i].strip())
    return result
class MymovieBotsSpider(scrapy.Spider):
    name = 'mymovie_bots'
    allowed_domains = ['naver.com']
    start_urls = ['http://movie.naver.com/movie/point/af/list.nhn']

    def parse(self, response):
        titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        stars = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        descs = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/text()').extract()
        converted_descs = remove_space(descs)
        writers = response.css('.author::text').extract()
        dates = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()
        
        items = []
        for i in range(len(titles)):
            item = MymovieItem()
            item['title'] = titles[i]
            item['star'] = stars[i]
            item['desc'] = converted_descs[i]
            item['writer'] = writers[i]
            item['date'] = dates[i]
            
            yield item
            # print(item)
        #     items.append(item)
        # return items