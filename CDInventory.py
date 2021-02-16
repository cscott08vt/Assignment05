#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# CScott, 2021-Feb-14, Modified the program
#------------------------------------------#

# Declare variables

strChoice = '' # User input
deleteID = '' # User input for deleting specific ID
lstTbl = []  # list of dictionaries to hold data
dictRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        objFile = open(strFileName, 'r') # Read in txt file
        for row in objFile:
            lstRow = row.strip().split(',')
            dictRow = {'ID':int(lstRow[0]),'Title':lstRow[1],'Artist':lstRow[2]} # Assign indexed data into dictionary values
            lstTbl.append(dictRow)
        objFile.close()
        print('Data Loaded successfully\n')
        loadedData = True
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dictRow={'ID':int(strID),'Title':strTitle,'Artist':strArtist}
        lstTbl.append(dictRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print()
    elif strChoice == 'd':
         print('The current inventory is:')
         print('ID, CD Title, Artist')
         for row in lstTbl:
             print(*row.values(), sep = ', ')
         deleteID = int(input('Type the ID you want to delete: '))
         foundID = False
         for row in lstTbl:
             if deleteID == row['ID']:
                 lstTbl.remove(row)
                 foundID = True
         if foundID == False:
             print('\nID ' + str(deleteID) + ' not found in inventory')
             print()
    elif strChoice == 's':
         # 4. Save the data to a text file CDInventory.txt if the user chooses so
         if loadedData == True: # Execute if the load command was used previously
             objFile = open(strFileName, 'w')
         else:  # Execute if the load command was NOT previously used
             objFile = open(strFileName, 'a')
         for row in lstTbl:
             strRow = ''
             for item in row.values():
                 strRow += str(item) + ','
             strRow = strRow[:-1] + '\n'
             objFile.write(strRow)
         objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

