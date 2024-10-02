import csv

with open('weather_data.csv', mode='r') as file:
    csvFile = csv.reader(file)
    temperatures = []
    for rows in csvFile:
        if rows[1] != "temp":
            # 當rows[1]不是"temp"的時候，將rows[1]的內容存到temperatures裡面，並將str轉成int。
            temperatures.append(int(rows[1]))
            
    print(temperatures)


