import os
import sys
import pickle

#########################################################################################################
#                                           # CLASS ~ MAIN_MENU
# This is the starting point for the program. It redirects the user to either 'Manage Your Trips' or 
# 'View Your Trips'. The user may also exit the program if they wish.
#########################################################################################################
class Main_Menu: 
 
#********************************************************************************************************  
#                                           # DEF ~ MAIN_MENU
#                                                                                  
# NAME:                (main_menu)    ~     This menu gives the user 6 different options to search for an 
#                                               entry by. (Date, Time, Rider Stars, Miles Driven, 
#                                                          Amount Earned, and Location)
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none    
#********************************************************************************************************                                                
    def main_menu(ride_share_database):
        print("---Ride Share Tracker---\n")
        print("1. Manage Your Trips")
        print("2. View Your Trips")
        print("3. Exit")

        choice =  input("\nSelection: ")
        choice = Validate.validate_choice(choice, 6) # Check if entry is between 1-5.

        # Decide which Subsequent Menu to Open
        if choice == 1:
            Entry_Menu.entry_menu(ride_share_database)
        elif choice == 2:
            View_Menu.view_menu(ride_share_database)
        elif choice == 3:
            sys.exit()
        else:
            print("An error occured, and a valid choice was not provided to the program.")
#_______________________________________________________________________________________________________


#########################################################################################################
                                           # CLASS ~ ENTRY_MENU
# This class is responsible for managing the trip entries in the ride share database. The user can create
# delete, or erase all trip entries that have been previously saved. The user can all return to the main
# menu as well.
#########################################################################################################
class Entry_Menu:
                         
#********************************************************************************************************  
#                                           #DEF ~ ENTRY_MENU
#                                                
# NAME:               (entry_menu)    ~     Displays the Entry Menu for the Ride Share Tracker with seven    
#                                               different options. (Date, Time, Rider Stars, Miles Driven 
#                                               Amount Earned, Location, and Return)
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none       
#********************************************************************************************************                                                       
    def entry_menu(ride_share_database):
        Read_Write_Binary.write_to_file(ride_share_database)

        print("----Manage Trip Menu----")
        print("1. Create New Trip")
        print("2. Delete Trip")
        print("3. Clear All Trips") 
        print("4. Return")
    
        choice =  input("\nSelection: ")
        choice = Validate.validate_choice(choice, 5) # Check if entry is between 1-5.

        # Decide which Subsequent Menu to Open
        if choice == 1:
            Entry_Menu.new_entry(ride_share_database)
        elif choice == 2:
            Entry_Menu.delete_entry(ride_share_database)
        elif choice == 3:
            print("Are you sure you want to clear all entries in the ride share tracker?")
            print("Once this has been done it cannot be undone.")
            choice = Validate.validate_yes_no()
            if choice == 1: # 1 = Yes in Validate
                Entry_Menu.clear_all_entries(ride_share_database)
            else:
                Entry_Menu.entry_menu(ride_share_database)         
        elif choice == 4:
            Main_Menu.main_menu(ride_share_database)
        else:
            print("An error occured, and a valid choice was not provided to the program.")
#--------------------------------------------------------------------------------------------------------


#******************************************************************************************************** 
#                                               #DEF ~ NEW_ENTRY
#                                                  
# NAME:                (new_entry)    ~     This menu gives the user 6 different options to search for an 
#                                               entry by. (Date, Time, Rider Stars, Miles Driven, 
#                                                          Amount Earned, and Location)
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none    
#********************************************************************************************************  
    def new_entry(ride_share_database):
        new_entry = {}
        another = 1
        
        while another == 1:
            print("DATE:")
            # Date
            date = Convert.convert_to_date() # Asks for day, month, and year, then creates a date string.
            new_entry["date"] = date
            # Time
            time = Convert.convert_to_time() # Asks for the hour, minutes, and am or pm
            new_entry["time"] = time
            # Tip Amount
            new_entry["tip_amount"] = input("Tip Amount: ")
            # Miles Driven
            new_entry["miles_driven"] = input("Miles Driven: ")
            #Rider stars
            rider_stars = int(input("Rider Stars: ") )
            rider_stars = Convert.convert_to_stars(rider_stars)
            new_entry["rider_stars"] = rider_stars
            # Amount Earned
            new_entry["amount_earned"] = input("Amount Earned: ")
            # Location
            new_entry["location"] = input("Location: ") 
            
            ride_share_database.append(new_entry)
            new_entry = {}
            
            print("Want to make another selection? ")
            another =  Validate.validate_yes_no()


        Read_Write_Binary.write_to_file(ride_share_database)

        Entry_Menu.entry_menu(ride_share_database)
#--------------------------------------------------------------------------------------------------------


#******************************************************************************************************** 
                                           # DEF ~ DELETE_ENTRY
                                                  
# NAME:             (delete_entry)    ~     This menu gives the user 6 different options to search for an 
#                                               entry by. (Date, Time, Rider Stars, Miles Driven, 
#                                               Amount Earned, and Location) After the entry is found,
#                                               the user can choose to delete the entry.
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none   
#********************************************************************************************************    
    def delete_entry(ride_share_database):
        entry_to_delete = {}
        entry_to_delete = Search.search_menu(ride_share_database)
        
        for index in range(len(ride_share_database)):      
            if ride_share_database[index-1] == entry_to_delete:
                print("The entry has been deleted.\n")
                del ride_share_database[index-1]
        
        
        Read_Write_Binary.write_to_file(ride_share_database)
        
        Entry_Menu.entry_menu(ride_share_database)
#---------------------------------------------------------------------------------------------------------


#********************************************************************************************************* 
                                        # DEF ~ CLEAR_ALL_ENTRIES
                                                  
# NAME:         (clear_all_entries)    ~     The user can completely clear all of the entries in their  
#                                               ride share database. However, they are prompted first
#                                               to comfirm this is the decision they wanted to make.
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none    
#********************************************************************************************************      
    def clear_all_entries(ride_share_database):
        outfile = open("ride_share_database.bin",'wb')
        cleared_entry = []
        pickle.dump(cleared_entry, outfile)
        outfile.close() 

        Entry_Menu.entry_menu(cleared_entry) 
#________________________________________________________________________________________________________


#########################################################################################################
                                           # CLASS ~ VIEW_MENU
# This class is responsible for displaying the trip view menu. The user can either search for an entry
# of display all of then entries. The user can all return to the main menu.
# menu as well.
#########################################################################################################
class View_Menu:
                         
#********************************************************************************************************  
                                            #DEF ~ VIEW_MENU
                                                
# NAME:                (view_menu)    ~     Displays the View Menu for the Ride Share Tracker with three    
#                                               different options. (View All Entries, Search for Entry, 
#                                               and Return)
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none       
#********************************************************************************************************                              
    def view_menu(ride_share_database):
            print("----View Trip Menu----")
            print("1. View All Entries")
            print("2. Search for Entry")
            print("3. Return")
        
            choice =  input("\nSelection: ")
            choice = Validate.validate_choice(choice, 5) # Check if entry is between 1-5.

            # Decide which Subsequent Menu to Open
            if choice == 1:
                View_In_Console.view_all_entries(ride_share_database)
            
            elif choice == 2:
                result_list = []
                result = Search.search_menu(ride_share_database)

                if result == "null":
                    View_Menu.view_menu(ride_share_database)
                else:   
                    result_list.append(result)
                    View_In_Console.save_to_txt(result_list, ride_share_database)
            
            elif choice == 3:
                Main_Menu.main_menu(ride_share_database)
            else:
                print("An error occured, and a valid choice was not provided to the program.")
#________________________________________________________________________________________________________


#########################################################################################################
                                          # CLASS ~ VIEW_IN_CONSOLE
# This class is responsible for displaying the trip entries in the ride share database. The user can 
# search for an individual entry or display all saved entries. After either option, the user can export
# the returned trip/s as a txt file..
#########################################################################################################
class View_In_Console:

#********************************************************************************************************  
#                                        # DEF ~ PRINT_DISPLAY_HEADER
#                                                
# NAME:               (entry_menu)    ~     Custom display header for ease of reading and interpreting    
#                                               the pulled data from the ride share tracker. 
#                                               
# ARGUMENTS:                (none)    ~     none   
#                                                
#
# RETURN:                   (none)    ~     none       
#********************************************************************************************************  
    def print_display_header():
        print("   Date         Time          Rider Stars     Miles Driven     Amount Earned     Location")
        print("--------------------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------------------------------


#********************************************************************************************************  
#                                           # DEF ~ VIEW_ENTRY  
#                                                
# NAME:               (view_entry)    ~     The identified ride share entry is displayed in an easy to 
#                                               read format.    
#                                               
# ARGUMENTS: (rider_share_database)   ~     The "database" of trip entries which is made up of a list 
#                                               of dictionaries. 
#                          (index)    ~     The index the idenitifed entry resides in the database.        

#
# RETURN:                   (none)    ~     none       
#********************************************************************************************************         
    def view_entry(ride_share_database, index):
        print(ride_share_database[index]["date"], end="   \t")
        print(ride_share_database[index]["time"], end="  \t")
        print(ride_share_database[index]["rider_stars"], end="  \t\t")
        print(ride_share_database[index]["miles_driven"], end="\t\t  ")
        print(ride_share_database[index]["amount_earned"], end="     \t")
        print(ride_share_database[index]["location"])    
#--------------------------------------------------------------------------------------------------------


#******************************************************************************************************** 
#                                         # DEF ~ VIEW_ALL_ENTRIES 
#
# NAME:          (view_all_entries)    ~     All of the entries in the ride share tracker are displayed     
#                                               in an easy to read format.
#                                               
# ARGUMENTS: (rider_share_database)   ~     The "database" of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none       
#********************************************************************************************************  
    def view_all_entries(ride_share_database):
        View_In_Console.print_display_header()

        for index in range(len(ride_share_database)):
            View_In_Console.view_entry(ride_share_database, index-1)

        View_In_Console.save_to_txt(ride_share_database, ride_share_database)
#--------------------------------------------------------------------------------------------------------


#********************************************************************************************************
#                                          # DEF ~ SAVE_TO_TXT
#
# NAME:               (save_to_txt)   ~    Displays the View Menu for the Ride Share Tracker with three    
#                                           different options. (View All Entries, Search for Entry, 
#                                               and Return)
#                                               
# ARGUMENTS:     (rider_share_data)   ~    The "database"  of trip entries which is made up of a list 
#                                           of dictionaries, or an individual entry from it. 
# ARGUMENTS: (rider_share_database)   ~     The "database" of trip entries which is made up of a list 
#                                             of dictionaries. 
#
# RETURN:                   (none)    ~     none       
#********************************************************************************************************      
    def save_to_txt(ride_share_data, ride_share_database):
        print("Would you like to save this information as a .txt file?")
        choice = Validate.validate_yes_no()

        if choice == 1:
            file_name = input("Enter a name for the file (without .txt): ")
            file_name = file_name + ".txt"   
            with open(os.path.join(sys.path[0], file_name), "w") as outfile:            
                Write_To_Txt.write_all_entries(ride_share_data, outfile)
        else:
            View_Menu.view_menu(ride_share_database)
#________________________________________________________________________________________________________


#########################################################################################################
#                                           # CLASS ~ SEARCH
# This class is responsible for displaying the trip entries in the ride share database. The user can 
# search for an individual entry or display all saved entries. After either option, the user can export
# the returned trip/s as a txt file. The user can all return to the main menu.
# menu as well.
#########################################################################################################
class Search:                    
                                           
#*********************************************************************************************************  
#                                          # DEF ~ SEARCH_MENU  
#                                                                                        
# NAME:              (search_menu)    ~     This menu gives the user 6 different options to search for 
#                                               an entry by. (Date, Time, Rider Stars, Miles Driven, 
#                                                             Amount Earned, and Location)
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none   
#*********************************************************************************************************                                             
    def search_menu(ride_share_database):

        print("Search for entry by:")
        print("1. Date")
        print("2. Time")
        print("3. Rider Stars")
        print("4. Miles Driven")
        print("5. Amount Earned")
        print("6. Location")
        print("7. Return") # Return to the main menu
    
        choice =  input("\nSelection: ")
        choice = Validate.validate_choice(choice, 7) # Check if entry is between 1-7.
        
        # Date
        if choice == 1:           
            date = Convert.convert_to_date() # Gets date from user and then converts to correct format
            return Search.search("date", date, ride_share_database)
        
        # Time
        elif choice == 2:
            print("Still need to make the function to accept time and am or pm")
            
        # Rider Stars
        elif choice == 3:
            rider_stars = input("Rider Stars: ")
            rider_stars = Validate.validate_choice(rider_stars, 5) # ***** 1-5
            Search.search("rider_stars", rider_stars, ride_share_database)
            
        # Miles Driven
        elif choice == 4:
            miles_driven = input("Miles Driven: ")
            miles_driven = Validate.validate_choice(miles_driven, 2000) # Generous end number
            Search.search("miles_driven", miles_driven, ride_share_database)
            
        # Amount Earned
        elif choice == 5:
            amount_earned = input("Amount Earned: ")
            amount_earned = Validate.validate_choice(amount_earned, 1000000) # Arbitrary end number
            Search.search("amount_earned", amount_earned, ride_share_database)
            
        # Location
        elif choice == 6:
            location= input("Location: ")
            Search.search("location", location, ride_share_database)
            
        # Main Menu
        elif choice == 7:
            return
        else:
            print("An error occured, and a valid choice was not provided to the program.")  
#--------------------------------------------------------------------------------------------------------                                               

#******************************************************************************************************** 
#                                               # DEF ~ SEARCH       
#                                         
# NAME:                   (search)    ~     This function looks for an entry in the ride share "database" 
#                                               by a key sent by a (python) function. If it is unable to
#                                               it alerts the user and returns to the search menu.
#                                               
# ARGUMENTS:           (parameter)    ~     The key that that functions looks through the database for. 
#                                               
#                          (value)    ~     The value for the key in the database they are searching for
#                                                the entry by.
#            (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries.
#
# RETURN:          (correct_entry)    ~     String of asterisks returned as the new rider_stars variable. 
#********************************************************************************************************                                               
    def search(parameter, value, ride_share_database):
        correct_entry = {}
        index = -1
        choice = ""
        found = False
        for entry in ride_share_database:
            
            index += 1
            if entry[parameter] == value:
                print("Index", index)
                print("   Date         Time          Rider Stars     Miles Driven     Amount Earned     Location\n")
                print("--------------------------------------------------------------------------------------------\n")
                View_In_Console.view_entry(ride_share_database, index)
                
                print("Is this the correct entry?")
                choice = Validate.validate_yes_no()                                                                      

            if choice == 1: # Yes = 1
                found = True
                correct_entry = entry
                break

        if found == False:
            print("\nUnable to locate the entry by the search terms provided.\n")
            return "null"
        
        return correct_entry
#________________________________________________________________________________________________________

#########################################################################################################
#                                           # CLASS ~ READ_WRITE_BINARY
# This class is responsible for saving and writing changes made by the user to a binary file. This format
# makes it harder for people to look at the saved information without creating a protected file or having
# a program that can read those files.
#########################################################################################################
class Read_Write_Binary:

#********************************************************************************************************
#                                           # DEF ~ READ_FILE
#
# NAME:            (read_file)    ~     This function checks if a binary file exists for the program. If 
#                                           not it will create a binary file. It then passes the 
#                                            database from the save file or a blank list to use as it.
#                                                          Amount Earned, and Location)
#                                               
# ARGUMENTS:             (none)    ~    none
#
# RETURN: (ride_share_database)    ~    The "database" of trip entries which is made up of a list 
#                                           of dictionaries.  
#********************************************************************************************************
    def read_file():
        try:
            infile = open("ride_share_database.bin",'rb')
            ride_share_database = pickle.load(infile) 
            infile.close()
        except:
            outfile = open("ride_share_database.bin",'wb')
            ride_share_database = []
            pickle.dump(ride_share_database, outfile)
            outfile.close()  
        
        return ride_share_database
#---------------------------------------------------------------------------------------------------------
 

#********************************************************************************************************
#                                       # DEF ~ WRITE_TO_FILE
#
# NAME:            (write_to_file)    ~     This function write the changes made by the user to the binary 
#                                               file for future use. 
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none    
#******************************************************************************************************** 
    def write_to_file(ride_share_database):
        outfile = open("ride_share_database.bin",'wb')
        pickle.dump(ride_share_database, outfile)
        outfile.close()   
#________________________________________________________________________________________________________


#########################################################################################################
#                                           # CLASS ~ WRITE_TO_TXT
# This class is responsible for exporting the user's data in an easy to read format to a .txt file. It 
# will either export a single entry or the entire ride share database.
#########################################################################################################
class Write_To_Txt:

    def write_entry(ride_share_data, index, outfile):
            amount_earned = ride_share_data[index]["amount_earned"]

            outfile.write(ride_share_data[index]["date"] + "   \t" + 
                        ride_share_data[index]["time"] + "  \t" +
                        ride_share_data[index]["rider_stars"] + "  \t\t" +
                        str(ride_share_data[index]["miles_driven"]) + "\t\t  " +
                        str(amount_earned) + "     \t" +
                        ride_share_data[index]["location"] + "\n")
            
             
#********************************************************************************************************
#                                       # DEF ~ WRITE_ALL_ENTRIES
#
# NAME:            (write_to_file)    ~     This menu gives the user 6 different options to search for an 
#                                               entry by. (Date, Time, Rider Stars, Miles Driven, 
#                                                          Amount Earned, and Location)
#                                               
# ARGUMENTS: (rider_share_entries)    ~     The "database"  of trip entries which is made up of a list 
#                                               of dictionaries. 
#
# RETURN:                   (none)    ~     none    
#********************************************************************************************************     
    def write_all_entries(ride_share_database, outfile):       
            outfile.write("   Date         Time          Rider Stars     Miles Driven     Amount Earned     Location\n")
            outfile.write("--------------------------------------------------------------------------------------------\n")
            for index in range(len(ride_share_database)):
                Write_To_Txt.write_entry(ride_share_database, index, outfile)  
            outfile.close()
            View_Menu.view_menu(ride_share_database) 



#########################################################################################################
#                                           # CLASS ~ CONVERT
# This class includes the functions: (convert_to_date, convert_to_time, convert_to_stars, 
# validate_choice, and validate am_pm). These functions are then used by the other python files to check 
# the user data submitted.
#########################################################################################################
class Convert:
                               
#********************************************************************************************************
#                                            # CONVERT_TO_DATE
#                          
# NAME:  (convert_to_date)    ~     This function gets the month, day, and date from the user. It then 
#                                       validates them using (validate_choice) function. Finally, it 
#                                       sends back the converted date as a string to the (Entry_Menu) 
#                                       class as the (date) variable.
#
# ARGUMENTS:        (none)    ~     none
#     
# RETURN: (converted_date)    ~     String sent back to user from the converted information.
#********************************************************************************************************
    def convert_to_date():
        month = input("Month: ")
        month = Validate.validate_choice(month, 12)
        day = input("Day: ")
        day = Validate.validate_choice(day, 31)
        year = input("Year: ")
        year = Validate.validate_choice(year, 2200)
        
        converted_date = str(month) + "/" + str(day) + "/" + str(year)
            
        return converted_date   
#--------------------------------------------------------------------------------------------------------
 

#********************************************************************************************************    
                                           # CONVERT_TO_TIME
                                    
# NAME: (convert_to_time)     ~     This function gets the hours, minutes, and am or pm from the user.
#                                       it then validates the input, and then converts it to an easy
#                                       to read string.        
#
# ARGUMENTS:       (none)     ~     none
#                  
# RETURN:   (time_output)     ~     This string is made of the hours, minutes, and am pm. It adds
#                                       the : and a space between minutes and am or pm.  
#********************************************************************************************************      
    def convert_to_time():
        print("TIME:")
        # Hours
        hours = input("Hour: ")
        hours = Validate.validate_choice(hours, 12)
        # Minutes
        minutes = input("Minutes: ")
        minutes = Validate.validate_choice(minutes, 60)
        
        if minutes < 10:
            minutes = "0" + str(minutes)
        
        # AM or PM
        am_pm = input("AM/PM: ")
        am_pm = Validate.validate_am_pm(am_pm)

        time_output = str(hours) + ":" + str(minutes) + " " + am_pm     # formatted string

        return time_output
#--------------------------------------------------------------------------------------------------------


#********************************************************************************************************
                                          # DEF ~ CONVERT_TO_STARS    

# NAME: (convert_to_stars)    ~     Converts the number from the (rider_stars) variable in the 
#                                       (Entry_Menu) class to asterisks. Ex: ***** for 5 
#
# ARGUMENTS:       (stars)    ~     Original rider_stars variable sent as an int. 
#
# RETURN:      (new_stars)    ~     String of asterisks returned as the (new) rider_stars variable.
#********************************************************************************************************
    def convert_to_stars(stars):
        new_stars = ""
        while stars > 0:
            new_stars += "*"
            stars -= 1
        
        return new_stars    
#________________________________________________________________________________________________________    


#########################################################################################################
#                                           # CLASS ~ VALIDATE
# Checks If Information Sent by User Was a Valid Option or Choice. It validates int, am/pm and yes or no.
#########################################################################################################
class Validate:
                                                     
#********************************************************************************************************
#                                           # DEF ~ VALIDATE_CHOICE    
#                                   
# NAME: (validate_choice)     ~     This function checks if the input sent was numeric and greater than 
#                                       zero. Also, that it is less than the constraint the (python) 
#                                       class sent. Then it returns the choice converted to int.  
#
# ARGUMENTS:     (choice)     ~     The string input sent from the python class making a decision.
#                  (nums)     ~     The constraint that determines what the choice cannot be 
#                                       greater than. 
#                   
# RETURN:     int(choice)     ~     Once the choice is validated it is converted from string to int.
#********************************************************************************************************
    def validate_choice(choice, nums):
        keep_looping = True

        while keep_looping == True:
            if choice.isdigit():
                # while 14 < 0 and 14 > 12
                while int(choice) < 0 or int(choice) > nums:
                    print("Invalid Choice. Choice must be between 1-", 
                    str(nums), ".", sep="")
                    choice = input("\nSelection: ")
                
                keep_looping = False
            else: 
                print("Invalid Choice. Choice must be numeric.")
                choice = input("\nSelection: ")
        
        return int(choice)   
#--------------------------------------------------------------------------------------------------------


#********************************************************************************************************
#                                         # DEF ~ VALIDATE_AM_PM
#                                      
# NAME:   (validate_am_pm)    ~     Checks if the (am_pm) variable provided by user was valid. If not,  
#                                       it will loop until it is. Then it returns it to the 
#                                       (Entry_Menu) class. 
#
# ARGUMENTS: (am_pm_input)    ~     User input for the am_pm variable.
#
# RETURN:    (am_pm_input)    ~     (am_pm) variable after being validated and lower-cased. 
#********************************************************************************************************      
    def validate_am_pm(am_pm_input):
        keep_looping = True

        while keep_looping == True:
            if am_pm_input  != "am" \
            and am_pm_input != "AM" \
            and am_pm_input != "pm" \
            and am_pm_input != "PM":
                am_pm_input = input("Invalid Choice. Choice must be am or pm: ")
            else:
                keep_looping = False

        return am_pm_input.lower()
#--------------------------------------------------------------------------------------------------------

                     
#********************************************************************************************************
#                                        # DEF ~ VALIDATE_YES_NO
#
# NAME: (validate_yes_no)    ~      Checks if the user entered a 1 or a 2 for the prompt. If not,  
#                                       it will loop until it is. Then it returns it to the a 
#                                       function
#
# ARGUMENTS:       (none)    ~      User input for the am_pm variable.
#
# RETURN:        (choice)    ~     Returns Yes or No (1 or 2) 
#********************************************************************************************************
    def validate_yes_no():
            print("1. Yes")
            print("2. No")

            choice =  input("\nSelection: ")
            choice = Validate.validate_choice(choice, 2) # Check if entry is Yes or No by checking 1 or 2
            
            return choice 
#--------------------------------------------------------------------------------------------------------

#________________________________________________________________________________________________________
                                            # END OF FILE