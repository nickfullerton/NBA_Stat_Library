# NBA Stat Library

Library that can be used in any NBA related Python Programs.  

It uses web scraping to get the players stats.  



## Description  


### Built With  

* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [requests](https://docs.python-requests.org/en/latest/)
* [re](https://docs.python.org/3/library/re.html)


### `main.py`

![The Main](https://user-images.githubusercontent.com/72878403/129645725-f9fc49c7-b703-464f-9c55-b86d2650d7ad.PNG)


### Output of `main.py`

![Output of The Main](https://user-images.githubusercontent.com/72878403/129645752-12a75dfc-4932-46df-8579-b014dadce296.PNG)


## Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/nickfullerton/NBA_Stat_Library.git
   ```
2. Go to `main.py`
3. Load in the class and choose a player you want
   ```python
   player = PlayerStats()
   players = player.GetPlayer("Michael Jordan")
   ```
4. Call any class methods to get the stats of the player
   ```python
    players[0].GetName()  # Returns Str, The player's name
    players[0].GetStats()  # Returns Dict, The player's regular season stats of his career
    players[0].GetPlayoffStats()  # Returns Dict, The player's playoff stats of his career
   ```



## License

Distributed under the MIT License. See `LICENSE.md` for more information.



## Contact

Nicholas Fullerton  - nickfullerton2285@gmail.com

Project Link: [https://github.com/nickfullerton/NBA_Stat_Library](https://github.com/nickfullerton/NBA_Stat_Library)
