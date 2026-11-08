import json
import os 
from rich.table import Table
from rich.console import Console
from rich.panel  import Panel
from rich import print
console = Console()
vault_data =[]
vaultData = "vaultData.json"
def save_data(data_list): 
    with open(vaultData , "w" ) as f:
        json.dump(data_list, f , indent=5)
    print("[green]Data has been saved.[/green]")
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
            print("[red]Invalid Input[/red] ")
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
       print("[red]There is no data to be viewed here.[/red]")
       return
    table = Table(title="VAULT")

    table.add_column("Id" , style = "cyan", no_wrap = True)
    table.add_column("Name" , style = "cyan")
    table.add_column("Item" , style = "cyan")
    table.add_column("Bill" , style = "green")
    table.add_column("Date" , style = "cyan")
    
    for entry in data_list:
        table.add_row(
                      str(entry["Id"]),
                      entry["Name"],
                      entry["Item"],
                      f"${entry['Bill']: .2f}",
                      entry["Date"]
                      )
    console.print(table)
vault_data = load_data()

while True:
   console.print(Panel("-------VAULT------", title="Vault ledger", style="bold"))
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
       
