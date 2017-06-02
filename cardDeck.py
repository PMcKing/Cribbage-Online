import requests
from Card import Card

deck = [None] * 3 #id, success, remaining
p1Hand = [None] * 6
p2Hand = [None] * 6
def getDeck():
    #gets a new shuffled deck
    global deck
    url = "http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    
    deck[0] = response.json()['deck_id']
    deck[1] = response.json()['success']
    deck[2] = response.json()['remaining']
    
def deal2player():
    global deck, p1Hand, p2Hand
    url = "http://deckofcardsapi.com/api/deck/" + deck[0] + "/draw/?count=12"
    response = requests.get(url)
    
    for x in range(0,5):
        print x
        img = response.json()['cards'][x]['image']
        code = response.json()['cards'][x]['code']
        value = response.json()['cards'][x]['value']
        suit = response.json()['cards'][x]['suit']
        p1Hand[x] = Card(img, code, value, suit)
        
    for x in range(6,12):
        print x
        img = response.json()['cards'][x]['image']
        code = response.json()['cards'][x]['code']
        value = response.json()['cards'][x]['value']
        suit = response.json()['cards'][x]['suit']
        p2Hand[x-6] = Card(img, code, value, suit)
        
   
getDeck()
deal2player()