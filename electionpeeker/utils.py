def parse_vote_count(row):
    return int(row['得票數'].replace(',', ''))
