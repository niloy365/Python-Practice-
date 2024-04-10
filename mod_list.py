#Modifying List
motor = ['honda','kawasaki','suzuki']
motor[0] = 'yamaha'
print(motor)

#Append Method
motor.append('yamaha')
print(motor)

bike = []
bike.append('v3')
bike.append('cg125')
bike.append('rs1')
print(bike)

#Insert method

motor.insert(0, 'pulsar')
print(motor) 

#Del Statement
del motor[0]
print(motor)

#POP method
popped_motor = motor.pop()
print(motor)
print(popped_motor)

last_owned = popped_motor
print(f'The last motorcycle we owned was a {last_owned.title()}')

latest = motor.pop(1)
print(f'Last year I bought a {latest.title()}')

#Remove Method
motor.remove('suzuki')
print(motor)

too_expensive = 'v3'
bike.remove(too_expensive)
print(bike)
print(f'\nA {too_expensive} is too expensive for us')