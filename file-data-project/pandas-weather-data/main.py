#-------------- Case 1
# with open("./file-data-project/pandas-weather-data/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#-------------- Case 2
# import csv

# with open("./file-data-project/pandas-weather-data/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

#-------------- Case 3
import pandas 
data = pandas.read_csv("./file-data-project/pandas-weather-data/weather_data.csv")
data.columns = data.columns.str.strip()

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data['temp'].mean())
# print(data['temp'].max())

# # Get data Columns
# print(data['condition'])
# print(data.condition)

# Get data Rows
# print(data[data.day.str.strip() == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data['day'].str.strip() == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Craete a dataframe from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("./file-data-project/pandas-weather-data/new_data.csv")
print(data)
