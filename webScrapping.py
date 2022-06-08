import scrapy


#Para instalar Scrappy:
#pip install scrapy

#Para instalar Steemer:
#pip install pystemmer

'''ignore_list= ["", ".", ";", "+", "-", "(", ")", ":" , "[", "]", "-", "<", ">", "_", "'", "?", "!","{", "}", "^", "+", "#", "$", "%", "&", "/", "*", '"', "«", "»"
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "el", "de", "la", "las", "los", "para", "con", "a", "como" "por", "sin", "tras"]'''


#titles_list = []
#subtitles_list = []
#img_alt_list = []
#img_src_list= []
#ref_list = []



class ScrappySpider(scrapy.Spider):
    name = 'wikiSpider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Mario_(franchise)']
    

    def parse(self, response):
        #stemmer = Stemmer.Stemmer('spanish')
        print('=====> Parseando la página: ' + response.url)       
        
        #Parseo de próxima página:

        next_urls = response.css('a::attr(href)').getall()
        for next_url in next_urls:
            if next_url is not None:
                yield scrapy.Request(response.urljoin(next_url))

        yield {
            
            #'Page' : response.url,                                                  #Scrapping del URL de la página
            'Title' : response.css('title ::text').getall(),                        #Título de la Página  #Scrapping de Titulos "Title" de una página
            'Subtitles' : response.css('.mw-headline::text').getall(),              #Scrapping de Subtitulos "h2" de una página
            'Image-alt-text' : response.css('img').xpath('@alt').getall(),          #Scrapping de texto Alt de imagenes "img" de una página
            'Image-src-text' : response.css('img').xpath('@src').getall(),          #Scrapping de texto Source de imagenes "src" de una página
            'References' : response.css('span.reference-text ::text').getall(),     #Scrapping de referencias ".reference-text" de una página
            #Scrapping de tags ".tag" de una página:

        }

        #Scrapping de Titulos "Title" de una página:
        #titles = response.css('title::text').getall()
        '''titles = response.css('.mw-first-heading::text').getall()
        for title in titles:
            if title is not titles_list:
                titles_list.append(title)
                print("==================== " + title)'''
                

        #Scrapping de Subtitulos "h2" de una página:
        '''subtitles = response.css('.mw-headline::text').getall()
        
        for subtitle in subtitles:
            if subtitle is not subtitles_list:
                subtitles_list.append(subtitle)
                #print(subtitle)'''


        #Scrapping de texto Alt de imagenes "img" de una página:
        '''img_alts = response.css('img').xpath('@alt').getall()
        
        for alt in img_alts:
            if alt is not img_alt_list:
                img_alt_list.append(alt)
                #print("==================== " + alt)'''

        #Scrapping de texto Source de imagenes "src" de una página:
        '''img_src = response.css('img').xpath('@src').getall()
        for src in img_src:
            if src is not img_src_list:
                img_src_list.append(src)
                #print("==================== " + src)'''

        #Scrapping de referencias ".reference-text" de una página:
        '''refs= response.css('span.reference-text ::text').getall()
        for ref in refs:
            if ref is not ref_list:
                ref_list.append(ref)
                print("==================== " + ref)'''



        #Scrapping de tags ".tag" de una página:
        ''' refs= response.css('tag ::text').getall()
        for ref in refs:
            if ref is not ref_list:
                if ref != "" or ref == "." or ref == " ":      # ===================================== Filtrar valores
                    ref_list.append(ref)
                    #print("==================== " + ref)'''
        

        
               
    '''def returnLists():
        return titles_list #, subtitles_list, img_alt_list, img_src_list,ref_list'''
        
               
    
        
