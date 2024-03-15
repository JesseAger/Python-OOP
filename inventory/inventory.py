import os
from datetime import datetime

def save_items_to_inventory(SerialNo: int, Item: str, Date: str, Price: float):
        if not os.path.exists('Inventory.txt'):
            with open('Inventory.txt', 'w') as file:
                file.write("SerialNo\tItem\tDate\tPrice")
        with open('Inventory.txt', 'a') as file:
            file.write(f"{SerialNo.zfill(4)}\t{Item}\t{Date}\t{Price}\n")


def read_items_from_inventory():
    Items = []
    if os.path.exists('Inventory.txt'):
        with open('Inventory.txt') as file:
            Items= file.readlines
    # return [line.strip().split('\t') for line in Items]

def main():
    saved_items = read_items_from_inventory()

    while True: 
        Item_input = input("Enter data (Item, Date_of_purchase, SerialNo, Purchase_price) separated by commas (or 'q' to quit): ")
        if Item_input == 'q':
            break

        Items = Item_input.split(',')
        if len(Items) !=4:
            print('Incomplete Inventory information')
            continue

        SerialNo, Item, Date, Price = [components.strip() for components in Items]
        save_items_to_inventory(SerialNo, Item, Date, Price)
        print('Inventory Added')

        added_item = read_items_from_inventory()
        # for entry in added_item:
        #     print(entry)

if __name__ == "__main__":
    main()




        









