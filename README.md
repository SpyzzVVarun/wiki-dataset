<h1 align = "center">WikiExtract</h1>
<p align = "center"> An Open Domain English Information Extraction/Text-to-Table/Table-to-Text Dataset focusing on the Sports Domain</p>

## Overview 

A dataset of 29,051 entities across 11 sports categories, comprising structured infoboxes and unstructured content extracted from Wikipedia articles, intended for tasks in Information Extraction, such as automated infobox generation and updating from page content, and Text Generation, such as Text-to-Table and Table-to-Text generation.


## Motivation

This dataset has been created to facilitate research and development in the field of information extraction and text generation. When talking about text generation, it aims to support tasks in the domain of Table-to-Text or Text-to-Table generation. It also aims to support tasks such as automated infobox generation and updation from Wikipedia page content. The motivation behind this is to enable more efficient and accurate extraction of structured information from unstructured (and structured) text, particularly from Wikipedia articles, which are rich in structured and unstructured data.

## Why Sports Domain?

TLDR: Complex structure of infobox data in several categories along with rich unstructured and semi-structured data in the page content.

The sports domain was chosen due to its unique characteristics, including the complex structure of infobox data and the richness of unstructured and semi-structured content within Wikipedia articles. In many sports categories, the infoboxes contain a wealth of structured information such as player statistics, team details, match results, and tournament history. This structured data is often organized in a hierarchical or relational format, making it a challenging but valuable resource for tasks such as automated infobox generation and data extraction.

Moreover, the sports articles on Wikipedia are known for their extensive narrative content, which provides context, analysis, and historical background related to the sports category. By focusing on the sports domain, we can explore innovative approaches to extract, analyze, and utilize both structured and unstructured data, leading to advancements in natural language processing, information retrieval, and knowledge representation. 

## Sports Categories

The categories, their entity counts and the templates are provided below. The templates for each infobox can be accessed via the given links
 
1. [Alpine Sking](https://en.wikipedia.org/wiki/Template:Infobox_alpine_ski_racer) - 340
2. [Badminton](https://en.wikipedia.org/wiki/Template:Infobox_badminton_player) - 3157
3. [Baseball](https://en.wikipedia.org/wiki/Template:Infobox_baseball_biography) - 1419
4. [Basketball](https://en.wikipedia.org/wiki/Template:Infobox_basketball_biography) - 4768
5. [Cricketer](https://en.wikipedia.org/wiki/Template:Infobox_cricketer) - 4945
6. [Cyclist](https://en.wikipedia.org/wiki/Template:Infobox_cyclist) - 4945
7. [Equesterian](https://en.wikipedia.org/wiki/Template:Infobox_equestrian) - 188
8. [Football](https://en.wikipedia.org/wiki/Template:Infobox_football_biography) - 4607
9. [Squash](https://en.wikipedia.org/wiki/Template:Infobox_squash_player) - 774
10. [Tennis](https://en.wikipedia.org/wiki/Template:Infobox_tennis_biography) - 3077
11. [Table Tennis](https://en.wikipedia.org/wiki/Template:Infobox_table_tennis_player) - 831

## Contents

`infoboxes_1`: Contains the infobox data for each entity and is contained within the category folders

`pages_1`: Contains the non-infobox page content for each entity and is contained within the category folders

`scripts` - Contains the category-wise data extraction and processing code.

## Steps to Reproduce

### Infoboxes

1. Go to the category sub-directory in the `scripts` directory.
2. Extract the relevant entities to `titles.txt`
   
   ```
   python entities.py
   ```

3. Create the folder with the name `f"{TEMPLATE}-infoboxes"` with TEMPLATE from `constants.py`
4. Extract the entities to the the above created directory

   ```
   python main.py
   ```

### Non-Infobox

1. Go to the `pages` sub-directory in the `scripts` directory.
2. Run `code.ipynb`

## Example Data Instance: Sachin Tendulkar

### Non-Infobox Page Content

The non-infobox text on the Wikipedia page of Sachin Tendulkar, accessible at [this link](https://en.wikipedia.org/wiki/Sachin_Tendulkar), provides comprehensive information about his life, career, achievements, and contributions to the sport of cricket.

### Infobox

```json
{
    "name": "Sachin Tendulkar",
    "country": "India",
    "fullname": "Sachin Ramesh Tendulkar",
    "birth_place": "Bombay, Maharashtra, India, (now Mumbai, India)",
    "height": "165 cm",
    "family": "Ramesh Tendulkar (father)",
    "batting": "Right-handed",
    "bowling": "Right-arm leg Right-arm leg break",
    "internationalspan": "1989-2013",
    "testdebutdate": "15 November",
    "testdebutyear": "1989",
    "testdebutagainst": "Pakistan",
    "testcap": "187",
    "lasttestdate": "14 November",
    "lasttestyear": "2013",
    "lasttestagainst": "West Indies",
    "odidebutdate": "18 December",
    "odidebutyear": "1989",
    "odidebutagainst": "Pakistan",
    "odicap": "74",
    "odishirt": "10 (formerly 99, 33)",
    "lastodidate": "18 March",
    "lastodiyear": "2012",
    "lastodiagainst": "Pakistan",
    "oneT20I": "true",
    "T20Idebutdate": "1 December",
    "T20Idebutyear": "2006",
    "T20Idebutagainst": "South Africa",
    "T20Icap": "11",
    "T20Ishirt": "10",
    "source": "https://www.espncricinfo.com/india/content/player/35320.html ESPNcricinfo",
    "module": "Infobox officeholder",
    "embed": "yes",
    "signature": "Sachin Tendulkar Signature.svg",
    "office": "Member of Parliament, Rajya Sabha",
    "constituency": "Nominated",
    "term_start": "27 April 2012",
    "term_end": "26 April 2018 ",
    "Test": {
        "matches": "200",
        "runs": "15,921",
        "bat avg": "53.78",
        "100s/50s": "51/68",
        "deliveries": "4,240",
        "wickets": "46",
        "bowl avg": "54.17",
        "fivefor": "0",
        "tenfor": "0",
        "best bowling": "3/10",
        "catches/stumpings": "115/-"
    },
    "ODI": {
        "matches": "463",
        "runs": "18,426",
        "bat avg": "44.83",
        "100s/50s": "49/96",
        "deliveries": "8,054",
        "wickets": "154",
        "bowl avg": "44.48",
        "fivefor": "2",
        "tenfor": "0",
        "best bowling": "5/32",
        "catches/stumpings": "140/-"
    },
    "FC": {
        "matches": "310",
        "runs": "25,396",
        "bat avg": "57.84",
        "100s/50s": "81/116",
        "deliveries": "7,605",
        "wickets": "71",
        "bowl avg": "61.74",
        "fivefor": "0",
        "tenfor": "0",
        "best bowling": "3/10",
        "catches/stumpings": "186/-"
    },
    "LA": {
        "matches": "551",
        "runs": "21,999",
        "bat avg": "45.54",
        "100s/50s": "60/114",
        "deliveries": "10,230",
        "wickets": "201",
        "bowl avg": "42.17",
        "fivefor": "2",
        "tenfor": "0",
        "best bowling": "5/32",
        "catches/stumpings": "175/-"
    },
    "clubs": {
        "Mumbai": "1988-2013",
        "Yorkshire": "1992",
        "East Bengal": "1994",
        "Mumbai Indians( 10 )": "2008-2013"
    },
    "birth_date": "1973-4-24",
    "medaltemplates": [
        "Sport: Men's Cricket",
        "Country: {{IND}}",
        "Competition: ICC Cricket World Cup",
        "Competition: ICC Champions Trophy",
        "Competition: ACC Asia Cup",
        "Competition: Austral-Asia Cup"
    ]
}
```



## Version Information

v1.0 (this version) Initial Release.

## License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
