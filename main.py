# numbers = [1, 2, 3]
# keyword format for list comprehension
# easier method of creating new lists instead of using a for loop
# new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# this will also work for other things. like strings and other sequences. list, range, string, and tuple.
# use the format:
# name = "Angela"
# new_list = [letter for letter in name]
#
# new_list = [letter for letter in name]
# print(new_list)

# number_range = range(1, 5)
# new_list = [number * 2 for number in number_range]
# print(new_list)
#
# # conditional list comprehension - will check against condition before looping through sequence.
# # new_list = [new_item for item in list if test]
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# # short_names = [name for name in names if len(name) < 5]
# caps_names = [name.upper() for name in names if len(name) > 5]
# print(caps_names)

# Dictionary Comprehension
# in the format:
# new_dict = {new_key:new_value for item in list}

# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)
# print(students_scores['Alex'])
# # passed_students = {student:students_scores[student] for student in students_scores if students_scores[student] >= 60}
# passed_students = {student:score for (student, score) in students_scores.items() if students_scores[student] >= 60}
# print(passed_students)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# convert dictionary to items and convert temp to fahrenheit.
# items in dictionary become tuple. have to conert so you can loop through the values.
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
#
# print(weather_f)

student_dict = {
    "student": ["Angela", "james", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_df = pandas.DataFrame(student_dict)
# print(student_df)

# loop through pandas dataframe. using for loop with items() method on rows only shows the values, which isn't great.
# for (key, value) in student_df.items():
#     print(value)
# pandas has a built in iterrows() method for looping through rows of a data frame.
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)