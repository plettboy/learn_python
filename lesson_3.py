#logical operators
print('welcome to rollerland rollercoaster!')
height = input('What is your height? (cm)')
if height <= 100:
    print('too short')
else:
    print('get on da rollacoasta')

# == equal to, != not equal to, >= <=

#nested IF ELSES

# if condition:
#     if condition:
#         do this
#     else:
#         do this
# else do this

print('welcome to rollercoasta')
height = int(input("How tall you is?"))

if height >= 100:
    print('you good')
    age = int(input('how old you is?'))
    if age >= 10:
        print('get on')
    elif age >= 5:
        print('go on da kids coaster')
    else:
        print('not old enough')
else:
    print('sorry not tall enough')

    # 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(float(weight / (height * height)))

if bmi < 18.5:
    print(f'Your BMI is {bmi}, your are underweight.')
elif bmi >= 18.5 and bmi < 25.0:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi >= 25.0 and bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi >= 30 and bmi < 35:
    print(f'Your BMI is {bmi}, your are obese.')
else:
    print(f'Your BMI is {bmi}, your are clinically obese.')
