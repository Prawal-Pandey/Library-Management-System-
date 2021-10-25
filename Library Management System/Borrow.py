import Date
import ListSplit

def borrowBook():
    success=False
    while(True):
        firstName=input("Enter the first name of the borrower:  ")
        if firstName.isalpha():
            break
        print("Please input alphabet from A to Z!")
    while(True):
        lastName=input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("Please input alphabet from A to Z!")
            
    t="D:\\Library Management System\\Data of Users\\Borrow-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("                  Library Management System  \n")
        f.write("                        Borrowed By: "+ firstName+"  "+lastName+"\n")
        f.write("    Date:-  " + Date.getDate()+"    Time: "+ Date.getTime()+"\n\n")
        f.write("S.N. \t\t Book Name \t       \t\t\t\t Author Name \n" )
    
    while success==False:
        print("Please select an option from below:    ")
        for i in range(len(ListSplit.bookname)):
            print("Enter", i, "to borrow the book", ListSplit.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.quantity[a])>0):
                    print("The book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(0,7):
                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"Rs."+ListSplit.cost[i]+"\n")


                    #if user wants more books
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow few more books? However, you cannot borrow the same book twice. Press y for yes and n for no. \n"))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListSplit.bookname)):
                                print("Enter", i, "to borrow book", ListSplit.bookname[i])
                            a=int(input())
                            if(int(ListSplit.quantity[a])>0):
                                print("The book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                                ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(0,7):
                                        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"Rs."+ListSplit.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thanks for borrowing the books from us. :)")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Sorry,The book is not available !")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose the book according to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")