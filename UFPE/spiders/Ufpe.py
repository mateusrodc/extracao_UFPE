# -*- coding: utf-8 -*-
import scrapy
from ..items import UfpeItem
import re
from html import unescape


class UfpeSpider(scrapy.Spider):
    name = 'ufpe'
    start_urls = [
        'https://repositorio.ufpe.br/simple-search?location=123456789%2F50&query=saude+mental&rpp=10&sort_by=score&order=desc']

    def parse(self, response):
        links = response.css('td:nth-child(2) a::attr(href)').extract()
        for link in links:
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        itens = UfpeItem()

        content = unescape(response.body.decode("utf-8")).replace("\xa0", " ")

        regex_data = re.compile(
            "<td class=\"metadataFieldValue\">(?:<\s*a[^>]*>(.*?)<\s*/\s*a>)?(.*)<\s*/td>")

        data = regex_data.findall(content)
        data = ["".join(item) for item in data]

        regex_types = re.compile("<td class=\"metadataFieldLabel\">([^:]*)")

        types = regex_types.findall(content)

        for i, _type in enumerate(types):
            if _type in ['Title', 'Authors', 'Keywords', 'Abstract', 'URI']:
                itens[_type.lower()] = data[i]

        yield itens
