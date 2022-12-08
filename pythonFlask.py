batcount = int(input("no.of bats sold:"))
wicketscount = int(input("no.of wickets sold: "))
# if (batcount<=0 or wicketscount<=0):
#     print("enter a positive number")

shoescount = int(input("no.of shoes sold: "))
ballscount = int(input("no.of balls :"))
padscount = int(input("no.of pads: "))

l = [batcount,wicketscount,shoescount,ballscount,padscount]
# using the for loop

# for i in l :
#     print(i)

# totalamount = batcount*500 + wicketscount*300 + shoescount*400
# print("user need to pay:",totalamount)

# using the if_else statement
if ((batcount<=0) or (wicketscount<=0) or (shoescount<=0)):
    print("enter a positive number")
else:
    print('product qunatity with price :')
    totalamount = batcount*200 + wicketscount*300 + shoescount*500
    entries = {batcount: 200, + wicketscount: 300, + shoescount: 500}
    for i,p in entries.items():
        print(i,p)
    print("user need to pay: ",totalamount)