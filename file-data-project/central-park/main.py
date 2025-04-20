import pandas

data = pandas.read_csv("./file-data-project/central-park/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv",  
                       on_bad_lines='skip') # Skip error line .csv
data.columns = data.columns.str.strip() # Removes whitespaces

# print(data["Primary Fur Color"].value_counts())
# print(data["Primary Fur Color"].unique())

black_squirrels_count = len(data[data["Primary Fur Color"].str.strip() == "Black"])
gray_squirrels_count = len(data[data["Primary Fur Color"].str.strip() == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"].str.strip() == "Red"])

print(gray_squirrels_count)
print(black_squirrels_count)
print(red_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "red", "Blakc"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./file-data-project/central-park/squirrel_count.csv")
