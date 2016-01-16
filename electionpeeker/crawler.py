import collections

import requests
from lxml.html import document_fromstring


class Crawler:

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    def get_content(self):
        response = requests.get(self.url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text

    def get_document(self):
        content = self.get_content()
        document = document_fromstring(content)
        return document


class TableCrawler(Crawler):
    def crawl(self):
        document = self.get_document()
        header, *rows, footer = document.cssselect('.tableT tr')
        header_contents = [
            column.text_content() for column in header.cssselect('td')
        ]
        info_list = [
            collections.OrderedDict(zip(
                header_contents,
                (c.text_content() for c in row.cssselect('td'))
            )) for row in rows
        ]
        return info_list
