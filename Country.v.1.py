#J.L. Martin CIS261 Week 4 Country Application

# Function to display the header and menu choices for the user def display_menu():
def display_menu():

    print("\n********* Country Guide Menu **********")

    print("1. View all countries --> All ")
    
    print("2. View a specific country --> Key")

    print("3. Add a new country --> Add")

    print("4. Delete a country --> Delete") 

    print("5. Exit")

    print("***************************************")

# Function to pre-populate a dictionary with country names viewing all and viewing via a specific country

def populate_country_dict(): 
    return { "US": "United States", "CA": "Canada", "MX": "Mexico", "TW": "Taiwan", "AU": "Australia", "JP": "Japan", "KR": "Korea (The Republic of)", "DE": "Germany", "IN": "India", "TH": "Thailand", "GB": "Great Britain", "CH": "Switzerland" } 

def view_all(country):
    for i, (key, value) in enumerate(country.items(), start = 1):
        print(f"{i}. {key}: {value}")

def view_key(country):
    key = input("Enter a key value:  ")
    if key in country:
        print(f"{key}: {country[key]}")
    else:
        print("Key not found.")
    
#Function to add a country

def add(country):
    key = input("Enter an abbreviation:  ")
    value = input("Enter country name:  ")
    country[key] = value
    print(f"{country} was added.  \n")

#Function to delete a country

def delete(country):
    key = input("Enter an abbreviation:  ").upper()
    if key in country:
        del country[key]
    
        print(f"{key} was deleted. \n")

    else:
        print("Invalid selection, please try again... \n")


def main():
    country = populate_country_dict()
    display_menu()

    while True:
        command = input("\n Please type a command:  ")
        if command.lower() == "all":
            view_all(country)

        elif command.lower() == "key":
            view_key(country)

        elif command.lower() == "add":
            add(country)

        elif command.lower() == "delete":
            delete(country)

        elif command.lower() == "exit":
            break

        else:
            print("Not valid, please try again...\n")
        
if  __name__ == '__main__':
     main()
     

    
            








