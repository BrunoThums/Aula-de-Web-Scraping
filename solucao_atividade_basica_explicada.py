import scrapy

#opção 1: pegar todas as frases e fazer as verificações (autor e tag)
#opção 2: já verificar se o autor bate, e se sim, verificar a tag

class BuscarcSpider(scrapy.Spider):
    # Nome da spider - que você vai chamar pelo terminal (scrapy crawl nomeDaSpider)
    name = "buscarG"
    # URLs que a spider percorrerá
    start_urls = ["http://quotes.toscrape.com/tag/life/page/1/","http://quotes.toscrape.com/tag/life/page/2/"]
    # Função para realizar o "download" da página para poder raspar as informações -> é ativada automaticamente, não é preciso chamá-la
    def parse(self, response):
        # Resgata o conjunto de frases, autores e tags a partir da resposta HTTP
        conteinerFrases = response.xpath('//div//div[contains(@class,"row")][2]/div[1]/div')
        # Simples print para depuração, para verificar se realmente pegou todas frases e nada além disso
        print("###################",conteinerFrases,"###################")
        # Loop para percorrer cada frase
        for conteinerFrase in conteinerFrases:
            # Print para depuração, para verificar a frase atual
            print("Frase:",conteinerFrase)
            # Aplicação do xpath para resgatar apenas o autor desta frase
            autor_t = conteinerFrase.xpath('.//small[contains(@class,"author")]/text()').get()
            # Aplicação do xpath para resgatar todas as tags desta frase
            tag_t = conteinerFrase.xpath('.//div[contains(@class,"tags")]//a/text()').getall()
            # Print para depuração, para verificar o autor
            print("##################\n",autor_t)
            # Print para depuração, para verificar as tags
            print("##################\n",tag_t)
            # Se o autor for o Mark e tiver a tag life, então
            if(autor_t=="Mark Twain" and "life" in tag_t):
                # Print para depuração
                print("\nok\n")
                # Aplicação do xpath para resgatar a frase atual
                frase_t = conteinerFrase.xpath('.//span[contains(@class,"text")]/text()').get()
                # Salva os itens raspados em uma variável
                item = {
                    'autor': autor_t,
                    'tags': tag_t,
                    'frase': frase_t,
                }
                # Informa ao Scrapy que esta variável deve ser utilizada para exportação dos dados...
                # ...quando utilizada com as opções:
                # -o (ou -O) nomeDoArquivo.extensão (.csv .xml .json)
                yield item
