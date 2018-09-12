import time
buyerlist=[]
sellerlist=[]

class person:
    def __init__(self):
        self.name=input("Enter your name: ")
        self.add=input("Enter your hostel address: ")
        self.email=input("Enter your email: ")
        self.id=input("Enter your id: ")
        self.phone=input("Enter your phone no: ")
    def display(self):
        print("Name: %s" % (self.name))
        print("Address: %s"%(self.add))
        print("Email: %s"%(self.email))
        print("ID: %s"%(self.id))
        print("Phone:%s "%(self.phone))
class buyer(person):
    def wishlist(self):
        time.sleep(2)
        self.books=int(input("If you want to buy all the books, enter '1' or else enter '0': "))
        time.sleep(1)
        self.labc=int(input("If you want to buy the labcoat, enter '1' else enter '0': "))
        time.sleep(1)
        self.calc=int(input("If you want to buy the calculator,enter '1' or else enter '0': "))
        time.sleep(1)
        self.wishl=[self.books,self.labc,self.calc]
        print("Thank you for entering your wishlist!")
    def __init__(self):
        print("WELCOME TO THE BUYERS SECTION\n---------------------------------------")
        super().__init__()
        self.wishlist()
        self.sum=self.books+self.calc+self.labc
        buyerlist.append((self,sum))
class seller(person):
    def selllist(self):
        self.books=int(input("If you want to sell all the books, enter 1 or else enter '0': "))
        time.sleep(2)
        self.labc=int(input("If you want to sell the labcoat, enter '1' else enter '0': "))
        time.sleep(1)
        self.calc=int(input("If you want to sell the calculator,enter '1' or else enter '0': "))
        time.sleep(1)
        self.price=int(input("Enter the total price of all the above stuff."))
        self.sell=[self.books,self.labc,self.calc,self.price]
    def __init__(self):
        print("WELCOME TO THE SELLERS SECTION\n---------------------------------------")
        
        super().__init__()
        self.selllist()
        self.sum=self.books+self.calc+self.labc+self.price
        sellerlist.append((self,sum))
    def display(self):
        print("Name: %s" % (self.name))
        print("Address: %s"%(self.add))
        print("Email: %s"%(self.email))
        print("ID: %s"%(self.id))
        print("Phone:%s "%(self.phone))
flag=1
while flag==1:

    a=int(input("----------------------------------\n   If you want to buy, Enter '1'\n    If you want to sell, Enter '2'\n   If you want to quit, Enter '0'\n----------------------------------------\n"))
    
    if a==1:
        guy=buyer()
        #guy.wishlist()
        a=input("\nIf you wish to go back to the main menu,press 1 or to find out your bookpop/bookmom, Press '0' \n ")
    elif a==2:
        guy=seller()
        
        #guy.selllist()
        flag=input("\nIf you wish to go back to the main menu,press 1 or to find out your bookson/bookdaughter, Press '0' \n ")
    else:
        break    

sorted(buyerlist,key=lambda x:x[1],reverse=True)
sorted(sellerlist,key=lambda y:y[1],reverse=True)
for i in range(0,len(buyerlist)):
    print("--------------------------------------------------------------------------\nTransaction ID : %s , %s SHOULD BUY THE STUFF FROM %s FOR RS.%s \n --------------------------------------------------------------------------" % (i+1,buyerlist[i][0].name,sellerlist[i][0].name,sellerlist[i][0].price))
txn=0;
ala=input("TO GET THE CONTACT OF BUYER, PRESS 1 . TO GET THE CONTACT OF SELLER, PRESS 2")
if ala==1:
    txn=int(input("\nENTER THE TRANSACTION ID TO GET THE CONTACT OF BUYER \n"))
    buyerlist[txn-1][0].display()
elif ala==2:
    txn=int(input("\nENTER THE TRANSACTION ID TO GET THE CONTACT OF SELLER \n"))
    sellerlist[txn-1][0].display()


