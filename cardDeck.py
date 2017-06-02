import requests
from Card import Card

deck = [None] * 3 #id, success, remaining

def getDeck():
    #gets a new shuffled deck
    global deck
    url = "http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    
    deck[0] = response.json()['deck_id']
    deck[1] = response.json()['success']
    deck[2] = response.json()['remaining']
    
def dealhandplayer():
    global deck
    url = "http://deckofcardsapi.com/api/deck/" + deck[0] + "/draw/?count=12"
    response = requests.get(url)
    
    p1Hand = [None] * 6
    p2Hand = [None] * 6
    
    for x in range(0,6):
        img = response.json()['cards'][x]['image']
        code = response.json()['cards'][x]['code']
        value = response.json()['cards'][x]['value']
        suit = response.json()['cards'][x]['suit']
        p1Hand[x] = Card(img, code, value, suit)
        
    for p in range(0,6):
        p1Hand[p].getValue()
        
   
getDeck()
dealhandplayer()