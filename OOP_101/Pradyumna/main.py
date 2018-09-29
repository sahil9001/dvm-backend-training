import time
import json
import requests
import re
import sys

import os.path
from os import path

sellers={
    1:{
        "A1":[],
        "A2":[],
        "A3":[],
        "A4":[],
        "A7":[],
        "A8":[],
        "AB":[],
        "B1":[],
        "B2":[],
        "B3":[],
        "B4":[],
        "B5":[],
        "D2":[]
    },
    2:{
        "A1":[],
        "A2":[],
        "A3":[],
        "A4":[],
        "A7":[],
        "A8":[],
        "AB":[],
        "B1":[],
        "B2":[],
        "B3":[],
        "B4":[],
        "B5":[],
        "D2":[]
    },
    3:{
        "A1":[],
        "A2":[],
        "A3":[],
        "A4":[],
        "A7":[],
        "A8":[],
        "AB":[],
        "B1":[],
        "B2":[],
        "B3":[],
        "B4":[],
        "B5":[],
        "D2":[]
    },
    4:{
        "A1":[],
        "A2":[],
        "A3":[],
        "A4":[],
        "A7":[],
        "A8":[],
        "AB":[],
        "B1":[],
        "B2":[],
        "B3":[],
        "B4":[],
        "B5":[],
        "D2":[]
    }
}

hostelList={
    1:"Vishwakarma Bhawan",
    2:"Krishna Bhawan",
    3:"Gandhi Bhawan",
    4:"Bhagirath Bhawan",
    5:"Ashok Bhawan",
    6:"Rana Pratap Bhawan",
    7:"SR Bhawan",
    8:"Vyas Bhawan",
    9:"Budh Bhawan",
    10:"Ram Bhawan",
    11:"CVR Bhawan",
    12:"Malviya Bhawan",
    13:"Meera Bhawan"
}

currentyear=2018 # A gloal variable that stores the current year


class Person:

    def __init__(self):
        self.takeinput()

    def parse(self):
        self.joinyear=self.id[0:4]
        self.year=str(1+(currentyear-int(self.joinyear)))
        self.branch=self.id[4]+self.id[5]

        try:
            brnch=sellers[1][self.branch]
        except KeyError:
            print("\n Please enter a valid branch indentifier. \n")

        self.email='f'+self.year+self.id[8:12]+"@pilani.bits-pilani.ac.in"
        self.get_coordinate()


    def checkID(self): #Checks the validity of user entered values
        matchid=re.search(r'^201[45678][ABD]\dPS\d\d\d\d[PT]$',self.id)
        if(matchid):
            return True
        else:
            return False
    

    def checkPhone(self):
        matchphone=re.search(r'^\d+$',self.phone)
        if(matchphone):
            return True
        else:
            return False

    def checkHostelID(self):
        matchHostelID=re.search(r'^[1-13]$',self.hostelID)
        if(matchHostelID):
            return True
        else:
            return False

    
    def getHostel(self):
        print("""
            Please enter your hostel number from the list below.

            1. Vishwakarma Bhawan
            2. Krishna Bhawan
            3. Gandhi Bhawan
            4. Bhagirath Bhawan
            5. Ashok Bhawan
            6. Rana Pratap Bhawan
            7. SR Bhawan
            8. Vyas Bhawan
            9. Budh Bhawan
            10. Ram Bhawan
            11. CVR Bhawan
            12. Malviya Bhawan
            13. Meera Bhawan
        """)
        self.hostelID=input()
        while(self.checkHostelID()==False):
            self.hostelID=input("\n You have entered a invalid input. Please enter the correct hostel no.")
        self.add=hostelList[int(self.hostelID)]
        return


    def takeinput(self):
        self.name=input("Enter your name: ")
        self.getHostel()
        self.id=input("Enter your id: ")
        while(self.checkID()==False):
            self.id=input("\nPlease enter correct id: ")
        self.phone=input("\nEnter your phone no: ")
        while(self.checkPhone()==False):
            self.phone=input("\nEnter your phone no: ")
        self.parse()


    def display(self):
        print("Name: %s" % (self.name))
        print("Hostel Name: %s"%(self.add))
        print("Email: %s"%(self.email))
        print("ID: %s"%(self.id))
        print("Phone: %s"%(self.phone))


    def get_coordinate(self):
        resp1=requests.get("http://apis.mapmyindia.com/advancedmaps/v1/pi65d1hf2cf9nelbwdjfzw9yyjxrbxgz/geo_code?addr="+self.add+" BITS Pilani"+"&pin=333031")
        addr11=resp1.json()
        self.lat=addr11['results'][0]['lat']
        self.long=addr11["results"][0]["lng"]


class Buyer(Person): #Buyer class inherits the contact details from the Person class

    def welcome(self):
        print ("\n" * 100) #simple hack to get a clean interface to display buyers section
        print("WELCOME TO THE BUYERS SECTION | PLEASE REGISTER BELOW \n")


    def calculateDistance(self,lat1,long1):
        req=requests.get("http://apis.mapmyindia.com/advancedmaps/v1/pi65d1hf2cf9nelbwdjfzw9yyjxrbxgz/distance?center=%s,%s&pts=%s,%s"%(lat1,long1,self.lat,self.long))
        data=req.json()
        return data['results'][0]['length']


    def displaydata(self):

        print ("\n" * 100) #simple hack to get a clean interface

        if(path.exists('sellers_data.json')): #Check if file doesnt exist.
            pass
        else:
            print("There are not any sellers to display right now. Please check back later \n")
            sys.exit(0)
        with open("sellers_data.json","r") as sellerdata:
            data=json.load(sellerdata)

        print("""
   _____      _ _                _      _     _
  / ____|    | | |              | |    (_)   | |
 | (___   ___| | | ___ _ __     | |     _ ___| |_
  \___ \ / _ \ | |/ _ \ '__|    | |    | / __| __|
  ____) |  __/ | |  __/ |       | |____| \__ \ |_
 |_____/ \___|_|_|\___|_|       |______|_|___/\__|
"""
        )

        print("{:<15} {:<8} {:<15} {:<30} {:<30} {:<30}".format("NAME","ID","PRICE","CONDITION","ADDITIONAL DETAILS","DISTANCE FROM YOU"))
        for a in data[self.year][self.branch]:
            print("{:<15} {:<8} {:<15} {:<30} {:<30} {:<30}".format(a["name"],a["id"],a["Price Quoted"],a["Condition"],a["Additional details"],self.calculateDistance(a["Latitude"],a["Longitude"])))


    def __init__(self):

        self.welcome()
        super().__init__()
        self.displaydata()


class Seller(Person):

    def welcome(self):
        print ("\n" * 100) #simple hack to get a clean interface to display sellers section
        print("WELCOME TO THE SELLERS SECTION | PLEASE REGISTER BELOW \n")

    def checkPrice(self):
        matchprice=re.search(r'^\d+$',self.price)
        if(matchprice):
            return True
        else:
            return False

    def getDetails(self):
        self.price=input("Enter the price that you want to sell your stuff for: ")
        while(self.checkPrice()==False):
            self.price=input("Please enter proper value : ")
        
        self.condition=input("Please enter the condition of your stuff: ")
        self.addDetails=input("Please enter additional details: ")

        sellers[int(self.year)-1][self.branch].append({
                "name" : self.name,
                "id" : self.id,
                "Hostel name" : self.add,
                "Price Quoted" : self.price,
                "Condition" : self.condition,
                "Additional details": self.addDetails,
                "Latitude" : self.lat,
                "Longitude": self.long
            })
        print("\n Thank You for entering the details :)\n")

    def saveData(self):
        with open("sellers_data.json","w") as write_data:
            json.dump(sellers,write_data)

    def __init__(self):
        self.welcome()
        super().__init__()
        self.getDetails()
        self.saveData()


class Driver:

    def __init__(self):
        print("If you want to buy, Enter B\n")
        print("If you want to sell, Enter S\n")
        c=input()
        if(c=='B' or c=='b'):
            user=Buyer()
        elif(c=='S' or c=='s'):
            user=Seller()
        else:
            raise ValueError("\n You can only enter B or S \n")


if __name__=="__main__":
    welcome=Driver()