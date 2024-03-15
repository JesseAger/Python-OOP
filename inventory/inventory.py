import os
import datetime
import time
import time_date
Date = time_date.Date()
Time = time_date.Time()

def save_items_to_inventory(SerialNo: int, Item: str, Price: float, date = Date, time = Time):
        if not os.path.exists('Inventory.sql'):
            with open('Inventory.sql', 'w') as file:
                file.write("SerialNo\tItem\tPrice\tdate\t\ttime")
        with open('Inventory.sql', 'a') as file:
            file.write(f"{SerialNo.zfill(4)}\t{Item}\t{Price}\t{date}\t{time}\n")


def read_items_from_inventory():
    Items = []
    if os.path.exists('Inventory.sql'):
        with open('Inventory.sql') as file:
            Items= file.readlines
    # return [line.strip().split('\t') for line in Items]

def main():
    saved_items = read_items_from_inventory()

    while True: 
        Item_input = input("Enter data (Item, Date_of_purchase, SerialNo, Purchase_price) separated by commas (or 'q' to quit): ")
        if Item_input == 'q':
            break

        Items = Item_input.split('\t')
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




        









