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
        self.AssistsTurnoverRatio = None
        self.AssistsPerGame = None
        self.BenchPointspergame = None
        self.BlocksPerGame = None
        self.EffectiveFGpct = None
        self.FastbreakPoints = None
        self.FieldGoalPercentage = None
        self.FieldGoalsPercentageDefense = None
        self.FoulsPerGame = None
        self.FreeThrowAttemptsPerGame = None
        self.FreeThrowsMadePerGame = None
        self.ReboundMargins = None
        self.ReboundsDefensivePerGame = None
        self.ReboundsOffensivePerGame = None
        self.ReboundsPerGame = None
        self.ScoringDefense = None
        self.ScoringMargin = None
        self.ScoringOffense = None
        self.StealsPerGame = None
        self.ThreePointAttemptsPerGame = None
        self.ThreePointPercentage = None
        self.ThreePointPercentageDefense = None
        self.ThreePointersPerGame = None
        self.TurnoverMargin = None
        self.TurnoversForcedPerGame = None
        self.TurnoversPerGame = None
        self.WinningPercentage = None

    def change(self, stat_to_add, stat_val):
        if stat_to_add == 'name':
            self.name = stat_val
        elif stat_to_add == 'AssistTurnoverRatio':
            self.AssistsTurnoverRatio = stat_val
        elif stat_to_add == 'AssistsPerGame':
            self.AssistsPerGame = stat_val
        elif stat_to_add == 'BenchPointspergame':
            self.BenchPointspergame = stat_val
        elif stat_to_add == 'BlocksPerGame':
            self.BlocksPerGame = stat_val
        elif stat_to_add == 'EffectiveFGpct':
            self.EffectiveFGpct = stat_val
        elif stat_to_add == 'FastbreakPoints':
            self.FastbreakPoints = stat_val
        elif stat_to_add == 'FieldGoalPercentage':
            self.FieldGoalPercentage = stat_val
        elif stat_to_add == 'FieldGoalPercentageDefense':
            self.FieldGoalPercentageDefense = stat_val
        elif stat_to_add == 'FoulsPerGame':
            self.FoulsPerGame = stat_val
        elif stat_to_add == 'FreeThrowAttemptsPerGame':
            self.FreeThrowAttemptsPerGame = stat_val
        elif stat_to_add == 'FreeThrowPercentage':
            self.FieldGoalPercentage = stat_val
        elif stat_to_add == 'FreeThrowsMadePerGame':
            self.FreeThrowsMadePerGame = stat_val
        elif stat_to_add == 'ReboundMargin':
            self.ReboundMargin = stat_val
        elif stat_to_add == 'ReboundsDefensivePerGame':
            self.ReboundsDefensivePerGame = stat_val
        elif stat_to_add == 'ReboundsOffensivePerGame':
            self.ReboundsOffensivePerGame = stat_val
        elif stat_to_add == 'ReboundsPerGame':
            self.ReboundsPerGame = stat_val
        elif stat_to_add == 'ScoringDefense':
            self.ScoringDefense = stat_val
        elif stat_to_add == 'ScoringMargin':
            self.ScoringMargin = stat_val
        elif stat_to_add == 'ScoringOffense':
            self.ScoringOffense = stat_val
        elif stat_to_add == 'StealsPerGame':
            self.StealsPerGame = stat_val
        elif stat_to_add == 'ThreePointAttemptsPerGame':
            self.ThreePointAttemptsPerGame = stat_val
        elif stat_to_add == 'ThreePointPercentage':
            self.ThreePointPercentage = stat_val
        elif stat_to_add == 'ThreePointPercentageDefense':
            self.ThreePointPercentageDefense = stat_val
        elif stat_to_add == 'ThreePointersPerGame':
            self.ThreePointersPerGame = stat_val
        elif stat_to_add == 'TurnoverMargin':
            self.TurnoverMargin = stat_val
        elif stat_to_add == 'TurnoversForcedPerGame':
            self.TurnoversForcedPerGame = stat_val
        elif stat_to_add == 'TurnoversPerGame':
            self.TurnoversPerGame = stat_val
        elif stat_to_add == 'WinningPercentage':
            self.WinningPercentage = stat_val
        else:
            print('+')
        return

    def ret_val(self, stat_to_ret):
        if stat_to_ret == 'name':
            return self.name
        elif stat_to_ret == 'AssistTurnoverRatio':
            return self.AssistsTurnoverRatio
        elif stat_to_ret == 'AssistsPerGame':
            return self.AssistsPerGame
        elif stat_to_ret == 'BenchPointspergame':
            return self.BenchPointspergame
        elif stat_to_ret == 'BlocksPerGame':
            return self.BlocksPerGame
        elif stat_to_ret == 'EffectiveFGpct':
            return self.EffectiveFGpct
        elif stat_to_ret == 'FastbreakPoints':
            return self.FastbreakPoints
        elif stat_to_ret == 'FieldGoalPercentage':
            return self.FieldGoalPercentage
        elif stat_to_ret == 'FieldGoalPercentageDefense':
            return self.FieldGoalPercentageDefense
        elif stat_to_ret == 'FoulsPerGame':
            return self.FoulsPerGame
        elif stat_to_ret == 'FreeThrowAttemptsPerGame':
            return self.FreeThrowAttemptsPerGame
        elif stat_to_ret == 'FreeThrowPercentage':
            return self.FieldGoalPercentage
        elif stat_to_ret == 'FreeThrowsMadePerGame':
            return self.FreeThrowsMadePerGame
        elif stat_to_ret == 'ReboundMargin':
            return self.ReboundMargin
        elif stat_to_ret == 'ReboundsDefensivePerGame':
            return self.ReboundsDefensivePerGame
        elif stat_to_ret == 'ReboundsOffensivePerGame':
            return self.ReboundsOffensivePerGame
        elif stat_to_ret == 'ReboundsPerGame':
            return self.ReboundsPerGame
        elif stat_to_ret == 'ScoringDefense':
            return self.ScoringDefense
        elif stat_to_ret == 'ScoringMargin':
            return self.ScoringMargin
        elif stat_to_ret == 'ScoringOffense':
            return self.ScoringOffense
        elif stat_to_ret == 'StealsPerGame':
            return self.StealsPerGame
        elif stat_to_ret == 'ThreePointAttemptsPerGame':
            return self.ThreePointAttemptsPerGame
        elif stat_to_ret == 'ThreePointPercentage':
            return self.ThreePointPercentage
        elif stat_to_ret == 'ThreePointPercentageDefense':
            return self.ThreePointPercentageDefense
        elif stat_to_ret == 'ThreePointersPerGame':
            return self.ThreePointersPerGame
        elif stat_to_ret == 'TurnoverMargin':
            return self.TurnoverMargin
        elif stat_to_ret == 'TurnoversForcedPerGame':
            return self.TurnoversForcedPerGame
        elif stat_to_ret == 'TurnoversPerGame':
            return self.TurnoversPerGame
        elif stat_to_ret == 'WinningPercentage':
            return self.WinningPercentage
        else:
            return 'Attribute Not Present 2'
        return

teams_list = {}
headers = ['name',
            'Assist/Turnover Ratio',
            'Assists Per Game',
            'Bench Points per game',
            'Blocks Per Game',
            'Effective FG pct',
            'Fastbreak Points',
            'Field Goal Percentage',
            'Field Goal Percentage Defense',
            'Fouls Per Game',
            'Free Throw Attempts Per Game',
            'Free Throw Percentage',
            'Free Throws Made Per Game',
            'Rebound Margin',
            'Rebounds (Defensive) Per Game',
            'Rebounds (Offensive) Per Game',
            'Rebounds Per Game',
            'Scoring Defense',
            'Scoring Margin',
            'Scoring Offense',
            'Steals Per Game',
            'Three Point Attempts Per Game',
            'Three Point Percentage',
            'Three Point Percentage Defense',
            'Three Pointers Per Game',
            'Turnover Margin',
            'Turnovers Forced Per Game',
            'Turnovers Per Game',
            'Winning Percentage']

def scrape():

    check = 0

    print('processing page :', 'Sports')
    url = 'https://www.ncaa.com/stats/basketball-men/d1'
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
    scope = soup.find('div', attrs={'id': 'block-bespin-content'})
    scope = scope.find_all('div', attrs={'class': 'stats-header__filter'})
    scope = scope[1]
    scope = scope.find('select')
    scope = scope.find_all('option')

    stats_url = []
    for item in scope:
        if item['value'] == '':
            continue
        else:
            stats_url.append(item['value'])
    
    # print(stats_url)
            
    teams = {}
    bad_str = [' ', ',', '/', '!', '(', ')']
    for link in stats_url:
        print(link)
        for page in range(1, 9):
            new_link = url = 'https://www.ncaa.com' + link + '/p' + str(page)

            try:
                # use the browser to get the url. This is suspicious command that might blow up.
                indiv_page = requests.get(new_link)  # this might throw an exception if something goes wrong.

            except Exception as e:  # this describes what to do if an exception is thrown
                error_type, error_obj, error_info = sys.exc_info()  # get the exception information
                print('ERROR FOR LINK:', new_link)  # print the link that cause the problem
                print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
                continue  # ignore this page. Abandon this and go back.

            # print(new_link)
            stat_text = BeautifulSoup(indiv_page.text, 'html.parser')
            curr_stat = stat_text.find('div', attrs={'class': 'stats-header__lower__title'}).text.strip()
            for i in bad_str:
                curr_stat = curr_stat.replace(i, '')
            stats_scope = stat_text.find('tbody')
            names = stats_scope.find_all('a')
            rows = stats_scope.find_all('tr')

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
