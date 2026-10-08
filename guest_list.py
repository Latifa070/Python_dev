guests= ['ama', 'abiba','hamdi','rahma']
for guest in guests:
    print (f"Hello, {guest.title()} I'm inviting you to a dinner party")

print(f"\n{guests[1].title()} can't make it to the party")

guests[1]= 'sweetheart'

print('\nPeople that are still invited to the party\n')
for guest in guests:
    print(f'{guest.title()} you are still invited to the party')

print("\nI've found a bigger table I'm inviting more people")
guests.insert(0,'beautiful')
guests.insert(3,'Samira')
guests.append('Assia')

print("\n This is a new list of people coming\n")

for guest in guests:
    print(f"{guest.title()} you are invited to the dinner party")

print("\n I can only invite two people to the party, sorry for any inconvenience caused\n")

removed_guest1 = guests.pop()
print(f"\n{removed_guest1.title()}  sorry for any inconvenience caused")

removed_guest2 = guests.pop()
print(f"\n{removed_guest2.title()}  sorry for any inconvenience caused")

removed_guest3 = guests.pop()
print(f"\n{removed_guest3.title()}  sorry for any inconvenience caused")

removed_guest4 = guests.pop()
print(f"\n{removed_guest4.title()}  sorry for any inconvenience caused")

removed_guest5 = guests.pop()
print(f"\n{removed_guest5.title()}  sorry for any inconvenience caused\n")

for guest in guests:
    print(f"{guest.title()} You're invited ")

del guests[0]
del guests[0]

print(guests)