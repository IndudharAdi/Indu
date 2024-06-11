#Step 1 : Create the list name
print("Original List")
guest = ['Rahul','Laxman', 'Manav', 'Josheph', 'Alex']
print(guest)
print()

#Step 2: Print out personalized message to 3 of them

print("Personalized msg : ")
print(f'Hi {guest[0]} hope you are bringing the cake')
print(f'Hi {guest[3]} don\'t forget the dress code')
print(f'Hi {guest[2]} No messing up with other guests')

# Adding 3 new guests in different Positions
print('Adding rishab in end, sam in the middle and Ram at the starting of the list')

guest.append('Rishab')
guest.insert(0, 'Ram')
guest.insert(len(guest)//2, 'Sam')
print(guest)

#Step 5: Print the length of the string
print('Length of the guest list',len(guest))


import random
#Step 6 Remove 1 Random person and 1 Specific person
print('Removing Manav')
guest.remove('Manav')
print(guest)

print('removing one random Person')
del guest[random.randint(0, len(guest))]
print(guest)
print()

#Step 7: Sort the original list 
sorted_guest = sorted(guest)
print('sorted list of quest: ', sorted_guest)
print()

guest.reverse()
print("reversed sorted list", guest)
