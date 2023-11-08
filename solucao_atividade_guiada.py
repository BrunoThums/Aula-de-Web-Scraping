import scrapy

class BuscarcSpider(scrapy.Spider):
    name = "buscarG"
    start_urls = ["http://quotes.toscrape.com/tag/simile/"]
    def parse(self, response):
        conteinerFrases = response.xpath('//div//div[contains(@class,"row")][2]/div[1]/div')
        print("###################",conteinerFrases,"###################")
        for conteinerFrase in conteinerFrases:
            print("Frase:",conteinerFrase)
            autor_t = conteinerFrase.xpath('.//small[contains(@class,"author")]/text()').get()
            tag_t = conteinerFrase.xpath('.//div[contains(@class,"tags")]//a/text()').getall()
            print("##################\n",autor_t)
            print("##################\n",tag_t)
            if( "simile" in tag_t):
                print("\nok\n")
                frase_t = conteinerFrase.xpath('.//span[contains(@class,"text")]/text()').get()
                item = {
                    'autor': autor_t,
                    'tags': tag_t,
                    'frase': frase_t,
                }
                yield item
