import requests
import json

class YumiBot:
    """Class for requesting data from Riot API """
    
    def __init__(self, key, region = 'na1'):
        self._api_key = key
        self._region = region

    def __str__(self):
        info = "Current Key: " + self._api_key + "\nCurrent Region: " + self._region
        return info

    def change_key(self, key):
        self._api_key = key

    def change_region(self, region):
        self._region = region

    def request_by_summoner_name(self, name):
        url = "https://" + self._region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + self._api_key
        response = requests.get(url)
        return response.json()

    def get_matchlist_by_id(self, id):
        url = "https://" + self._region + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + id + "?api_key=" + self._api_key
        response = requests.get(url)
        return response.json()
    
    def get_match_data(self,match_id):
        url = "https://" + self._region+ ".api.riotgames.com/lol/match/v4/matches/" + str(match_id) + "?api_key=" + self._api_key
        response = requests.get(url)
        return response.json()


# testing
a = YumiBot("abderf","na1")
id = a.request_by_summoner_name("123")["accountId"]
data = a.get_matchlist_by_id(id)
l = data["matches"][0]["gameId"]
print(a.get_match_data(l))