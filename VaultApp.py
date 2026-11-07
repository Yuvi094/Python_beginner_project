
vault_data =[]
def save_data(data_list):
    with open("vault_data.txt", "w") as File:
        for data_list in vault_data:
            data_delimiter = f"{data_list['Id']}|{data_list['Name']}|{data_list['Item']}|{data_list['Bill']}|{data_list['Date']}\n"
            File.write(data_delimiter)
def load_data():
    temp_vault_list = []
    with open("vault_data.txt", "r") as File:
            for data_delimiter in File:
                data_parts = data_delimiter.strip().split("|")
                entry = {
                "Id": data_parts[0],
                "Name": data_parts[1],
                "Item": data_parts[2],
                "Bill": float(data_parts[3]),
                "Date": data_parts[4]
                        
                    }
                temp_vault_list.append(entry)
    return temp_vault_list
                
def add_data(data_list):
    name_business = input("Enter name of business: ")
    item_name = input("Enter the item name: ")
    try:
        bill = float(input("Enter the bill amount: "))
    except ValueError:
        print("This input value in not applicable use a number ")
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
        print(data_list)
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
            for entry in vault_data:
                print(f"ID: {entry['Id']} | Business: {entry['Name']} |Item: {entry['Item']} | Bill: {entry['Bill']} | Date: {entry['Date']}",""  )
        case "3":
            save_data(vault_data)
        case "4":
            break
        case _:
            print("Invalid input")
       
