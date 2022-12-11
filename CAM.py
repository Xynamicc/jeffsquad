# Computer Assisted Team Management
# Created specifically for the Jeff Squad
# Program by Shane Long
# Discord: Xynamicc#9999
# 
# version: 0.1

import os
from time import sleep

def main():

    def mainMenu():
        print('Please select an option below.')
        print('==============================')
        print('1.) List Staff')
        print('2.) Add or Remove Staff')
        print('3.) Record Time')
        print('4.) Quit\n')
        return
    
    def listStaff():
        sleep(1)
        os.system('cls')
        print('Fetching list of staff...') # FIXME proper loading screen using another function
        sleep(2)

        fList = open('C:\\Users\\Shane\Desktop\\jeffsquad\\CAM\\list.txt', encoding='utf-8')
        for line in fList:
            print(line)
            sleep(0.15)

        userChoice = int(input('Press RETURN to continue.'))
        fList.close()
        return



    def editStaffMenu():
        os.system('cls')
        print('          Staff Roster Application')
        print('============================================')
        print('Would you like to ADD or REMOVE staff?')
        print('1.) ADD')
        print('2.) REMOVE')
        return -1

    editUsername = None
        
    def editStaff(mode):
        # opens the staff management menu. Requires one parameter, either 1 or 2. FIXME
        os.system('cls')
        if mode == 1:
            editUsername = input('Please type the name of the user you would like to ADD: ')
            fAdd = open('C:\\Users\\Shane\\Desktop\\jeffsquad\\CAM\\list.txt', 'a', encoding='utf-8')
            fAdd.write(f'\n{editUsername}')
            fAdd.close()
            sleep(1)
            os.system('cls')
            print('Success!')
            print('User was sucessfully added as a staff member. Exiting application...')
            input('Press enter to exit. ')
        elif mode == 1: # FIXME - This section needs logic that looks for a specifc username and then removes it from the list.txt file.
            editUsername = input('Please type the name of the user you would like to REMOVE: ')
            fAdd = open('C:\\Users\\Shane\\Desktop\\jeffsquad\\CAM\\list.txt', 'a', encoding='utf-8')
            for line in fAdd:
                if line == editUsername:
                    print('1')
            fAdd.close()
        return -1

    def timeClock():
        # opens the time clock module. Eventually will require parameters to pick a specific function.
        # FIXME currently does not do anything.
        return -1

    print(' Jeff Squad Computer Assisted Team Management')
    print(' Use of this software is intended only for members of management of the Jeff Squad!\n',
    'Unauthorized access to this system is prohibited and subject to prosecution to the fullest extent of the law.'
    )
    proceed = str(input('Do you wish to continue? (y/n): '))

    if proceed != 'y':
        exit()
    
    # Menu screen
    os.system('cls') # clears the screen

    mainMenu() # displays the main menu
    userChoice = None
    userChoice = int(input('Please select an option: '))
    
    # Input validation
    while not (userChoice >= 1 and userChoice <= 4):
        os.system('cls')
        mainMenu()
        print('Invalid option. Please try again.')
        userChoice = int(input('Please select an option: '))

    # Function logic    
    if userChoice < 1 or userChoice > 4:
        print('Invalid option. Please try again.')
        os.system('cls')
        mainMenu()
    elif userChoice == 1:
        listStaff()
    elif userChoice == 2:
        editStaffMenu()
        editChoice = None
        editChoice = int(input('Please select an option: '))
        while editChoice not in [1, 2]:
            os.system('cls')
            editStaffMenu()
            print('Invalid option. Please try again.')
            editChoice = int(input('Please select an option: '))
        editStaff(editChoice)
    elif userChoice == 3:
        print('User choice option 3.')
    elif userChoice == 4:
        exit()
        
    
    








main()