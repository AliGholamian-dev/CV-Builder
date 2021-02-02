from AliceCV import createAliceCV


class createPDF:
    def __init__(self, dictOfInformation):
        self.dictOfInformation = dictOfInformation

    def makeCV(self):
        if self.dictOfInformation["Template"] == "AliceCV":
            createAliceCV(self.dictOfInformation)
