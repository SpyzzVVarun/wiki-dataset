from driver import driver
from selenium.webdriver.common.by import By
import re
from mwparserfromhell import parse
import os
import json
from functions import *
from cricketer import *
from constants import XPATH, TEMPLATE

with open("titles.txt", "r") as f:
    text = f.read()
    titles = text.split("\n")
    f.close()


for page_title in titles:
    try:
        if(os.path.exists(f'{TEMPLATE}-infoboxes/{page_title}')):
            continue
        json_dict = dict()
        global_lst = []
        championship_years = {}
        birth_date = ''
        url = f'https://en.wikipedia.org/w/index.php?title={page_title}&action=history&action=raw'
        driver.get(url)
        page =  replace_newlines(remove_comments(driver.find_element(By.XPATH,XPATH).text))
        temp = replace_special(re.findall('(?<=\{\{Infobox)(.*)',replace_newlines(page))[0])
        # Figuring out where }} ends to mark end of infobox
        i=2
        infobox = ''
        for char in temp:
            if (i==0):
                break
            infobox = infobox + char
            if char=='{':
                i = i+1
            elif char=='}':
                i = i-1
        try:
            infobox = infobox.split('medaltemplates')[0] + 'medaltemplates' + infobox.split('medaltemplates')[1].replace(' | ','|')
        except:
            pass
        try:
            infobox = infobox.split('medal_templates')[0] + 'medal_templates' + infobox.split('medal_templates')[1].replace(' | ','|')
        except:
            pass
        for key_value in re.findall('\^(.*?)ZXC',replace_tabs(infobox+' | ')):
            try:
                key = key_value.split('=')[0]
                value = '='.join(key_value.split('=')[1:])
                if value.strip() == '':
                    key = key_value.split(': ')[0]
                    value = ': '.join(key_value.split(':')[1:])
                if value.strip() == '':
                    key = key_value.split('=')[0]
                    value = '='.join(key_value.split('=')[1:])
                # Do i need these strips??
                key = key.strip()
                if ("medal" in key) and ("show" not in key):
                    wikicode = parse(value)
                    medal_templates = wikicode.filter_templates()

                    for templatei in medal_templates:
                        try:
                            if templatei.name.matches("MedalSport"):
                                global_lst.append("Sport: "+clean(templatei.get(1).value.strip()))
                            elif templatei.name.matches("MedalCountry"):
                                global_lst.append("Country: "+clean(templatei.get(1).value.strip()))
                            elif templatei.name.matches("MedalCount"):
                                global_lst.append("Competition: "+clean(templatei.get(1).value.strip()))
                                global_lst.append("Gold Medal: "+clean(templatei.get(2).value.strip()))
                                global_lst.append("Silver Medal: "+clean(templatei.get(3).value.strip()))
                                global_lst.append("Bronze Medal: "+clean(templatei.get(4).value.strip()))
                                global_lst.append("Competition: "+clean(templatei.get(5).value.strip()))
                                global_lst.append("Gold Medal: "+clean(templatei.get(6).value.strip()))
                                global_lst.append("Silver Medal: "+clean(templatei.get(7).value.strip()))
                                global_lst.append("Bronze Medal: "+clean(templatei.get(8).value.strip()))
                                global_lst.append("Competition: "+clean(templatei.get(9).value.strip()))
                                global_lst.append("Gold Medal: "+clean(templatei.get(10).value.strip()))
                                global_lst.append("Silver Medal: "+clean(templatei.get(11).value.strip()))
                                global_lst.append("Bronze Medal: "+clean(templatei.get(12).value.strip()))
                            elif templatei.name.matches("MedalCompetition"):
                                competition = clean(templatei.get(1).value.strip())
                                global_lst.append("Competition: "+competition)
                            elif templatei.name.matches("MedalGold"):
                                try:
                                    competition = clean(templatei.get(1).value.strip())
                                except:
                                    pass
                                try:
                                    year_event = clean(templatei.get(2).value.strip())
                                except:
                                    pass
                                try:
                                    event = clean(templatei.get(3).value.strip())
                                except:
                                    pass
                                string = 'Gold Medal: '
                                try:
                                    string = string + competition
                                except:
                                    pass
                                try:
                                    string = string + ' ' + year_event
                                except:
                                    pass
                                try:
                                    string = string + ' ' + event
                                except:
                                    pass
                                global_lst.append(string)
                            elif templatei.name.matches("MedalSilver"):
                                try:
                                    competition = clean(templatei.get(1).value.strip())
                                except:
                                    pass
                                try:
                                    year_event = clean(templatei.get(2).value.strip())
                                except:
                                    pass
                                try:
                                    event = clean(templatei.get(3).value.strip())
                                except:
                                    pass
                                string = 'Silver Medal: '
                                try:
                                    string = string + competition
                                except:
                                    pass
                                try:
                                    string = string + ' ' + year_event
                                except:
                                    pass
                                try:
                                    string = string + ' ' + event
                                except:
                                    pass
                                global_lst.append(string)
                            elif templatei.name.matches("MedalBronze"):
                                try:
                                    competition = clean(templatei.get(1).value.strip())
                                except:
                                    pass
                                try:
                                    year_event = clean(templatei.get(2).value.strip())
                                except:
                                    pass
                                try:
                                    event = clean(templatei.get(3).value.strip())
                                except:
                                    pass
                                string = 'Bronze Medal: '
                                try:
                                    string = string + competition
                                except:
                                    pass
                                try:
                                    string = string + ' ' + year_event
                                except:
                                    pass
                                try:
                                    string = string + ' ' + event
                                except:
                                    pass
                                global_lst.append(string)
                        except:
                            pass
                    break
                elif key == 'WorldOpenresult':
                    parsed_code = parse(value)
                    linkss = parsed_code.filter_wikilinks()
                    for linki in linkss:
                        year = linki.text.strip()
                        championship_years[year] = linki.title.strip()
                        
                elif key == 'birth_date':
                    parsed_code = parse(value)
                    date_templatei = parsed_code.filter_templates()[0]
                    try:
                        birth_date = birth_date + date_templatei.get(1).value.strip() + '-' 
                    except:
                        pass
                    try:
                        birth_date = birth_date + date_templatei.get(2).value.strip() + '-' 
                    except:
                        pass
                    try:
                        birth_date = birth_date + date_templatei.get(3).value.strip() + '-'
                    except:
                        pass
                    try:
                        birth_date = birth_date + date_templatei.get(4).value.strip()
                    except:
                        pass
                else:
                    json_dict[key] = clean(value)

                squashMod(json_dict, key)
                modify(json_dict,key)
                
            except:
                continue

        # Post Modification Cleaning
        for key in json_dict:
            if type(json_dict[key]) is str:
                json_dict[key] = post_clean(json_dict[key])
            elif type(json_dict[key]) is list:
                json_dict[key] = [post_clean(a) for a in json_dict[key]]
                
        # Removing empty slots
        remove = []
        for key in json_dict.keys():
            try:
                if(json_dict[key].strip() == ''):
                    remove.append(key)
            except:
                pass
        for key in remove:
            json_dict.pop(key)

        # Removing redundant slots
        for key in redundant:
            try:
                json_dict.pop(key)
            except:
                pass

        try:
            if birth_date:
                json_dict['birth_date'] = birth_date[:-1]
        except:
            pass    

        try:
            if global_lst:
                json_dict['medaltemplates'] = global_lst
        except:
            pass

        try:
            if championship_years:
                json_dict['WorldOpenresult'] = championship_years
        except:
            pass

        

        with open(f"{TEMPLATE}-infoboxes/{page_title}.json", "w", encoding="utf-8") as f:
            new_dict = dict()
            new_dict = json_dict.copy()
            json.dump(new_dict, f, indent=4)
            f.close()
    except:
        pass

# Manually removed last few useless pages
        