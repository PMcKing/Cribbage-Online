import requests

deck = [None] * 3 #id, success, remaining

def getDeck():
    global deck
    url = "http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    
    deck[0] = response.json()['deck_id']
    deck[1] = response.json()['success']
    deck[2] = response.json()['remaining']
    
    
    for p in deck: print p
    
  
getDeck()