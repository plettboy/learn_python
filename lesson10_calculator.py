f_num = input('What is your first number?')
operation = input('What is your operation? (choose multiply, divide, add or subtract)')
l_num = input('What is your second number?')

operations = {
    '+': add,
    "-": subtract,
    '*': multiply,
    '/': divide
}

def calculation(f_num, l_num, operation):
    return(f'{f_num}{operation}{l_num}')

calculation(f_num, l_num, operation)

#while loops, recursion, etc