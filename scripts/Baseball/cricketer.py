import re
from functions import *
redundant = ['image', 'alt', 'caption', 'show-medals', 'module', 'updated', 'url', 'publisher', 'title', 'work', 'image_size', 'imagesize',
             'show-medals', 'update', '']

interesting_keys = ['nickname', 'residence', 'children', 'weight_lb', 'pastcoaching', 'current_team',
'pastexecutive', 'status', 'cflstatus', 'highlights', 'draftyear', 'draftround', 'draftpick', 'nfl_draft',
'medaltemplates', 'pastteams', 'pastadmin', 'number', 'position', 'supplemental_draft', 'afl_draft', 'cfl_draft', 'stats', 'regular_record',
'playoff_record', 'overall_record', 'nfl', 'expansion_draft', 'team', 'number', 'position', 'positionplain',
'bats', 'throws', 'statleague', 
'statyear', 'stat1label', 'stat1value', 'stat2label', 'stat2value', 'stat3label', 'stat3value'
,'stat4label'
,'stat4value'
,'stat5label'
,'stat5value','stat6label','stat6value','stat7label','stat7value','stat2league' ,'stat2year' ,'stat21label' ,'stat21value'
,'stat22label'
,'stat22value'
,'stat23label'
,'stat23value'
,'stat24label'
,'stat24value'
,'stat25label'
,'stat25value'
,'stat26label'
,'stat26value'
,'stat27label'
,'stat27value'
,'stat3league'
,'stat3year'
,'stat31label'
,'stat31value'
,'stat32label'
,'stat32value'
,'stat33label'
,'stat33value'
,'stat34label'
,'stat34value'
,'stat35label'
,'stat35value'
,'stat36label'
'stat36value', 'stat37label' ,'stat37value', 'statMyear', 'formerteams', 'managerwins', 'managerlosses',
'managerties', 'teams']


def squashMod(json_dict, key):
    # Nickname and height
    if key in ['nickname', 'height']:
        json_dict[key] = re.sub('url(.*)', '', json_dict[key])
        json_dict[key] = re.sub('title(.*)', '', json_dict[key])

    # Name and fullname
    if key in ['name', 'full_name']:
        json_dict[key] = re.sub("post-nominals","",json_dict[key])

    if key in ['nickname', 'height', 'birth_place', 'weight', 'trainer', 'names', 'billed',
                  'debut', 'retired', 'campus_size', 'students', 'endowment', 'vice_chancellor',
                   'religious_affiliation', 'academic_affiliations', 'president']:
            json_dict[key] = re.sub('url(.*)', '', json_dict[key])
            json_dict[key] = re.sub('https(.*)', '', json_dict[key])
            json_dict[key] = re.sub('title(.*)', '', json_dict[key])

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
        for i in range(1,8):
            if (f'stat{i}label' in json_dict.keys() and f'stat{i}value' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))
    lst = {}
    for num in stats:
        lst[json_dict[f'stat{num}label']] = json_dict[f'stat{num}value']
        del json_dict[f'stat{num}label']
        del json_dict[f'stat{num}value']
    if lst:
        if('statleague' in list(json_dict.keys())):
            json_dict[json_dict['statleague']] = lst
            del json_dict['statleague']
        else:
            json_dict['stats'] = lst

    stats = []
    for key in json_dict.keys():
        for i in range(1,8):
            if (f'stat2{i}label' in json_dict.keys() and f'stat2{i}value' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))
    lst = {}
    for num in stats:
        lst[json_dict[f'stat2{num}label']] = json_dict[f'stat2{num}value']
        del json_dict[f'stat2{num}label']
        del json_dict[f'stat2{num}value']
    if lst:
        if('stat2league' in list(json_dict.keys())):
            json_dict[json_dict['stat2league']] = lst
            del json_dict['stat2league']
        else:
            json_dict['stats2'] = lst
            
    stats = []
    for key in json_dict.keys():
        for i in range(1,8):
            if (f'stat3{i}label' in json_dict.keys() and f'stat3{i}value' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))
    lst = {}
    for num in stats:
        lst[json_dict[f'stat3{num}label']] = json_dict[f'stat3{num}value']
        del json_dict[f'stat3{num}label']
        del json_dict[f'stat3{num}value']
    if lst:
        if('stat3league' in list(json_dict.keys())):
            json_dict[json_dict['stat3league']] = lst
            del json_dict['stat3league']
        else:
            json_dict['stats3'] = lst
        

