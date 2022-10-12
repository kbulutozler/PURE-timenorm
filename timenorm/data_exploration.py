

import json
  
# Opening JSON file
f = open('/Users/bulut/timenorm-garage/PURE-timenorm-datasets/scierc_data/processed_data/json/train.json')
  
# returns JSON object as 
# a dictionary
train = json.load(f)
print(train)