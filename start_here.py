from functions import *

#########################################################################################################
#                                          # CLASS ~ MAIN
# This program creates a "database" of ride-share trip entries. The user can then add new trips,
# delete ones by searching by category, or clear all entries. They can also view an individual entry or
# all of the entries. Then they may choose after each choice if they want to export the data as a .txt.  
#########################################################################################################
def main():
    ride_share_database = Read_Write_Binary.read_file() 
    Main_Menu.main_menu(ride_share_database) # Entries, Search, Display, Export, Exit

#--------------------------------------------------------------------------------------------------------
main() # Run the main application.