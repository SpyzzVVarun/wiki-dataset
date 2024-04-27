import re
from functions import *
redundant = ['image', 'alt', 'caption', 'show-medals', 'module', 'updated', 'url', 'publisher', 'title', 'work', 'image_size', 'imagesize']

interesting_keys = ['nickname', 'residence', 'children', 'height', 'weight', 'turnedpro', 'retired', 'plays',
'coach', 'racquet', 'website', 'date_of_highest_ranking', 
'medaltemplates', 'WorldOpenresult', 'event', 'highest_ranking']

timeline_keys = ['date_of_highest_ranking', 'date_of_current_ranking', 'birth_date', 'medaltemplates', 'WorldOpenresult', 'turnedpro', 'years_active']

final_timeline_keys = ['date_of_highest_ranking', 'date_of_current_ranking', 'medaltemplates', 'WorldOpenresult', 'turnedpro', 'years_active']

def squashMod(json_dict, key):
    # Nickname and height
    if key in ['nickname', 'height']:
        json_dict[key] = re.sub('url(.*)', '', json_dict[key])
        json_dict[key] = re.sub('title(.*)', '', json_dict[key])

    # Name and fullname
    if key in ['name', 'full_name']:
        json_dict[key] = re.sub("post-nominals","",json_dict[key])