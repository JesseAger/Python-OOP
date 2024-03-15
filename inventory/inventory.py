import os
from datetime import datetime
from time_date import Time, Date

def save_items_to_inventory(SerialNo: int, Item: str, Price: float, Date = Date, Time=Time):
        if not os.path.exists('Inventory.csv'):
            with open('Inventory.csv', 'w') as file:
                file.write("SerialNo\tItem\tPrice\tDate\tTime")
        with open('Inventory.csv', 'a') as file:
            file.write(f"{SerialNo.zfill(4)}\t{Item}\t{Price}\t{Date}\t{Time}\n")


def read_items_from_inventory():
    Items = []
    if os.path.exists('Inventory.csv'):
        with open('Inventory.csv') as file:
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

        SerialNo, Item, Price = [components.strip() for components in Items]
        save_items_to_inventory(SerialNo, Item, Price, Date)
        print('Inventory Added')

        added_item = read_items_from_inventory()
        # for entry in added_item:
        #     print(entry)

if __name__ == "__main__":
    main()




        









