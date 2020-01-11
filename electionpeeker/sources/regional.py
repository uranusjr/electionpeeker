import re

import requests

from ..crawler import TableCrawler
from ..entities import Person
from ..utils import parse_vote_count


TOTAL_SEATS = 1
URL_PREFIX = 'https://www.cec.gov.tw/pc/zh_TW/L1/n'
URL_SUFFIX = '.html'


def crawl_electorate(url):
    crawler = TableCrawler(url)
    info_list = crawler.crawl()
    elected_infos = sorted(info_list, key=parse_vote_count, reverse=True)
    elected = [
        Person(info['姓名'], info['推薦之政黨'])
        for info in elected_infos[:TOTAL_SEATS]
    ]
    return elected


def iter_areas():
    """Crawl back area IDs.

    Areas are declared in ``https://www.cec.gov.tw/pc/zh_TW/js/treeT.js``.
    Use regex to match ``thrAreaID`` assignments.
    """
    pattern = re.compile(r'^thrAreaID\[\d+\]\[\d+\]\[0\]=\'(\d+)\';$')
    source = 'https://www.cec.gov.tw/pc/zh_TW/js/treeT.js'
    resp = requests.get(source)
    for line in resp.text.splitlines():
        match = pattern.match(line.strip())
        if not match:
            continue
        yield match.group(1)



def crawl():
    """Crawl each URL for regional election results.
    """
    elected_list = []
    for code in iter_areas():
        url = '{prefix}{code}{suffix}'.format(
            prefix=URL_PREFIX, suffix=URL_SUFFIX, code=code,
        )
        elected = crawl_electorate(url)
        elected_list.extend(elected)
    return elected_list
