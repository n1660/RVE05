import sys
import os
from enum import Enum
import bs4 as bs
import requests
import string
#______________________________________________________________________________________________________________________________________#
class Position(Enum):
    ALL = 0
    QB = 1
    RB = 2
    WR = 3
    TE = 4
    K = 7
    DEF = 8


def get_players(pos):
    site = requests.get('http://fantasy.nfl.com/research/projections#researchProjections=researchProjections%2C%2Fresearch%2Fprojections%253Fposition%253D' + str(Position[pos].value) + '%2526statCategory%253DprojectedStats%2526statSeason%253D2018%2526statType%253DseasonProjectedStats%2526statWeek%253D1%2Creplace').text
    file_tmp = ('tmp_' + Position[pos].name + '.txt')
    with open (file_tmp, 'w') as tmp:
        tmp.write(site)  
    with open(file_tmp, 'r') as url:
        soup = bs.BeautifulSoup(url.read(), 'lxml')
    soup_body = soup.body
    soup_body_doc = soup_body.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'doc')
    soup_body_doc_bdWrap = soup_body_doc.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'bd-wrap')
    soup_body_doc_bdWrap_bd = soup_body_doc_bdWrap.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'bd')
    soup_body_doc_bdWrap_bd_primary = soup_body_doc_bdWrap_bd.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'primary')
    soup_body_doc_bdWrap_bd_primary_primaryContent = soup_body_doc_bdWrap_bd_primary.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'primaryContent')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders = soup_body_doc_bdWrap_bd_primary_primaryContent.find(lambda tag: tag.name == 'div' and tag.has_attr('id') and tag['id'] == 'researchScoringLeaders')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders.find(lambda tag: tag.name == 'div' and tag.has_attr('class') and tag['class'] == 'content')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content.find(lambda tag: tag.name == 'div' and tag.has_attr('class') and tag['class'] == 'bd')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd_tableWrap = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd.find(lambda tag: tag.name == 'div' and tag.has_attr('class') and tag['class'] == 'tableWrap')
    table_players = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd_tableWrap.find(lambda tag: tag.name == 'table' and tag.has_attr('class') and tag['class'] == 'tableType-player hasGroups')
    table_players_head = table_players.find(lambda tag: tag.name == 'thead')
    table_players_header = { 'upperhead': table_players_head.find(lambda tag: tag.name == 'thead' and tag.has_attr('class') and tag['class'] == 'first'), \
                                'lowerhead': table_players_head.find(lambda tag: tag.name == 'thead' and tag.has_attr('class') and tag['class'] == 'last') }
    print('\n'.join(table_players_header))



def get_input_position():
    usr_input = ''
    while usr_input.upper() not in [entry.name for entry in Position]:
        usr_input = input('Which position(s)?[QB, RB, WR, TE, K, DEF, ALL]\n')
    return str(usr_input).upper()


def main():
    position = get_input_position()
    get_players(position)

if __name__ == "__main__":
    main()