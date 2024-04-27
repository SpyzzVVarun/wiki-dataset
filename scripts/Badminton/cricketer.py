import re
from functions import *
redundant = ['image', 'alt', 'caption', 'show-medals', 'module', 'updated', 'url', 'publisher', 'title', 'work', 'image_size', 'imagesize', 'medals-expand']
interesting_keys = ['nickname', 'residence', 'children', 'height', 'weight', 'turnedpro', 'retired', 'plays',
'coach', 'racquet', 'website', 'highest_ranking_date', 'current_ranking_date', 'current_ranking', 
'medaltemplates', 'WorldOpenresult', 'event', 'highest_ranking', 'career_record', 'titles', 'played', 'medals', 'years_active']


def keyMod(json_dict, key):
    # Nickname and height
    if key in ['nickname', 'height']:
        json_dict[key] = re.sub('url(.*)', '', json_dict[key])
        json_dict[key] = re.sub('title(.*)', '', json_dict[key])
    
    if key in ['nickname', 'height', 'birth_place', 'weight', 'trainer', 'names', 'billed',
                  'debut', 'retired', 'campus_size', 'students', 'endowment', 'vice_chancellor',
                   'religious_affiliation', 'academic_affiliations', 'president']:
        json_dict[key] = re.sub('url(.*)', '', json_dict[key])
        json_dict[key] = re.sub('https(.*)', '', json_dict[key])
        json_dict[key] = re.sub('title(.*)', '', json_dict[key])

    # Name and fullname
        if key in ['name', 'full_name']:
            json_dict[key] = re.sub("post-nominals","",json_dict[key])
        

