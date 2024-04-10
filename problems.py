frens = ['mugu', 'fagu', 'j2', 'rabbi', 'tasfik']
message = ['ekta kutta', 'I hate', 'is a time saver', 'is a romantic vehicle', 'I wish to have a nightstay on a', 'It is my dream to have a journey by a']
print(f'{frens[0]} {message}')
print(f'{frens[1]} {message}')
print(f'{frens[2]} {message}')
print(f'{frens[3]} {message}')
print(f'{frens[4]} {message}')


vehicle = ['car', 'bike', 'cycle', 'boat', 'ship']
print(f'{message[1]} {vehicle[0]}')
print(f'{vehicle[1]} {message[2]}')
print(f'{vehicle[2]} {message[3]}')
print(f'{message[4]} {vehicle[3]}')
print(f'{message[5]} {vehicle[4]}')

#Problem 2
#making list for inviting guests 

guests = ['rabbi','fagu','mugu','fija','vija']
mess = ["you're invited to have dinner together at my home","I found a bigger dinner table!","I'm extremely sorry, I can only invite two people!","I'm sorry for that I couldn't invite you!", "You're still invited!"]
#print(f'Dear {guests[0].title()} {mess}')
#print(f'Dear {guests[1].title()} {mess}')
#print(f'Dear {guests[2].title()} {mess}')
#print(f'Dear {guests[3].title()} {mess}')
#print(f'Dear {guests[4].title()} {mess}')

#absent = guests[4]
#print(guests) 

#print(f'Dear {guests[0].title()} {mess[0]}')
#print(f'Dear {guests[1].title()} {mess[0]}')
#print(f'Dear {guests[2].title()} {mess[0]}')
#print(f'Dear {guests[3].title()} {mess[0]}')
#print(f'Dear {guests[4].title()} {mess[0]}')


#print(f'Dear {guests[0].title()}, {mess[1]}')
#print(f'Dear {guests[1].title()}, {mess[1]}')
#print(f'Dear {guests[2].title()}, {mess[1]}')
#print(f'Dear {guests[3].title()}, {mess[1]}')
#print(f'Dear {guests[4].title()}, {mess[1]}')

#adding new guests

guests.insert(0, 'polok')
guests.insert(2,'lappu')
guests.append('Ihsan')


print(guests)
#print(f'Dear {guests[0].title()} {mess[0]}')
#print(f'Dear {guests[1].title()} {mess[0]}')
#print(f'Dear {guests[2].title()} {mess[0]}')
#print(f'Dear {guests[3].title()} {mess[0]}')
#print(f'Dear {guests[4].title()} {mess[0]}')
#print(f'Dear {guests[5].title()} {mess[0]}')
#print(f'Dear {guests[6].title()} {mess[0]}')
#print(f'Dear {guests[7].title()} {mess[0]}')

#popping out guests from list

print(mess[2])
bad = guests.pop(0)
print(f'{bad} {mess[3]}')
bad = guests.pop(0)
print(f'{bad} {mess[3]}')
bad = guests.pop(0)
print(f'{bad} {mess[3]}')
bad = guests.pop(0)
print(f'{bad} {mess[3]}')
bad = guests.pop(0)                             
print(f'{bad} {mess[3]}')
bad = guests.pop(0)
print(f'{bad} {mess[3]}')

print(f'Dear, {guests[0]} {mess[4]}')
print(f'Dear, {guests[1]} {mess[4]}')

#emptying list

del guests[0]
del guests[0]

print(guests)