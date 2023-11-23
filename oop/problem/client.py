from Tech import Tech
from Mobile import Mobile
from Laptop import Laptop
from SalesMan import SalesMan
from datetime import date

phone_1 = Mobile('Samsung A54', 35000, 198, 'Blue', 6.6, 64)
phone_2 = Mobile('Realme 8 5g', 25000, 200, 'Black', 6.7, 42)
phone_3 = Mobile('Nokia N70', 7500, 120, 'Sky', 3.2, 8)

laptop_1 = Laptop('Dell', 45000, 1.2, 'Black', 4, 'Ryxen', .5)
laptop_2 = Laptop('HP', 85000, 1.3, 'Silver', 8, 'Intel', 1)
laptop_3 = Laptop('Asus', 77500, 1.5, 'Purple Black', 'Black-barry', 16, 1)

# print price
# print(phone_1.price)

# print discount
# phone_1.apply_discount()
# print(phone_1.price)

# print total product
# print(Tech.get_total_poducts())

#shiping cost
# print(laptop_3.calculate_shipping_cost(50))

#salesman
# salesman_1 = SalesMan('Robiul', 'Awal', 25000, date(1996,4,11))
# salesman_1.sale_product(phone_1)
# salesman_1.display_sales()