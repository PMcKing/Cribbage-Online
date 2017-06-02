import requests
import Card

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
   
getDeck()