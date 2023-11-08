import scrapy

class BuscarcSpider(scrapy.Spider):
    name = "buscarC"
    start_urls = ["http://quotes.toscrape.com/tag/life/page/1/","http://quotes.toscrape.com/tag/life/page/2/"]
    def parse(self, response):
        conteinerFrases = response.xpath('//div//div[contains(@class,"row")][2]/div[1]/div')
        #print("###################",frases,"###################")
        for conteinerFrase in conteinerFrases:
            #print("Frase:",conteinerFrase)
            autor_t = conteinerFrase.xpath('.//small[contains(@class,"author")]/text()').get()
            tag_t = conteinerFrase.xpath('.//div[contains(@class,"tags")]//a/text()').getall()
            #print("##################\n",autor_t)
            #print("##################\n",tag_t)
            if(autor_t=="Mark Twain" and "life" in tag_t):
                #print("\nok\n")
                frase_t = conteinerFrase.xpath('.//span[contains(@class,"text")]/text()').get()
                item = {
                    'autor': autor_t,
                    'tags': tag_t,
                    'frase': frase_t,
                }
                yield item
