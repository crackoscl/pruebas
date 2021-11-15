from functools import reduce

receipts = [
    {'id': 1, 'consolidated': False},
    {'id': 2, 'consolidated': True},
    {'id': 3, 'consolidated': False},
    {'id': 4, 'consolidated': True},
    {'id': 5, 'consolidated': True},
    {'id': 6, 'consolidated': False},
]


def reducer_receipts(acc, receipts):
    key = 'consolidated' if receipts['consolidated'] else 'not_consolidated'
    acc[key].append(receipts)
    return acc


result = reduce(reducer_receipts, receipts, {
                'consolidated': [], 'not_consolidated': []})
print(result)
