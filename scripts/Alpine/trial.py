import os
print(len(os.listdir("alpine_ski_racer-infoboxes")))

import os
import json
from constants import TEMPLATE

infobox_dir = 'C:/Users/nagpa/Infobox-Data-Alpine/alpine_ski_racer-infoboxes'

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