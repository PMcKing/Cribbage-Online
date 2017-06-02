class Card(object):
    def __init__(self, img, code, value, suit):
        self.img = img
        self.code = code
        self.value = value
        self.suit = suit 
    def getValue(self):
        return self.value
    def getImg(self):
        return self.img; 