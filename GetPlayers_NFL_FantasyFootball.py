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
    K = 8
    DEF = 9


def get_players(pos):
    site = requests.get('http://fantasy.nfl.com/research/scoringleaders#researchScoringLeaders=researchScoringLeaders%2C%2Fresearch%2Fscoringleaders%253Fposition%253D' + str(Position[pos])[-1] + '%2526statCategory%253Dstats%2526statSeason%253D2017%2526statType%253DseasonStats%2526statWeek%253D1%2Creplace').text
    file_tmp = ('tmp_' + (Position[pos].split(':')[0].name).split('.')[1] + '.txt')
    with open (file_tmp, 'w') as tmp:
        tmp.write(site)  
    with open(file_tmp, 'r') as url:
        soup = bs.BeautifulSoup(url.read(), 'lxml')
    soup_body = soup.body
    soup_body_doc = soup_body.find('div', id = 'doc')
    soup_body_doc_bdWrap = soup_body_doc.find('div',id = 'bd-wrap')
    soup_body_doc_bdWrap_bd = soup_body_doc_bdWrap.find('div', id = 'bd')
    soup_body_doc_bdWrap_bd_primary = soup_body_doc_bdWrap_bd.find('div', id = 'primary')
    soup_body_doc_bdWrap_bd_primary_primaryContent = soup_body_doc_bdWrap_bd_primary.find('div', id = 'primaryContent')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders = soup_body_doc_bdWrap_bd_primary_primaryContent.find('div', id = 'researchScoringLeaders')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders.find('div', class_ = 'content')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders.find('div', class_ = 'bd')
    soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd_tableWrap = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd.find('div', class_ = 'tableWrap')
    table_players = soup_body_doc_bdWrap_bd_primary_primaryContent_researchScoringLeaders_content_bd_tableWrap.find('table', class_ = 'tableType-player hasGroups')
    table_players_header = table_players.thead.tr('tr', class_ = 'last')
    pass



def get_input_position():
    usr_input = ''
    while usr_input.upper() not in [entry.name for entry in Position]:
        usr_input = input('Which position(s)?[QB, RB, WR, TE, K, DST, ALL]\n')
    return str(usr_input).upper()


def main():
    position = get_input_position()
    get_players(position)

if __name__ == "__main__":
    main()