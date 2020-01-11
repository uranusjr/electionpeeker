from ..crawler import TableCrawler
from ..entities import Party
from ..utils import parse_vote_count


URL = 'https://www.cec.gov.tw/pc/zh_TW/L4/n00000000000000000.html'
TOTAL_SEATS = 34


def calculate_round_1(vote_counts):
    total_vote_count = sum(vote_counts.values())
    result = sorted(
        ((name, TOTAL_SEATS * vote_count / total_vote_count)
         for name, vote_count in vote_counts.items()),
        key=lambda r: r[1] % 1, reverse=True,
    )
    return result


def calculate_round_2(round_1_result):
    remaining = TOTAL_SEATS - sum(int(row[1]) for row in round_1_result)
    result = [
        Party(name, int(count) + 1)
        for name, count in round_1_result[:remaining]
    ] + [
        Party(name, int(count))
        for name, count in round_1_result[remaining:]
    ]
    return result


def crawl():
    crawler = TableCrawler(URL)
    info_list = crawler.crawl()
    vote_counts = {
        info['政黨']: parse_vote_count(info)
        for info in info_list if float(info['得票率%']) >= 5.0
    }
    round_1_result = calculate_round_1(vote_counts)
    final_result = calculate_round_2(round_1_result)
    return final_result
