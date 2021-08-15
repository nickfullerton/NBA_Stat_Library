import bs4, requests
from src.Player import *


class PlayerStats:

    def __init__(self):
        self.__players = []

    def GetPlayer(self, name):
        search_url = "https://www.basketball-reference.com/search/search.fcgi?search="
        full_url = search_url + name
        response = requests.get(full_url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        output = soup.find_all('div', {'class': 'search-item-url'})

        # parallel?
        for value in output:
            if "/international" in value.text:
                continue
            common_url = "https://www.basketball-reference.com/"
            main_url = common_url + value.text
            new_response = requests.get(main_url)
            new_soup = bs4.BeautifulSoup(new_response.text, 'html.parser')
            name = new_soup.find_all('h1', {'itemprop': 'name'})[0].text
            self.__players.append(Player(name.strip('\n'), main_url))
        return self.__players
