receipts = [
  { 'id': 1, 'consolidated': False },
  { 'id': 2, 'consolidated': True },
  { 'id': 3, 'consolidated': False },
  { 'id': 4, 'consolidated': True },
  { 'id': 5, 'consolidated': False },
  { 'id': 6, 'consolidated': True },
];

def reducer_list(receipts):
    receipts_dict = {'consolidated':[],'not_consolidated':[]}
    for receipt in receipts:
        if receipt['consolidated'] == True:
            receipts_dict['consolidated'].append(receipt)
        elif receipt['consolidated'] == False:
            receipts_dict['not_consolidated'].append(receipt)
    return receipts_dict
        
        
print(reducer_list(receipts))
