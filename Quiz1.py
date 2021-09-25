# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:24:04 2021

@author: 20bcs115

Client-XYZ
"""
"""
                ---Assumption---
        It is assumed that that are only 3 blood banks in a place which are new,
        People can donate, retrive and get info of each blood bank
"""
class bank:
    
    rare=['AB-', 'O-']
    
    def __init__(self, name, contact, address):
        self.name= name
        self.contact=contact
        self.address=address
        self.donors=[]
        self.blood_group=[]
        self.rare=[]
        self.count=0

    def bankname(self):
        return self.name
    
    
    def bankcontact(self):
        return self.contact
    
    
    def bankaddress(self):
        return self.address
    
    
    def add(self, fullname, blood_group):
        if fullname not in self.donors:
            self.donors.append(fullname)
            self.blood_group.append(blood_group)
            self.count=self.count+1
        
        if blood_group in bank.rare:
            self.rare.append(blood_group)
            
    def retrive(self, bg):
        if bg in self.blood_group:
            print("The blood group is available in the bank!")
            self.donors.remove(self.blood_group.index(bg))
            self.blood_group.remove(bg)
            self.count=self.count-1
        else:
            print("Blood group not available")
            
            
    def bankinfo(self):
        if self.count==0:
            print("No donors in bank")
        else:
            print("\nBlood Bank name", self.name)
            print("\ncontact", self.contact)
            print("\nAddress", self.address)
            print("\n The list of donors are as follows:\n")
            for d in self.donors:
                print(d+" -blood group "+ self.blood_group[self.donors.index(d)]+"\n")
            
            if len(self.rare):
                print("\nRare blood group(s):")
                for r in self.rare:
                    print("\n",r)
            else:
                print("\nRare blood group not available")
                
                
            
         
         
         
"""       
The three blood banks are bank_1, bank2 and bank 3 which are objects of the class bank

""" 

bank_1= bank("KLE", 123, "ad1")  
bank_2= bank("GIM", 456, "ad2")  
bank_3= bank("BIM", 789, "ad3")  

banks=[bank_1, bank_2, bank_3]


def add_donor():
    firstname =input("Enter your name, blood group and number form 0-2 for the blood bank you gotta donate among the 3\n")
    bg=input('')
    num=int(input(''))
    banks[num].add(firstname, bg)
    
    """
    if num == 1:
        bank_1.add(firstbane, bg)
    
    if num == 2:
        bank_2.add(firstbane, bg)   
        
    if num == 3:
        bank_3.add(firstbane, bg)
     """   

def ret_donor():
    bg=print("\nPlease enter blood group and the bank number\n")
    num=int(input(''))
    banks[num].retrive(bg)
   


def blood_info():
    num=int(input('Please enter the bank number from 0-2to get its info '))
    banks[num].bankinfo()


while(1):
    
    enter = int(input("Enter \n1. For blood donation, \n2.For blood retrival, \n3.For blood bank information "))
    
    if enter == 1:
        add_donor()
    
    if enter == 2:
        ret_donor()   
        
    if enter == 1:
        blood_info()
     