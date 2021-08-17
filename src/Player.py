import bs4, requests
import re

class Player:

    def __init__(self, name, url):
        self.__url = url
        self.__name = name
        self.__stats = {}
        self.__playoff = {}
        self.__years = []
        self.__yearsPlayoffs = []
        self.__achievements = []
        self.__info = []

        self.__SetStats()
        self.__SetYears()

    def __SetStats(self):
        req = requests.get(self.__url)
        urlSoup = bs4.BeautifulSoup(req.text, 'html.parser')
        table = urlSoup.find_all('table')
        seasons_reg = table[0].find_all('tr', {'class': 'full_table'})
        seasons_playoff = table[1].find_all('tr', {'class': 'full_table'})
        reg_career = table[0].find('tfoot').find_all('td')
        playoff_career = table[1].find('tfoot').find_all('td')
        self.__FillStats(seasons_reg, seasons_playoff, reg_career, playoff_career)

        achievements = urlSoup.find('ul', {'id':'bling'}).find_all('li')
        for value in achievements:
            self.__achievements.append(value.text)

        personal = urlSoup.find('div', {'id': 'meta'}).find_all('p')

        for value in personal:
            text = value.text
            new_text = ''.join(text.split())
            for item in new_text.split('▪'):
                self.__info.append(item.split(':'))

    def __SetYears(self):
        for key in self.__stats:
            self.__years.append(key)

        for key in self.__playoff:
            self.__yearsPlayoffs.append(key)

    def __FillStats(self, seasons, playoffs, reg_career, playoff_career):
        for value in seasons:
            year = value.find_all('a')[0].text
            stats = value.find_all('td')
            self.__LoadStats(self.__stats, year, stats)

        for value in playoffs:
            year = value.find_all('a')[0].text
            stats = value.find_all('td')
            self.__LoadStats(self.__playoff, year, stats)

        self.__LoadStats(self.__stats, 'Career', reg_career)
        self.__LoadStats(self.__playoff, 'Career', playoff_career)

    def __LoadStats(self, main_dict, name, stats):
        main_dict[name] = {}
        main_dict[name]['Age'] = stats[0].text
        main_dict[name]['Team'] = stats[1].text
        main_dict[name]['League'] = stats[2].text
        main_dict[name]['Position'] = stats[3].text
        main_dict[name]['Games'] = stats[4].text
        main_dict[name]['Games Started'] = stats[5].text
        main_dict[name]['Min Played'] = stats[6].text
        main_dict[name]['FG'] = stats[7].text
        main_dict[name]['FGA'] = stats[8].text
        main_dict[name]['FG%'] = stats[9].text
        main_dict[name]['3P'] = stats[10].text
        main_dict[name]['3PA'] = stats[11].text
        main_dict[name]['3P%'] = stats[12].text
        main_dict[name]['2P'] = stats[13].text
        main_dict[name]['2PA'] = stats[14].text
        main_dict[name]['2P%'] = stats[15].text
        main_dict[name]['eFG%'] = stats[16].text
        main_dict[name]['FT'] = stats[17].text
        main_dict[name]['FTA'] = stats[18].text
        main_dict[name]['FT%'] = stats[19].text
        main_dict[name]['ORB'] = stats[20].text
        main_dict[name]['DRB'] = stats[21].text
        main_dict[name]['TRB'] = stats[22].text
        main_dict[name]['APG'] = stats[23].text
        main_dict[name]['SPG'] = stats[24].text
        main_dict[name]['BPG'] = stats[25].text
        main_dict[name]['TOV'] = stats[26].text
        main_dict[name]['PF'] = stats[27].text
        main_dict[name]['PTS'] = stats[28].text

    def GetStats(self):
        return self.__stats

    def GetPlayoffStats(self):
        return self.__playoff

    def GetName(self):
        return self.__name

    def GetYears(self):
        return self.__years

    def GetPlayoffYears(self):
        return self.__yearsPlayoffs

    def GetAchievements(self):
        return self.__achievements

    def GetInfo(self):
        return self.__info