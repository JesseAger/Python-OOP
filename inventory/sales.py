import random
class Sales:
    pay_rate = 0.8
    def __init__(self, Price) -> None:
        pass


    


purchase_price = 10
sell_price = 90
profit = sell_price+purchase_price

def exit():
    while True:
        break

def get_item():
    products = ['Phone', 'Laptop', 'Mouse', 'Cable', 'Keyboard', 'Monitor', 'HDDs', 'SSDs']
    Item = random.choice(products)
    return Item


        
get_item()

def generate_serialNo(low=0, count=50, high=100):
    unique_set=set()
    while len(unique_set) < count:
        unique_set.add(random.randint(low, high))
    return (unique_set)


# serialNo = generate_serialNo()

