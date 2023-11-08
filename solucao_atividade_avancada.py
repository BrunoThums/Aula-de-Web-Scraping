import scrapy

class BookSpider(scrapy.Spider):
    name = "book"
    start_urls = ["http://books.toscrape.com/index.html"]

    def parse(self, response):
        containerLivros = response.xpath('//ol[contains(@class,"row")]')
        links = []
        avaliacao = containerLivros.xpath('//p[contains(@class,"star-rating")]/@class').get()
        print("avaliação: ",avaliacao)
        href = containerLivros.xpath('//h3/a/@href').get()
        livro = containerLivros.xpath('//h3/a/text()').get()
        for containerLivro in containerLivros:
            if "five" in avaliacao.casefold():
                print("Achei!", livro)
                links.append(href)
        
        for link in links:
            print("entrei no link")
            yield response.follow(link, callback=self.parse_product)
        
        next_page = response.xpath('//li[contains(@class,"next")]/a/@href').get()
        print("#\n##\n##\n##\n###\n",next_page)
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        
            
        
        
    def parse_product(self, response):
        nome = response.xpath('//h1/text()').get()
        nome = nome.replace(",","")
        print("nome: ", nome)
        avaliacao = response.xpath('//p[contains(@class,"star-rating")]/@class').get()
        print("avaliacao: ", avaliacao)
        avaliacao = avaliacao.replace("star-rating ","")
        valor = response.xpath('//p[contains(@class,"price_color")]/text()').get()
        valor = valor.replace("£","")
        print("valor: ", valor)
        # Aqui tem uma trickzinha, o elemento do stock, logo abaixo do preço, parece estar bugado e não ser texto.
        # Usando o xpath abaixo podemos comprovar isto
        estoque = response.xpath('//*[contains(text(),"available")]/text()').get()
        estoque = estoque.strip().replace("In stock (","").replace(")","")
        print("estoque: ", estoque)
        print("fiz o parse")
        livro = {
            'nome':nome,
            'avaliacao':avaliacao,
            'valor (libras)':valor,
            'estoque':estoque,
        }
        print("ta aqui o livro", livro)
        yield livro



