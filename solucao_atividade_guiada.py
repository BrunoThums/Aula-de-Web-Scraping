import scrapy

class BuscarcSpider(scrapy.Spider):
    name = "buscarG"
    allowed_domains = ["quotesto.scrape.com"]
    start_urls = ["http://quotes.toscrape.com/tag/simile/"]
    global autor, frase
    global tags
    def parse(self, response):
        frases = response.xpath('//div//div[contains(@class,"row")][2]/div[1]/div')
        print("###################",frases,"###################")
        for frase in frases:
            print("Frase:",frase)
            autor_t = frase.xpath('.//small[contains(@class,"author")]/text()').get()
            tag_t = frase.xpath('.//div[contains(@class,"tags")]//a/text()').getall()
            print("##################\n",autor_t)
            print("##################\n",tag_t)
            if( "simile" in tag_t):
                print("\nok\n")
                frase_t = frase.xpath('.//span[contains(@class,"text")]/text()').get()
                item = {
                    'autor': autor_t,
                    'tags': tag_t,
                    'frase': frase_t,
                }
                yield item