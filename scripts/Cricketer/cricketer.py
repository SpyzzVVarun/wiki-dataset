import re
from functions import *

redundant = ['headerstyle', 'date', 'year', 'image', 'image_size', 'alt', 'caption', 'international', 'hidedeliveries',
                       'columns']

def cricketerMod(json_dict, key):
    # Birth Date and Age
    if key == 'birth_date' or key == 'death_date':
        json_dict[key] = json_dict[key][:re.search("(?<={{)(.*?)(?=\|)",json_dict[key]).start()-2] 
        + json_dict[key][re.search("(?<={{)(.*?)(?=\|)",json_dict[key]).end()+1:-2]
        if 'df=yes' in json_dict[key]:
            json_dict[key] = re.sub('\|df=yes','',json_dict[key]).strip()
        if 'df=y' in json_dict[key]:
            json_dict[key] = re.sub('\|df=y','',json_dict[key]).strip()

    # Birth Place
    if key == 'birth_place':
        if 'full_name' in json_dict[key]:
            json_dict[key] = re.sub('\|full_name =','',json_dict[key]).strip()
            
    # Bowling
    if key == 'bowling':
        json_dict[key] = json_dict[key].strip()
        json_dict[key] = json_dict[key][:json_dict[key].rindex(' '):] + ' ' + tab_sep_alt(json_dict[key])
    
    # Nickname
    if key == 'nickname':
        json_dict[key] = json_dict[key][:re.search("(?<={{)(.*?)(?=\|)",json_dict[key]).start()-2].strip()
    
    # Top Score
    if 'top score' in key and '*' in json_dict[key] :
        json_dict[key] = json_dict[key][:-9].strip()
        
    #Website
    if key == 'website':
        json_dict[key] = re.sub('(?<=\}\}\|).*','', json_dict[key])


def columnAddendum(json_dict):
    #Column Structuring
    club_lst = []    
    for i in range(1,18):
        if f'column{i}' in json_dict.keys():
            club_lst.append(i)
    for num in club_lst:
        lst = {}
        for col in [f'matches{num}', f'runs{num}', f'bat avg{num}', f'100s/50s{num}', f'top score{num}', f'deliveries{num}', 
                    f'wickets{num}', f'bowl avg{num}',  f'fivefor{num}', f'tenfor{num}', f'best bowling{num}', f'catches/stumpings{num}']:
            try:
                lst[col[:-1]] = json_dict[col]
            except:
                pass
            try:
                del json_dict[col]
            except:
                pass
        
        
        json_dict[json_dict[f'column{num}']] = lst
        try:
            del json_dict[f'column{num}']
        except:
            pass

def clubAddendum(json_dict):
#Club Structuring
    club_lst = []    
    for i in range(1,18):
        if f'club{i}' in json_dict.keys():
            club_lst.append(i)

    lst = {}
    for num in club_lst:
        try:
            lst[json_dict[f'club{num}'] + '( ' + json_dict[f'clubnumber{num}'] + ' )'] = json_dict[f'year{num}']
        except:
            try:
                lst[json_dict[f'club{num}']] = json_dict[f'year{num}']
            except:
                try:
                    lst[json_dict[f'club{num}'] + '( ' + json_dict[f'clubnumber{num}'] + ' )'] = ''
                except:
                    lst[json_dict[f'club{num}']] = ''
        try:
            del json_dict[f'clubnumber{num}']
        except:
            pass
        
        try:
            del json_dict[f'year{num}']
        except:
            pass
        
        del json_dict[f'club{num}']
        
    json_dict['clubs'] = lst