import json
from collections import defaultdict

cards = json.load(open('cards.json'))

# Time - HH:MM
# H
# M M
# Time -> cards for this time

# Card art
# https://art.hearthstonejson.com/v1/render/latest/ruRU/512x/<id>.png
ans = defaultdict(list)
# millhouse = 
for card in cards:
    if card.get('type') in ['MINION', 'SPELL']:
        firstv = int(str(card.get('attack', 0)))
        secondv = int(str(card.get('health', 0)))
        key = '{}{}'.format(firstv, secondv)
        ans[key].append(card)

for k in ans.keys():
    ans[k].sort(key=lambda x: x.get('collectible', 0), reverse=True)

# for a in range(0, 12):
#     for b in range(0, 60):
#         k = '{}:{}'.format(a, b)
#         if len(ans[k]) == 0:
#             ans[k].append(millhouse)

# for c in ans['1:11']:
#     print(c)
#     print('https://art.hearthstonejson.com/v1/render/latest/ruRU/512x/{}.png'.format(c['id']))

with open('parsed_new.js', 'w') as f:
    f.write('export default ' + json.dumps(ans))