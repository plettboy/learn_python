#Dictionaries and Nesting
#Dictionnary = {Key: Value, Value, Value}
programming_dictionnaty = {
    "Bug": "Caterpiller",
    "spider": "Ant",
}

#retrieve item from dictionnary
print(programming_dictionnaty['Bug'])

#adding new item to the data dictionnary
programming_dictionnaty['nicole'] = 'wowy'

#deleting things
programming_dictionnaty = {}

#edit item
programming_dictionnaty{"bug"} = "animal"

#to loop through keys 
for key in programming_dictionnaty:
    print(key)

#to loop through values
for key in programming_dictionnaty:
    print(key)
    print(programming_dictionnaty[key])

    #loop through and manipulate an array
    student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] < 70:
        student_grades[key] = "Fail"

    

# 🚨 Don't change the code below 👇
print(student_grades)

#Nesting dictionnaries and lists
nested = {
    key1: [List],
    key2: {dict}
}

travel_log = {
    'france': ['paris', 'lyonne', 'marseille']

}

new_travel = {
    'france': {cities: [paris, marseille],}
}

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = visits
    new_country['cities'] = cities
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)