number = ['1', '2', '3', '4', '5']
print(number[1*4])

number = ['1', '2', '3', '4', '5', '6', '7']
print(number[3])

name = 'hello'
print(name[1])

print('''available products:
    
butter(1), milk(2), cheese(3)
meat(4), ketchup(5), mayo(6)
noodles(7), eggs(8), bacon(9)''')

user_input = int(input('enter product number: '))

products = ['butter(1)', 'milk(2)', 'cheese(3)'
            'meat(4)', 'ketchup(5)', 'mayo(6)'
            'noodles(7)', 'eggs(8)', 'bacon(9)']

user_choice = products[user_input-1]
print('you recived' + user_choice)