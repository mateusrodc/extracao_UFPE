# -*- coding: utf-8 -*-
import scrapy
from ..items import UfpeItem


class AranhaSpider(scrapy.Spider):
    name = 'aranha'
    #allowed_domains = ['https://repositorio.ufpe.br']
    start_urls = ['https://repositorio.ufpe.br/simple-search?location=123456789%2F50&query=saude+mental&rpp=10&sort_by=score&order=desc']

    def parse(self, response):
        lista = response.css('td:nth-child(2) a::attr(href)').extract()
        next_page= response.css('.pagination li:last-child a::attr(href)').get()
        for link in lista:
            yield response.follow(link, self.Artigo)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def Artigo(self,response):
        itens= UfpeItem()
        titulo = response.css(':nth-child(3) tr:nth-child(1) td.metadataFieldValue::text').extract()
        resumo = response.css(':nth-child(3) tr:nth-child(6) td.metadataFieldValue::text').extract()
        
        
        itens['titulo']=titulo
        itens['resumo']=resumo
        
        

        yield itens
