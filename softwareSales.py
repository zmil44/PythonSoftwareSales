"""
Zach Miller
9/23/2013
Software Sales
"""

#gets purchase amount, determines discount and total amount
#then passes them to showPurchase
def main():
    purchaseAmount= int(input('Enter the number of packages to purchase '))
    retail=(purchaseAmount * 99)
    discountAmount=0
    totalAmount=0
    if (purchaseAmount>=10 and purchaseAmount<=19):
        discountAmount=(retail*.2)
    elif(purchaseAmount>=20 and purchaseAmount<=49):
        discountAmount=(retail*.3)
    elif(purchaseAmount>=50 and purchaseAmount<=99):
        discountAmount=(retail*.4)
    elif(purchaseAmount>=100):
        discountAmount=(retail*.5)
    totalAmount=(retail-discountAmount)
    showPurchase(discountAmount, totalAmount)

#prints discount amount and total amount
def showPurchase(discount,total):
    print('Discount Amount: $',format(discount,'.2f'))
    print('Total Amount: $',format(total,'.2f'))

#main function
main()
