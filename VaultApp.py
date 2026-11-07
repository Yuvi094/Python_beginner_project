import json
import os 
vault_data =[]
vaultData = "vaultData.json"
def save_data(data_list): 
    with open(vaultData , "w" ) as f:
        json.dump(data_list, f , indent=5)
    print("Data has been saved.")
def load_data():
    if not os.path.exists(vaultData):
        return []
    else :
         try: 
             with open(vaultData,"r") as f:
                 return json.load(f)
         except json.JSONDecodeError:
             return []             
def add_data(data_list):
    name_business = input("Enter name of business: ")
    item_name = input("Enter the item name: ")
    while True:
        try:
            bill = float(input("Enter the bill amount: "))
            break
        except ValueError:
            print("Invalid Input ")
    date = input("Enter the date of sale: ")
    entry = {
        "Id": len(data_list) + 1,
        "Name": name_business,
        "Item": item_name,
        "Bill": bill,
        "Date": date
    }
    data_list.append(entry)
def view_data(data_list):
    if not data_list:
       print("There is no data to be viewed here.")
    else:
        for entry in data_list:
            print(f"ID: {entry['Id']} | Business: {entry['Name']} | Item: {entry['Item']} | Bill: {entry['Bill']} | Date: {entry['Date']}")
vault_data = load_data()

while True:
   print("-------VAULT------")
   print("1 to append data")
   print("2 to view data ")
   print("3 to save data ")
   print("4 to exit vault")
   choice = input("Enter option (1-4): ")
   match choice:
        case "1":
            add_data(vault_data)
        case "2":
            view_data(vault_data)
        case "3":
            save_data(vault_data)
        case "4":
            break
        case _:
            print("Invalid input")
       
