#LOOPS
#for ITEM in LIST:
#DO SOMETHING TO EACH ITEM
score = 0
fruits = ['apple', 'peach', 'pear']
for x in fruits:
    score += 1
    print(x)
    print(score)

#will loop through each item print it individually
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += int(height)
    number_of_students = len(student_heights)
print(round(total_height / number_of_students))

#FIND THE MAX SCORE FROM STUDENTS
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = 0
for next_score in student_scores:
    if next_score > max_score:
        max_score = next_score

print(f'The highest score in the class is: {max_score}')

#USING FOR LOOPS WITH THE RANGE FUNCTION
#for number in range(a, b):
    #print(number)

#EG print numbers 1 to 10
for number in range(1, 11):
   print(number)

#to add them
for number in range(1, 11):
   sum = 0
   sum += number
   print(sum)

#ADD STEPS
for number in range(1, 11, 2):
   print(number)

#DIFFERENT WAYS OF ADING EVENS
#Write your code below this row 👇
result = 0
for evens in range(2,101,2):
    result += evens

print(result)

new_result = 0
for evens in range(2,101,2):
    if evens % 2 == 0:
        new_result += evens
print(new_result)