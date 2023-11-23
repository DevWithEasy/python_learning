class Toy:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

def print_to_object(toy_list):
    for item in toy_list:
        print(f'Name: {item.name}, Price: {item.price}')

toy_1 = Toy('Car',100)
toy_2 = Toy('Bike', 80)
toy_3 = Toy('Magnet',200)

toy_list = [toy_1, toy_2, toy_3]

# print_to_object(toy_list)

#default sorting sort method
# toy_list.sort(key=Toy.sort_priority)
# print_to_object(toy_list)

#default sorting sorted method
# sorted_toy_list = sorted(toy_list,key= Toy.sort_priority)
# print_to_object(sorted_toy_list)

#default sort with sort method and lambda function
# toy_list.sort(key= lambda x: x.price, reverse= True)
# print_to_object(toy_list)

#default sort with sorted method and lambda function
# sorted_toy_list = sorted(toy_list, key= lambda x: x.price, reverse= True)
# print_to_object(sorted_toy_list)