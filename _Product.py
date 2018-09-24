#product
#2018 09 18
#Cheung Anthony

# Attributes:

# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"

# Methods:

# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return Item: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
# Display Info: show all product details.  
# Every method that doesn't have to return something should return self so methods can be chained.

class Product:
    status="For Sale"
    count=0
    def __init__(self,price,item_name,weight,brand,status):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.status=status        
    def sell(self,newstatus=''):
        if newstatus.strip():
            self.status="sold"            
            return self          
        if not newstatus.strip():
            print("blanky\n")
            return self
    def tax(self,tax=''):
        taxstr=str(tax)
        if taxstr.strip():
            self.price=(self.price)*(1+(tax/100))
            return self          
        if not taxstr.strip():
            print("blanky\n")
            return self
    def reason_for_return(self,refund=''):
        refundstr=str(refund)
        if refundstr=="defective":
            self.price=0
            self.refund="Reason for return: Defective"
            return self          
        if refundstr=="like new":
            self.price=self.price
            self.refund="Reason for return: Like New"
            self.status="For sale"            
            return self          
        if refundstr=="opened":
            self.price=self.price-(self.price*.20)
            self.refund="Reason for return: Opened"
            self.status="Used"            
            return self            
        if not refundstr.strip():
            print("refund blanky\n")
            self.refund="Reason for return: N/A"
            return self
    def displayInfo(self):
        print("Price: " + "{:.2f}".format(self.price)+ "\nItem Name: "+ self.item_name + "\nWeight: "+ self.weight  +"\nStatus: " +self.status + "\n" +self.refund +"\n")
        return self
product1=Product(2,"milk","16oz","Dean's","For Sale")
product2=Product(20000,"diamond ring","2ct","Generic","For Sale")
#product1.sell("yes").tax(5).reason_for_return("opened").displayInfo()
product2.sell().tax().reason_for_return().displayInfo()

# decimals
# def myformat(x):
#     return ('{:.2f}'.format(x))
# myformat(1.00)
# print(myformat(1.00))

#     def cnt(self, newcount=''):
#         newcountstr=str(newcount)
#         if newcountstr.strip():
#             self.count=newcount
#             print(str(self.count))            
#             print("not 
# blanky")
#             return self
#         if not newcountstr.strip():
#             self.count=newcount
#             print("blanky")
#             return self
















# class Product:
#     status="For Sale"
#     count=0
#     def __init__(self,price,item_name,weight,brand,status):
#         self.price=price
#         self.item_name=item_name
#         self.weight=weight
#         self.brand=brand
#         self.status=status        
#     def sell(self,newstatus=''):
#         if newstatus.strip():
#             self.status="sold"            
#             print("Update Status: Sold\n")   
#             return self          
#         if not newstatus.strip():
#             print("wft\n")
#             return self            
#     def displayInfo(self):
#         print("Price: "+ str(self.price)+ "\nItem Name: "+ self.item_name + "\nWeight: "+ self.weight  +"\nStatus: " +self.status +"\n")
#         return self
# product1=Product(2,"milk","16oz","Dean's","For Sale")
# product2=Product(2,"milk","16oz","Dean's","For Sale")
# product1.sell("yes").displayInfo()
# product2.sell().displayInfo()


# class Product:
#     status="For Sale"
#     count=0
#     def __init__(self,price,item_name,status,count):
#         self.price=price
#         self.item_name=item_name
#         self.status=status
#         self.count=count
#     def cnt(self, newcount=''):
#         newcountstr=str(newcount)
#         if newcountstr.strip():
#             self.count=newcount
#             print(str(self.count))            
#             print("not 
# blanky")
#             return self
#         if not newcountstr.strip():
#             self.count=newcount
#             print("blanky")
#             return self    
#     def displayInfo(self):
#         print("Price: "+ str(self.price)+ "\nItem Name: "+ self.item_name + "Status: " +self.status + " " + str(self.count))
#         return self

# product1=Product(2,"milk","For Sale",1)
# product1.displayInfo().cnt()
# product2=Product(1,"pencil","1oz","Generic","For Sale")
# product3=Product(200000,"diamond ring","4ct","Generic","For Sale").logout(Sell)

 

# product1.price().item_name().weight().brand().status()
# product2.displayInfo().logut
# product3.displayInfo()

 
#

# https://stackoverflow.com/questions/45860417/chaining-instance-methods-in-python


# class User:
#     # this method to run every time a new object is instantiated
#     def __init__(self, name, email):
# 	# instance attributes 
#         self.name = name
#         self.email = email
#         self.logged = True
#     # login method changes the logged status for a single instance (the instance calling the method)
#     def login(self):
#         self.logged = True
#         print(self.name + " is logged in.")
#         return self
#     # logout method changes the logged status for a single instance (the instance calling the method)
#     def logout(self):
#         self.logged = False
#         print(self.name + " is not logged in")
#         return self
#     # print name and email of the calling instance
#     def show(self):
#         print("test = " + self.name + " test2=")
#         return self

# user1=User("firstlast","firstlast@email")
# user1.login().show().logout()



# class Car:
#     price=0
#     tax=0
#     def __init__(self,price,speed,fuel,mileage):
#         self.price=price
#         self.speed=speed
#         self.fuel=fuel
#         self.mileage=mileage
#     def display_all(self):
#         if self.price > 10000:
#             self.tax=0.15
#         else:
#             self.tax=0.12
#         print("Price: "+ str(self.price)+ "\nSpeed: "+ self.speed + "\nFuel: "+ str(self.fuel) + "\nMileage: "+ str(self.mileage) +"\nTax: " +str(self.tax) + "\n")
#         return self
# car1=Car(2000,"35mph","Full","15mpg")
# car2=Car(2000,"5mph","Not Full","105mpg")
# car3=Car(2000,"15mph","Kind of Full","95mpg")
# car4=Car(2000,"25mph","Full","25mpg")
# car5=Car(2000,"45mph","Empty","25mpg")
# car6=Car(20000000,"35mph","Empty","15mpg")

# car1.display_all()
# car2.display_all()
# car3.display_all()
# car4.display_all()
# car5.display_all()
# car6.display_all()


# class car:
#     miles=0

#     def __init__(self,price,max_speed,miles):
#         self.price=price
#         self.max_speed=max_speed
#         self.miles=miles
# #        self.ride=ride
# #        self.reverse=reverse
# #    def rev()
#     def displayInfo(self):
#         print("price=" + str(self.price)+ ", Maximum speed="+ self.max_speed +", Total Miles="+str(self.miles))
#         return self
# car1=car(200,"25mph",1)
# car1.displayInfo()


# import random
# def randInt(min='', max=''):
#     newmin=str(min)
#     newmax=str(max)
#     if not newmin.strip() and not newmax.strip():
#         print("both min and max blanky", max)
#         return(abs(round((random.random()*100))))
#     elif not newmin.strip() and newmax.strip():
#         print("max not blanky and min blanky", max)   
#         return(abs(round((random.random()*max)))          )
#     elif newmin.strip() and not newmax.strip():
#         print("min not blanky and max blanky", min) 
#         return(abs(round((random.random()*min-100))))
#     else:
#         print("both not blanky")
#         return(abs(round((random.random()*min-max))))
# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
# print(randInt(min=50, max=500))