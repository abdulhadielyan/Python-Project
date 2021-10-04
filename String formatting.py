#String Interpolation
#f-string
#format method

print('This is a string {}'.format('Inserted'))
print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {0} {1}'.format('fox','brown','quick'))
x=int(input("Enter an integer here "))
print('The number is  {}'.format(x))

print("The {f} {b} {q}".format(f='fox',b='brown',q='quick'))

#fstring
name = "Jose"
print(f'Hello, this is {name}')
name = "Sami"
age = 24
print(f'{name} is {age} years old')