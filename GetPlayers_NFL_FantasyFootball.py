import sys
import time
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
    WRRB_FLEX = 5
    K = 7
    DEF = 8


def get_bs_tag_by_ID(parent_tag, type, id):
    return parent_tag.find(lambda tag: tag.name == type and tag.has_attr('id') and tag['id'] == id)


def get_bs_tag_by_class(parent_tag, type, classname):
    return parent_tag.find(lambda tag: tag.name == type and tag.has_attr('class') and tag['class'] == classname)


def get_players(pos, offset, year):
    if offset < 1:
        offset = 1

        if Position[pos].value == 0:
            site = requests.get('http://fantasy.nfl.com/draftcenter/breakdown?leagueId=#draftCenterBreakdown=draftCenterBreakdown%2C%2Fdraftcenter%2Fbreakdown%253FleagueId%253D%2526offset%253D' + str(offset) + '%2526position%253Dall%2526season%253D' + year + '%2526sort%253DdraftAveragePosition%2Creplace').text
        # elseif offset:
        #     site = requests.get('http://fantasy.nfl.com/draftcenter/breakdown?leagueId=#draftCenterBreakdown=draftCenterBreakdown%2C%2Fdraftcenter%2Fbreakdown%253FleagueId%253D%2526offset%253D' + str(offset) + '%2526position%253D' + str(Position[pos].value) + '%2526season%253D' + year + '%2526sort%253DdraftAveragePosition%2Creplace').text
        file_tmp = ('AverageDraftPositions/adp_' + Position[pos].name + '.txt')
        
        common(soup)
        common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_bd'] = get_bs_tag_by_class(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content'], 'div', 'bd')
        common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_bd_tableWrap'] = get_bs_tag_by_class(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_bd'], 'div', 'tableWrap')
        main.table_players[str(year)] = get_bs_tag_by_class(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_bd_tableWrap'], 'table', 'tableType-Players hasGroups')


def common(soup):
    common.soup['body'] = main.soup.body
    common.soup['body_doc'] = get_bs_tag_by_ID(common.soup['body'], 'div', 'doc')
    common.soup['body_doc_bdWrap'] = get_bs_tag_by_ID(common.soup['body_doc'], 'div', 'bd-wrap')
    common.soup['body_doc_bdWrap_bd'] = get_bs_tag_by_ID(common.soup['body_doc_bdWrap'], 'div', 'bd')
    common.soup['body_doc_bdWrap_bd_primary'] = get_bs_tag_by_ID(common.soup['body_doc_bdWrap_bd'], 'div', 'primary')
    common.soup['body_doc_bdWrap_bd_primary_primaryContent'] = get_bs_tag_by_ID(soup['body_doc_bdWrap_bd_primary'], 'div', 'primaryContent')
    common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown'] = get_bs_tag_by_ID(common.soup['body_doc_bdWrap_bd_primary_primaryContent'], 'div', 'draftCenterBreakdown')
    common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content'] = get_bs_tag_by_ID(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown'], 'div', 'content')


def count_position_depths(url):
    for str_pos in Position:
        common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd'] = get_bs_tag_by_class(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content'], 'div', 'hd')
        common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd_paginationWrap'] = get_bs_tag_by_class(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd'], 'div', 'paginationWrap')
        common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd_paginationWrap_paginationSearch'] = get_bs_tag_by_class(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd_paginationWrap'], 'div', 'pagination search')
        common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd_paginationWrap_paginationSearch_paginationTitle'] = get_bs_tag_by_class(common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd_paginationWrap_paginationSearch'], 'span', 'pagination search')
        main.stock[str_pos] = common.soup['body_doc_bdWrap_bd_primary_primaryContent_draftCenterBreakdown_content_hd_paginationWrap_paginationSearch_paginationTitle'].split(' ')[-2]


def main():
    main.table_players = {}
    common.soup = {}
    main.stock = {}
    year = time.ctime().split(' ')[-1]
    with open (file_tmp, 'w') as tmp:
        tmp.write(site)  
    with open(file_tmp, 'r') as html:
        main.soup = bs.BeautifulSoup(html.read(), 'lxml')
    for position in Position:
        get_players(position, offset, year)

if __name__ == "__main__":
    main()