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

def generate_serialNo():
    unique_set=set()
    for i in range(1, 100):
        unique_set.add(random.randint(0, i))
        serial_set=list(unique_set)
        for number in serial_set:
            return number
    
generate_serialNo()
# serialNo = generate_serialNo()

