"""one class to make a rol"""


# waar bestaat enn rol uit :
# een aantal
# een ordernummer
# een itemnummer pdf
# een wikkel

class Roll:
    """rights and needs for a roll """

    def __init__(self, begin, eind, wikkel, item, aantal, posities):
        self.begin = begin
        self.eind = eind
        self.wikkel = wikkel
        self.item = item
        self.aantal = aantal
        self.posities = posities

    def rol(self):
        pass

    def wikkel(self):
        pass

    def qr(self):
        pass

