from Tech import Tech

class Mobile(Tech): 
    def __init__(self, name, price, weigth, color, screen, camera):
        super().__init__(name, price, weigth, color)
        self.screen = screen
        self.camera = camera

    def apply_discount(self):
        self.price = int(self.price - self.price * super().discount/2)

    def __str__(self):
        return  f'Name: {self.name}\nPrice: {self.price}\nWeight: {self.weight}\n'\
                f'Color: {self.color}\nScreen: {self.screen}\nCamera: {self.camera}\n'\

