class Robot :
    def __init__(self, name, version):
        self.name = name
        self.version = version
    
    def move_backward(self):
        print(f'{self.name} is moving backwards')
    
    def move_forward(self):
        print(f'{self.name} is moving forward')

    def move_rightward(self):
        print(f'{self.name} is moving right backwards')

    def move_leftward(self):
        print(f'{self.name} is moving left backwards')


class HouseBot(Robot) :
    def __init__(self, name, version,area_cover) :
        super().__init__(name, version)
        self.area_cover = area_cover

    def clean(self):
        if self.area_cover > 0 :
            print(f'{self.name} is cleaning the house')
            self.area_cover -= 30

            if self.area_cover < 0 :
                self.area_cover = 0
        else :
            print(f'{self.name} is not cleaning the house ! please reset area_cover')

    def set_area_cover(self, area_cover):
        if self.area_cover == 0 :
            self.area_cover = area_cover
        else :
            print(f'I can still clean more area')

    #metho override
    def move_backward(self):
        print(f'{self.name} is moving override backwards')
        super().move_backward()

house_bot = HouseBot('house_bot',1.1,50)

# print(house_bot.name)
# house_bot.clean()
# house_bot.clean()
# house_bot.clean()
# house_bot.set_area_cover(50)
# house_bot.clean()
# house_bot.clean()
# house_bot.clean()
# house_bot.move_backward()

#buildin helper method for class

# print(help(Robot))
# print(issubclass(Robot,HouseBot))
# print(issubclass(HouseBot,Robot))
# print(issubclass(HouseBot,object))
# print(isinstance(house_bot,HouseBot))
# print(isinstance(house_bot,Robot))
# print(isinstance(house_bot,object))