import requests
import time 
import json

class YumiBot:
    """Class for requesting data from Riot API """
    
    def __init__(self, key, region = 'na1', rate = 50):
        self._api_key = key
        self._region = region
        self._rate = rate

    def __str__(self):
        info = "Current Key: " + self._api_key + "\nCurrent Region: " + self._region
        return info

    def change_key(self, key):

        self._api_key = key

    def change_region(self, region):
        """
        Change region of the scraper 

        Parameters
        ----------
        region : String
            The region id defined by the riot api (defaulted na1)

        Returns
        -------
        None
        """
        self._region = region

    def request_by_summoner_name(self, name):
        """
        Request player IDs by summoner name

        Parameters
        ----------
        name : String
            Player's ingame name

        Returns
        -------
        response.json() : dict()
            Json format of the result requested from Riot API
        """
        url = "https://" + self._region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + self._api_key
        response = requests.get(url)
        return response.json()

    def get_matchlist_by_id(self, id):
        """
        Get the most recent 100 game a player had played including special mode

        Parameters
        ----------
        id : String
            The id obtained in player information

        Returns
        -------
        response.json() : dict()
            Json format of the result requested from Riot API
        """
        url = "https://" + self._region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + id + "?queue=420&api_key=" + self._api_key
        response = requests.get(url)
        return response.json()
    
    def get_match_data(self,match_id):
        """
        Get specific information about a match by the match_id 

        Parameters
        ----------
        match_id : int
            The match id

        Returns
        -------
        response.json() : dict()
            Json format of the result requested from Riot API
        """
        url = "https://" + self._region+ ".api.riotgames.com/lol/match/v4/matches/" + str(match_id) + "?api_key=" + self._api_key
        response = requests.get(url)
        return response.json()

    def get_game_ids_by_name(self, name):
        """
        Get and return the match_ids of a player's ranked games

        Parameters
        ----------
        name : String
            Player's ingame name

        Returns
        -------
        game_id : List
            A list of match ids of 100 ranked games 
        """
        id  = self.request_by_summoner_name(name)["accountId"]
        data = self.get_matchlist_by_id(id)["matches"]
        
        game_id = list()
        for index in data:
            game_id.append(index["gameId"])
        return game_id
    

# testing
a = YumiBot("mystery","na1")
b = a.get_game_ids_by_name("asd")
print(a.get_match_data(b[0])["teams"][0])