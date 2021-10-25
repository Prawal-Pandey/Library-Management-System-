import ListSplit
import Date
def returnBook():
    name=input("Enter the name of Borrower:  ")
    a="D:\\Library Management System\\Data of Users\\Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("Rs.") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("OOPS !\nThe borrower name is incorrect.")
        returnBook()

    b="D:\\Library Management System\\Data of Users\\Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System   \n")
        f.write("                   Returned By:    "+ name+"\n")
        f.write("    Date: " + Date.getDate()+"    Time:"+ Date.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(0,7):
        if ListSplit.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\tRs."+ListSplit.cost[i]+"\n")
                ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
            total+=float(ListSplit.cost[i])
            
    print("\t\t\t\t\t\t\t"+"Rs."+str(total))
    print("Is the book return date expired ?")
    print("Press Y for Yes or N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=5*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: Rs."+ str(fine)+"\n")
        total=total+fine
    
    print("Final Total:     "+ "Rs."+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: Rs."+ str(total))
    
        
    with open("Stock.txt","w+") as f:
            for i in range(0,7):
                f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"Rs."+ListSplit.cost[i]+"\n")