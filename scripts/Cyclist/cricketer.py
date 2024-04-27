import re
from functions import *
redundant = ['image', 'alt', 'caption', 'show-medals', 'module', 'updated', 'url', 'publisher', 'title', 'work', 'image_size', 'imagesize']

# interesting_keys = ['nickname', 'residence', 'children', 'height', 'weight', 'turnedpro', 'retired', 'plays',
# 'coach', 'racquet', 'website', 'date_of_highest_ranking', 
# 'medaltemplates', 'WorldOpenresult', 'event', 'highest_ranking']

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

def addMod(json_dict):
    cyclist_lst = []    
    for i in range(1,18):
        if (f'proyears{i}' in json_dict.keys() and f'proteam{i}' in json_dict.keys()):
            cyclist_lst.append(i)

    lst = {}
    for num in cyclist_lst:
        try:
            lst[json_dict[f'proteam{num}']] = json_dict[f'proyears{num}']
        except:
            pass
                
        try:
            del json_dict[f'proteam{num}']
        except:
            pass
        
        try:
            del json_dict[f'proyears{num}']
        except:
            pass
        
    if lst:
        json_dict['pro_career'] = lst
        
    cyclist_lst = []    
    for i in range(1,18):
        if (f'amateurteam{i}' in json_dict.keys() and f'amateuryears{i}' in json_dict.keys()):
            cyclist_lst.append(i)

    lst = {}
    for num in cyclist_lst:
        try:
            lst[json_dict[f'amateurteam{num}']] = json_dict[f'amateuryears{num}']
        except:
            pass
                
        try:
            del json_dict[f'amateurteam{num}']
        except:
            pass
        
        try:
            del json_dict[f'amateuryears{num}']
        except:
            pass
        
    if lst:
        json_dict['am_career'] = lst
        
    cyclist_lst = []    
    for i in range(1,18):
        if (f'manageteam{i}' in json_dict.keys() and f'manageyears{i}' in json_dict.keys()):
            cyclist_lst.append(i)

    lst = {}
    for num in cyclist_lst:
        try:
            lst[json_dict[f'manageteam{num}']] = json_dict[f'manageyears{num}']
        except:
            pass
                
        try:
            del json_dict[f'manageteam{num}']
        except:
            pass
        
        try:
            del json_dict[f'manageyears{num}']
        except:
            pass
        
    if lst:
        json_dict['manage_career'] = lst