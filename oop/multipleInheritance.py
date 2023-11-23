class Singer:
    def __init__(self,genre):
        self.genre = genre
    def sing(self):
        print(f'Sing {self.genre} music')

class Dancer:
    def __init__(self,style):
        self.style = style

    def dance(self):
        print(f'Dance {self.style} style')

class Artist:
    def __init__(self,painting_material):
        self.painting_material = painting_material

    def paint(self):
        print(f'Painting with {self.painting_material}')


class SuperHumen(Singer,Dancer,Artist):
    def __init__(self,genre,style,painting_material,sport):
        Singer.__init__(self,genre)
        Dancer.__init__(self,style)
        Artist.__init__(self,painting_material)
        self.sport = sport

    def play(self):
        print(f'Playing {self.sport}')

        #override dance method
    def dance(self, competition):
        print(f'Danceing with {self.style} in {competition}')


super_humen = SuperHumen('Peopo','Pinking po', 'iolpaint', 'Football')

super_humen.dance('P')