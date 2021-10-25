# Made by Prawal Pandey
# https://www.linkedin.com/in/prawal-pandey-6a5b7b18b/
# GitHub https://github.com/Prawal-Pandey

import Return
import ListSplit
import Date
import Borrow

def start():
    while(True):
        print("        Welcome to the Library Management System         ")
        print("__________________________________________________________")
        print("Enter 1) To Display")
        print("Enter 2) To Borrow a Book")
        print("Enter 3) To Return a Book")
        print("Enter 4) To Exit\n")
        try:
            a=int(input("Select an option amoung 1-4:   "))
            print()
            if(a==1):
                with open("D:\Library Management System\stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()

            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thanks for using Library Management System")
                break
            else:
                print("Please enter a valid option from 1-4 ")
        except ValueError:
            print("Please input as suggested by the system.")
start()
