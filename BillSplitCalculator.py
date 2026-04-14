totalAmount = float(input("Enter the Total Bill Amount:"))
print("Total Bill Amount is ","₹",totalAmount)
Friends = int(input("Enter the number of friends :"))

IndividualsPay = totalAmount/Friends
print("Each will pay Amount:","₹",IndividualsPay)

print("The data type of TotalAmount is",type(totalAmount))
print("The data type of Friends is:",type(Friends))
print("The data type of IndividualPay is:",type(IndividualsPay))