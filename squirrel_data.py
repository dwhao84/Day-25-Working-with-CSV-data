import pandas

from main import new_data

new_data_frame = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# 想辦法印出 Fur color and count:
# Primary Fur Color

grey_squirrels_count = len(new_data_frame[new_data_frame["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(new_data_frame[new_data_frame["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(new_data_frame[new_data_frame["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

squirrels_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [ grey_squirrels_count,cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrels_dict)
df.to_csv("squirrels_count.csv")