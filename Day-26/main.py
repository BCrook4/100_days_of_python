# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# test = sentence.split()
# print(test)
# result = {word:len(word) for word in sentence.split()}
# print(result)

import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

student_data_frame = pandas.DataFrame(data)
print(data)

# loop thru rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(row.students)