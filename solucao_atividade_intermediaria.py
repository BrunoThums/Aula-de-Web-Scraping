import scrapy


class HockeySpider(scrapy.Spider):
    name = "hockey"
    start_urls = ["http://www.scrapethissite.com/pages/forms/"]

    def parse(self, response):
        containerTimes = response.xpath('//tr[contains(@class,"team")]')
        timeGFGS = []
        for containerTime in containerTimes:
            time = containerTime.xpath('.//td[contains(@class,"name")]/text()').get()
            golsFeitos = containerTime.xpath('.//td[contains(@class,"gf")]/text()').get()
            golsSofridos = containerTime.xpath('.//td[contains(@class,"ga")]/text()').get()
            if(int(golsFeitos)>300 and int(golsSofridos)<220):
                timeGFGS.append((time.strip(),golsFeitos.strip(),golsSofridos.strip()))
        next_page = containerTime.xpath('//a[contains(@aria-label,"Next")]/@href').get()
        print("#\n##\n##\n##\n###\n",next_page)
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        timeGFGS = sorted(timeGFGS,key=lambda x: float(x[1]), reverse=True)
        for time, golsfeitos, golssofridos in timeGFGS:    
            item = {
                'time': time,
                'golsFeitos': golsfeitos,
                'golsSofridos': golssofridos,
                }
            yield item

