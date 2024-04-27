import re
from functions import *
redundant = ['image', 'alt', 'caption', 'show-medals', 'module', 'updated',
            'url', 'publisher', 'title', 'work', 'image_size', 'imagesize', 'medals-expand']

interesting_keys = ['nickname', 'residence', 'children', 'height', 'weight', 'highlights',
'medaltemplates', 'medals','number', 'position', 'stats', 'regular_record',
'playoff_record', 'overall_record', 'disciplines', 'club', 'wcdebut', 'website', 'wcwins', 'wcpodiums', 
'wcoveralls', 'wctitles', 'olympicteams',
'olympicmedals',
'olympicgolds',
'paralympicteams',
'paralympicmedals', 
'paralympicgolds',
'worldsteams',
'worldsmedals',
'worldsgolds',
'wcseasons']


def squashMod(json_dict, key):
    # Nickname and height
    if key in ['nickname', 'height']:
        json_dict[key] = re.sub('url(.*)', '', json_dict[key])
        json_dict[key] = re.sub('title(.*)', '', json_dict[key])

    # Name and fullname
        if key in ['name', 'full_name']:
            json_dict[key] = re.sub("post-nominals","",json_dict[key])

#nfldraft
def nflMod(json_dict):
    nfl_lst = []
    for key in json_dict.keys():
        if key in ['draftyear', 'draftround', 'draftpick']:
            nfl_lst.append(key)
    lst = {}
    for key in nfl_lst:
        lst[key[5:]] = json_dict[key]
        del json_dict[key]
    if lst:
        json_dict['nfl_draft'] = lst

#suppdraft
def suppMod(json_dict):
    supp_lst = []
    for key in json_dict.keys():
        if 'suppdraft' in key:
            supp_lst.append(key)
    lst = {}
    for key in supp_lst:
        lst[key[9:]] = json_dict[key]
        del json_dict[key]
    if lst:
        json_dict['supplemental_draft'] = lst

#afldraft
def aflMod(json_dict):
    afl_lst = []
    for key in json_dict.keys():
        if 'afldraft' in key:
            afl_lst.append(key)
    lst = {}
    for key in afl_lst:
        lst[key[8:]] = json_dict[key]
        del json_dict[key]
    if lst:
        json_dict['afl_draft'] = lst

#cfldraft
def cflMod(json_dict):
    cfl_lst = []
    for key in json_dict.keys():
        if 'cfldraft' in key:
            cfl_lst.append(key)
    lst = {}
    for key in cfl_lst:
        lst[key[8:]] = json_dict[key]
        del json_dict[key]
    if lst:
        json_dict['cfl_draft'] = lst

#expansiondraft
def expMod(json_dict):
    exp_lst = []
    for key in json_dict.keys():
        if 'expansiondraft' in key:
            exp_lst.append(key)
    lst = {}
    for key in exp_lst:
        lst[key[14:]] = json_dict[key]
        del json_dict[key]
    if lst:
        json_dict['expansion_draft'] = lst
    
#statleague
def aflstatMod(json_dict):
    stats = []
    for key in json_dict.keys():
        for i in range(1,18):
            if (f'aflstatlabel{i}' in json_dict.keys() and f'aflstatvalue{i}' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))
    lst = {}
    try:
        lst['afl_season'] = json_dict['aflstatseason']
        del json_dict['aflstatseason']
    except:
        pass
    for num in stats:
        lst[json_dict[f'aflstatlabel{num}']] = json_dict[f'aflstatvalue{num}']
        del json_dict[f'aflstatlabel{num}']
        del json_dict[f'aflstatvalue{num}']
    if lst:
        json_dict['afl_stats'] = lst

#cflstatleague
def cflstatMod(json_dict):
    stats = []
    for key in json_dict.keys():
        for i in range(1,18):
            if (f'cflstatlabel{i}' in json_dict.keys() and f'cflstatvalue{i}' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))
    lst = {}
    try:
        lst['cfl_season'] = json_dict['cflstatseason']
        del json_dict['cflstatseason']
    except:
        pass
    for num in stats:
        lst[json_dict[f'cflstatlabel{num}']] = json_dict[f'cflstatvalue{num}']
        del json_dict[f'cflstatlabel{num}']
        del json_dict[f'cflstatvalue{num}']
    if lst:
        json_dict['cfl_stats'] = lst
        

#statleague
def statMod(json_dict):
    stats = []
    for key in json_dict.keys():
        for i in range(1,18):
            if (f'statlabel{i}' in json_dict.keys() and f'statvalue{i}' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))
    lst = {}
    for num in stats:
        lst[json_dict[f'statlabel{num}']] = json_dict[f'statvalue{num}']
        del json_dict[f'statlabel{num}']
        del json_dict[f'statvalue{num}']
    if lst:
        try:
            json_dict['stats_' + json_dict['statleague']] = lst
            del json_dict['statleague']
        except:
            json_dict['stats'] = lst
        

