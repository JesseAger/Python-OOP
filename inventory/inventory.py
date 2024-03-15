import os
import datetime
import time
from time_date import Time, Date

def save_items_to_inventory(SerialNo: int, Item: str, Price: float, Date_of_execution = Date, Time_of_execution = Time):
        if not os.path.exists('Inventory.csv'):
            with open('Inventory.csv', 'w') as file:
                file.write("SerialNo\tItem\tPrice\tDate_of_execution\tTime_of_execution")
        with open('Inventory.csv', 'a') as file:
            file.write(f"{SerialNo.zfill(4)}\t{Item}\t{Price}\t{Date_of_execution}\t{Time_of_execution}\n")


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
        if len(Items) !=3:
            print('Incomplete Inventory information')
            continue

        SerialNo, Item, Price = [components.strip() for components in Items]
        save_items_to_inventory(SerialNo, Item, Price, Date, Time)
        print('Inventory Added')

        added_item = read_items_from_inventory()
        # for entry in added_item:
        #     print(entry)

if __name__ == "__main__":
    main()




        









