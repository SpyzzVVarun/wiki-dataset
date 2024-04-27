# import os
# from constants import TEMPLATE
# print(len(os.listdir(f"{TEMPLATE}-infoboxes")))

import os
import json
from constants import TEMPLATE

infobox_dir = f'C:/Users/nagpa/Infobox-Data-Baseball/{TEMPLATE}-infoboxes'

empty_infobox_count = 0


count = 0
total_count = 0
for entity in os.listdir(infobox_dir):
    total_count += 1
    entity_path = os.path.join(infobox_dir, entity)
    try:
        with open(entity_path, 'r') as json_file:
            data = json.load(json_file)
            if data == {}:
                count += 1
    except:
        count += 1

print(TEMPLATE, total_count, count)