# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Mercedes Gonzalez Gonzalez, 08/09/2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open("ToDoList.txt", "r+")
    for row in objFile:
        item, value = row.split(",")
        dicRow = {"item": item.strip(), "value": value.strip()}
        lstTable.append(dicRow)
    objFile.close()
except Exception as error:
    print("Error detected while attempting to open and/or read file 'ToDoList.txt': {}".format(error))

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) > 0:
            for dicRow in lstTable:
                print("Item: {} | Value: {}".format(dicRow["item"], dicRow["value"]))
        else:
            print("The table of items is currently empty. Please add items to the table")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newItem = input("Please enter a new item: ")
        try:
            newFloatValue = float(input("Please enter a value for the new item: $"))
        except ValueError as error:
            print("The Value provided is not a number. Please introduce a number next time")
        except Exception as error:
            print(error)
        else:
            lstTable.append({"item": newItem.strip(), "value": newFloatValue})
            print("Thank you! The data provided has been added to the table")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("You have selected to remove an existing item from the list/Table")
        itemToRemove = input("Please, provide the name of the item you wish to remove: ")
        found = False
        for dicRow in lstTable:
            if itemToRemove.strip().lower() == dicRow["item"].lower():
                lstTable.remove(dicRow)
                found = True
                print("The item selected has been successfully removed!")
                break
        if not found:
            print("The item you selected was not found in the table." \
                  " Please make sure you are selecting an existing item next time")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w+")
        for dicRow in lstTable:
            objFile.write("{},{} \n".format(dicRow["item"], dicRow["value"]))
        objFile.close()
        print("Data successufully saved to 'ToDoList.txt'")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting the program ... ! Good Bye !")
        break  # and Exit the program
    else:
        print("Please select a menu option from [1 to 5]. Your choice was not valid.")
