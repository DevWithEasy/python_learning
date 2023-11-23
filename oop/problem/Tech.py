class Tech :
    total_products = 0
    discount = 0.5

    def __init__(self, name, price, weigth, color):
        self.name = name
        self.price = price
        self.color = color
        self.weight = weigth
        Tech.total_products += 1
    
    def apply_discount(self):
        self.price = int(self.price - self.price * Tech.discount)

    def calculate_shipping_cost(self , rate):
        return f'Shipping cost will be {round(self.weight * rate,2)}'
    
    @classmethod
    def get_total_poducts(cls):
        return f'Total poducts is {cls.total_products}'
