import pandas


# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         # print(row)
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)
# print(data["temp"].mean())
#
# maximum = data["temp"].max()
# print(maximum)

# # get data columns
# print(data["condition"])
# print(data.condition)

# get data rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday)
print(monday.temp)
monday_temp = monday.temp[0]
print(monday_temp)
temp_f = (9/5) * monday_temp + 32
print(temp_f)

# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# SQUIRREL EXERCISE

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240914.csv")
colors_filtered = squirrel_data["Primary Fur Color"].dropna()
fur_color = colors_filtered.unique()
# print( fur_color )

# count occurrences of each fur color
counts = []
for color in fur_color:
    counts.append( int(colors_filtered.value_counts()[color] ))
# print(counts)

squirrel_dict = {
    "Fur Color": fur_color,
    "Count": counts
}

fur_data = pandas.DataFrame(squirrel_dict)
fur_data.to_csv("squirrel_count.csv")
