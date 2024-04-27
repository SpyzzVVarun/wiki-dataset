import re
from functions import *
redundant = [
"embed", 
"image", 
"image_size", 
"alt", 
"caption", 
"height_footnote", 
"weight_footnote", 
]

interesting_keys =[
"team", 
"number", 
"position", 
"league", 
"conference",
"death_date", 
"death_place", 
"height_ft", 
"height_in", 
"height_cm", 
"height_order",
"weight_lb", 
"weight_kg", 
"weight_order",  
"high_school", 
"college", 
"draft_year", 
"draft_round", 
"draft_pick", 
"draft_team", 
"draft_league", 
"career_start", 
"career_end", 
"career_position", 
"career_number", 
"coach_start", 
"coach_end", 
"referee_start", 
"referee_end", 
"years1", 
"team1", 
"years2", 
"team2", 
"years3", 
"team3", 
"years4", 
"team4", 
"years5", 
"team5", 
"years6", 
"team6", 
"years7", 
"team7", 
"years8", 
"team8", 
"years9", 
"team9", 
"years10", 
"team10", 
"years11", 
"team11", 
"years12", 
"team12", 
"years13", 
"team13", 
"years14", 
"team14", 
"years15", 
"team15", 
"years16", 
"team16", 
"years17", 
"team17", 
"years18", 
"team18", 
"years19", 
"team19", 
"years20", 
"team20", 
"years21", 
"team21", 
"years22", 
"team22", 
"years23", 
"team23", 
"years24", 
"team24", 
"years25", 
"team25", 
"years26", 
"team26", 
"years27", 
"team27", 
"years28", 
"team28", 
"years29", 
"team29", 
"years30", 
"team30", 
"years31", 
"team31", 
"years32", 
"team32", 
"years33", 
"team33", 
"years34", 
"team34", 
"years35", 
"team35", 
"years36", 
"team36", 
"years37", 
"team37", 
"years38", 
"team38", 
"years39", 
"team39", 
"years40", 
"team40", 
"cyears1", 
"cteam1", 
"cyears2", 
"cteam2", 
"cyears3", 
"cteam3", 
"cyears4", 
"cteam4", 
"cyears5", 
"cteam5", 
"cyears6", 
"cteam6", 
"cyears7", 
"cteam7", 
"cyears8", 
"cteam8", 
"cyears9", 
"cteam9", 
"cyears10", 
"cteam10", 
"cyears11", 
"cteam11", 
"cyears12", 
"cteam12", 
"cyears13", 
"cteam13", 
"cyears14", 
"cteam14", 
"cyears15", 
"cteam15", 
"cyears16", 
"cteam16", 
"cyears17", 
"cteam17", 
"cyears18", 
"cteam18", 
"cyears19", 
"cteam19", 
"cyears20", 
"cteam20", 
"highlights", 
"stat1label", 
"stat1value", 
"stat2label", 
"stat2value", 
"stat3label", 
"stat3value", 
"stats_league", 
"bbr", 
"bbr_wnba", 
"nbanew", 
"wnba_profile", 
"cstats_league1", 
"cwin1", 
"closs1", 
"cstats_league2", 
"cwin2", 
"closs2", 
"cstats_league3", 
"cwin3", 
"closs3", 
"cstats_league4", 
"cwin4", 
"closs4", 
"cstats_league5", 
"cwin5", 
"closs5", 
"HOF", 
"HOF_player", 
"HOF_coach", 
"womensHOF", 
"FIBA_HOF_player", 
"CBBASKHOF_year", 
"medal_templates", 
]








def squashMod(json_dict, key):
    # Nickname and height
    if key in ['nickname', 'height', 'birth_place', 'weight', 'trainer', 'names', 'billed',
                'debut', 'retired', 'campus_size', 'students', 'endowment', 'vice_chancellor', 
                'religious_affiliation',]:
        json_dict[key] = re.sub('url(.*)', '', json_dict[key])
        json_dict[key] = re.sub('https(.*)', '', json_dict[key])
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
    llst = []    
    for i in range(1,41):
        if (f'years{i}' in json_dict.keys() and f'team{i}' in json_dict.keys()):
            llst.append(i)

    lst = {}
    for num in llst:
        try:
            lst[json_dict[f'team{num}']] = json_dict[f'years{num}']
        except:
            pass
                
        try:
            del json_dict[f'team{num}']
        except:
            pass
        
        try:
            del json_dict[f'years{num}']
        except:
            pass
        
    if lst:
        json_dict['teams'] = lst
        
    llst = []    
    for i in range(1,41):
        if (f'cyears{i}' in json_dict.keys() and f'cteam{i}' in json_dict.keys()):
            llst.append(i)

    lst = {}
    for num in llst:
        try:
            lst[json_dict[f'cteam{num}']] = json_dict[f'cyears{num}']
        except:
            pass
                
        try:
            del json_dict[f'cteam{num}']
        except:
            pass
        
        try:
            del json_dict[f'cyears{num}']
        except:
            pass
        
    if lst:
        json_dict['cteams'] = lst
        
    stats = []
    for key in json_dict.keys():
        for i in range(1,7):
            if (f'stat{i}label' in json_dict.keys() and f'stat{i}value' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))
    lst = {}
    for num in stats:
        lst[json_dict[f'stat{num}label']] = json_dict[f'stat{num}value']
        del json_dict[f'stat{num}label']
        del json_dict[f'stat{num}value']
    if lst:
        if('stats_league' in list(json_dict.keys())):
            json_dict[json_dict['stats_league']] = lst
            del json_dict['stats_league']
        else:
            json_dict['stats'] = lst
            
    stats = []
    for key in json_dict.keys():
        for i in range(1,7):
            if (f'cstats_league{i}' in json_dict.keys() and f'cwin{i}' in json_dict.keys() and  f'closs{i}' in json_dict.keys()):
                stats.append(i)
    stats = list(set(stats))

    for num in stats:
        lst = {}
        lst["win"] =  json_dict[f'cwin{num}']
        lst["loss"] =  json_dict[f'closs{num}']
        del json_dict[f'cwin{num}']
        del json_dict[f'closs{num}']
        if lst:
            json_dict['c' + json_dict[f'cstats_league{num}']] = lst
        



