#Step 1 get the name of Statium
Stadium_name = input("Enter Stadium Name : ")

#Step 2 Print name of the field in uppercase

print(Stadium_name.upper())
#step 3 : get Input for the width and the length of the field
width = float(input('Enter the width of the field in KM :'))
length = float(input('Enter the length of the field in KM :'))

#step 4: print the area of the field

area = width * length
print(f'the area of statdium {Stadium_name} is {area} Square feet')

#step 5 : Calculate the cost per seat without Discount

totalseats = 152905
totalcost = 1000000

costPerSeat = totalcost / totalseats
print(f'the cost perseat without discount is ${costPerSeat:.2f}')

# Step 6 Calcualte the seat cost with a discount 60%
discount = 0.6
discountCostPerSeat = costPerSeat * (1 - discount)
totalSaving = totalcost - (discountCostPerSeat * totalseats)

print(f'cost per seat with 60% discount {discountCostPerSeat:.2f}')
print(f'total Savings {totalSaving: .2f}')

