class Card(object):
    def __init__(self, img, code, value, suit):
        self.img = img
        self.code = code
        self.value = value
        self.suit = suit 
    def getValue(self):
        print self.value