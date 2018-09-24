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
            return self
    def tax(self,tax=''):
        taxstr=str(tax)
        if taxstr.strip():
            self.price=(self.price)*(1+(tax/100))
            return self          
        if not taxstr.strip():
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
            self.refund="Reason for return: N/A"
            return self
    def displayInfo(self):
        print("Price: " + "{:.2f}".format(self.price)+ "\nItem Name: "+ self.item_name + "\nWeight: "+ self.weight  +"\nStatus: " +self.status + "\n" +self.refund +"\n")
        return self
product1=Product(2,"milk","16oz","Dean's","For Sale")
product2=Product(20000,"diamond ring","2ct","Generic","For Sale")
product1.sell("yes").tax(5).reason_for_return("opened").displayInfo()
product2.sell().tax().reason_for_return().displayInfo()
