from bs4 import BeautifulSoup
import csv
import urllib.request,sys,time
import requests
import re
import copy
import pandas as pd

class Team:
    def __init__(self):
        self.name = None
        self.conf = None

    def change(self, stat_to_add, stat_val):
        if stat_to_add == 'name':
            self.name = stat_val
        elif stat_to_add == 'conf':
            self.conf = stat_val
        else:
            print('+')
        return

    def ret_val(self, stat_to_ret):
        if stat_to_ret == 'name':
            return self.name
        elif stat_to_ret == 'conf':
            return self.conf
        else:
            return 'Attribute Not Present 2'
        return

teams_list = {}
headers = ['name',
            'conf']

def scrape():

    check = 0

    print('processing page :', 'Sports')
    url = 'https://fansided.com/posts/march-madness-bracket-2024-how-many-teams-from-each-conference-made-the-tournament-01hs943wh162'
    print(url)

    # an exception might be thrown, so the code should be in a try-except block
    try:
        # use the browser to get the url. This is suspicious command that might blow up.
        page = requests.get(url)  # this might throw an exception if something goes wrong.

    except Exception as e:  # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()  # get the exception information
        print('ERROR FOR LINK:', url)  # print the link that cause the problem
        print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
        # continue  # ignore this page. Abandon this and go back.

    soup = BeautifulSoup(page.text, 'html.parser')
    scope = soup.find('table', attrs={'class': 'table_1yarp85'})

            
    teams = {}
    bad_str = [' ', ',', '/', '!', '(', ')']

    try:
        # use the browser to get the url. This is suspicious command that might blow up.
        indiv_page = requests.get(new_link)  # this might throw an exception if something goes wrong.

    except Exception as e:  # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()  # get the exception information
        print('ERROR FOR LINK:', new_link)  # print the link that cause the problem
        print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
          # ignore this page. Abandon this and go back.


    for name, row in zip(names, rows):
        if name.text not in teams:
            teams[name.text] = None
        else:
            continue

        teams[name.text] = row.find_all('td')[-1].text

if check == 0:
    key_list = []
    for key in teams.keys():
        key_list.append(key)

    hold_team = {}
    objs = [Team() for i in range(len(teams))]
    for i in range(len(key_list)):
        objs[i].name = key_list[i]
        hold_team[key_list[i]] = objs[i]
    check += 1

for key, val in teams.items():
    hold_team[key].change(curr_stat, val)
teams = {}

    table_list = []
    head_list = []
    for header in headers:
        head_list.append(header)

    table_list.append(head_list)

    for item in objs:
        row_list = []
        for attrib in headers:
            curr_word = attrib
            for i in bad_str:
                curr_word = curr_word.replace(i, '')
            row_list.append(item.ret_val(curr_word))
            # print(row_list)
        table_list.append(row_list)
    # print(table_list)
    return table_list

def main():

    stats = scrape()
    head = stats[0]
    stats = stats[1:]
    df = pd.DataFrame(stats, columns=head)
    print(df)
    df.to_csv('c:/Users/clayw/Desktop/March/MarchMadness.csv', index=False)
    input('Press anything to continue...')

main()
