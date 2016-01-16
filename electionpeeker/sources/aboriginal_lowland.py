from ..crawler import TableCrawler
from ..entities import Person
from ..utils import parse_vote_count


URL = 'http://www.cec.gov.tw/zh_TW/T2/n000000000000000.html'
TOTAL_SEATS = 3


def crawl():
    crawler = TableCrawler(URL)
    info_list = crawler.crawl()
    elected_infos = sorted(info_list, key=parse_vote_count, reverse=True)
    elected = [
        Person(info['姓名'], info['推薦之政黨'])
        for info in elected_infos[:TOTAL_SEATS]
    ]
    return elected
