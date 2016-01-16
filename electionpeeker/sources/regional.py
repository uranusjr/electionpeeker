import requests

from ..crawler import TableCrawler
from ..entities import Person
from ..utils import parse_vote_count


TOTAL_SEATS = 1
URL_PREFIX = 'http://www.cec.gov.tw/zh_TW/T1/n'
URL_SUFFIX = '0000000000.html'


def crawl_electorate(url):
    crawler = TableCrawler(url)
    info_list = crawler.crawl()
    elected_infos = sorted(info_list, key=parse_vote_count, reverse=True)
    elected = [
        Person(info['姓名'], info['推薦之政黨'])
        for info in elected_infos[:TOTAL_SEATS]
    ]
    return elected


def crawl():
    """Crawl each URL for regional election results.

    The URLs are generated based on logic found in
    ``http://www.cec.gov.tw/zh_TW/js/treeT.js``. The basic idea is:

    * lv1 is a single-digit integer. 1 is Taipei, 2 is New Taipei, etc.

    * lv2 and lv3 indicates the electorate. I'm not sure how exactly they are
      different, but there seems to be two patterns:

        1. In municipalities, lv2 is always 0. lv3 is the electorate number.
        2. All counties share lv1 7 (Taiwan) and 8 (Fujian), while lv2
           (never 0) indicates the county or city, lv3 the electorate number.

    Numbers are tried sequentially, carrying up if a URL returns 404.
    """
    elected_list = []
    for lv1 in range(10):
        lv2 = 0
        while True:
            lv3 = 1
            while True:
                url = '{prefix}{lv1}{lv2:0>2}{lv3:0>2}{suffix}'.format(
                    prefix=URL_PREFIX, suffix=URL_SUFFIX,
                    lv1=lv1, lv2=lv2, lv3=lv3,
                )
                try:
                    elected = crawl_electorate(url)
                except requests.HTTPError:
                    break
                else:
                    elected_list.extend(elected)
                lv3 += 1
            if lv2 > 0 and lv3 == 1:
                break
            lv2 += 1
        if lv2 == 0:
            break
    return elected_list
