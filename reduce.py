from functools import reduce
from collections import defaultdict

receipts = [
    {'id': 1, 'consolidated': False},
    {'id': 2, 'consolidated': True},
    {'id': 3, 'consolidated': False},
    {'id': 4, 'consolidated': True},
    {'id': 5, 'consolidated': True},
    {'id': 6, 'consolidated': False},
]

# EJEMPLO 1 tiempo = 4.521000000000386e-06
def reducer_receipts(acc, receipts):
    key = 'consolidated' if receipts['consolidated'] else 'not_consolidated'
    acc[key].append(receipts)
    return acc


def separate_receipts_one(receipts) -> dict:
    return reduce(reducer_receipts, receipts, {
        'consolidated': [], 'not_consolidated': []})


# EJEMPLO 2  tiempo = 3.1739999999981505e-06
def separate_receipts_two(receipts) -> dict:
    receipts_dict = {'consolidated': [], 'not_consolidated': []}
    for receipt in receipts:
        if receipt['consolidated']:
            receipts_dict['consolidated'].append(receipt)
        else:
            receipts_dict['not_consolidated'].append(receipt)
    return receipts_dict


# EJEMPLO 3 tiempo = 4.065000000001012e-06
def separate_receipts_three(receipts) -> dict:
    return{
        'consolidated': [receipt for receipt in receipts if receipt.get('consolidated')],
        'not_consolidated': [receipt for receipt in receipts if not receipt.get('consolidate')]
    }



# EJEMPLO 4 time = 6.349999999998718e-06
def separate_receipts_four(receipts):
    receipts_dict = defaultdict(list)
    for receipt in receipts:
        if receipt['consolidated']:
            receipts_dict['consolidated'].append(receipt)
        else:
            receipts_dict['not_consolidated'].append(receipt)
    return receipts_dict



# EJEMPLO 5 tiempo = 6.466999999999584e-06
def separate_receipts_five(receipts):

    receipts_dict = defaultdict(list)
    for receipt in receipts:
        key = 'consolidated' if receipt['consolidated'] else 'not_consolidated'
        receipts_dict[key].append(receipt)
    return receipts_dict



# EJEMPLO 6 time = 3.825999999998442e-06
def separate_receipts_six(receipts):
    receipts_dict = {}
    for receipt in receipts:
        key = 'consolidated' if receipt['consolidated'] else 'not_consolidated'
        receipts_dict.setdefault(key, []).append(receipt)
    return receipts_dict


print(separate_receipts_six(receipts))
