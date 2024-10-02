# import pandas and openpyxl
import pandas
import openpyxl
from numpy.ma.extras import average

from csv_practice import temperatures

# read the data by using pandas
data = pandas.read_csv("weather_data.csv")

data_list = data["temp"].to_list()
print(data_list)

all_temperatures = 0

for temp in data_list:
    all_temperatures += temp
    print(temp)

# 取平均溫度
# Method 1
average_temps = all_temperatures / len(data_list)
print(average_temps)

# Method 2
print(data["temp"].mean())

# 找到最大data["temp"]裡面的最大值，用max去找。
print(max(data["temp"]))

# Get Data in first Row
print(data[data.day == "Monday"])

# Find the highest temperature
print(data[data.temp == data.temp.max()])

# 直接找到monday當天的資料。
monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Monday's celsius to Fahrenheit
monday_fahrenheit = monday.temp * 9/5 + 32
print(monday_fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
# Transfer to DataFrame.
new_data = pandas.DataFrame(data_dict)
print(new_data)

# save as CSV file, 在括號裡面輸入自訂的檔案名稱。
new_data.to_csv("new_data.csv")

# print(type(new_dataFrame)) # Name: temp, dtype: int64
# print(new_dataFrame["temp"])
# new_excel = pd.ExcelWriter('sampleFile.xlsx')
# new_dataFrame.to_excel(new_excel, index=True)
# new_excel._save()