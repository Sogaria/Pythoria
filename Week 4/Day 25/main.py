#with open("c:\\Users\\Sogaria\\Downloads\\day-25-start\\weather_data.csv") as file:
#    data = file.readlines()

#import csv
import pandas

#with open("Week 4/Day 25/weather_data.csv") as file:
#    data = csv.reader(file)
#    temps = []
#    for item in data:
#       if item[1] != "temp":
#            temps.append(int(item[1]))

#data = pandas.read_csv("Week 4/Day 25/weather_data.csv")
#print(data)

#temp_list = data.temp.to_list() 
#print(temp_list)
#avg_temp = sum(temp_list) / len(temp_list)
#print("Average temp:", data["temp"].mean())
#print("Max temp:", data["temp"].max())

#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#print(monday)
#print(monday_temp)


data = pandas.read_csv("Week 4/Day 25/squirrels.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

dict_squirrels = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
    
}

dataframe_squirrel_count = pandas.DataFrame.from_dict(dict_squirrels)
pandas.DataFrame.to_csv(dataframe_squirrel_count, "Week 4/Day 25/squirrel_count.csv")

