import os
import csv
import math

maxtemp = 0
mintemp=100
maxhumid=0

for file in os.listdir("/home/ahmed/Downloads/weatherdata (1)/weatherdata"):
    if "2002" in file:
        file_path = os.path.join("/home/ahmed/Downloads/weatherdata (1)/weatherdata", file)
        with open(file_path, 'r') as f:
            
            for line in file:
                data = f.readlines()
                csv_reader = csv.reader(data, delimiter=',')
                for row in csv_reader:
                    if len(row)>5:
                        maximumtemp = row[1]
                        
                        if maximumtemp.isdigit():
                            if  int(maximumtemp) > int(maxtemp):
                                    maxtemp = maximumtemp
                                    date1 = row[0]
            
            
                    if len(row)>5:
                        minimumtemp = row[2]
                        if minimumtemp.isdigit():
                            if  int(minimumtemp) < int(mintemp):
                                    mintemp = minimumtemp
                                    date2 = row[0]


                    if len(row)>5:
                        maximumhum = row[6]
                        if maximumhum.isdigit():
                            if  int(maximumhum) > int(maxhumid):
                                    maxhumid = maximumhum
                                    date3 = row[0]
                                    
print (f"on {date1} is the max tempature {maxtemp}")                        
print (f"on {date2} is the min tempature {mintemp}")                           
print (f"on {date3} is the max humid {maxhumid}")
print("--------------------------------------2-----------------------------------------------------------")            

max_temps = []
min_temps = []
humid = []

for file in os.listdir("/home/ahmed/Downloads/weatherdata (1)/weatherdata"):
   if "2005" in file and "Jun" in file:
        file_path = os.path.join("/home/ahmed/Downloads/weatherdata (1)/weatherdata", file)
        with open(file_path, 'r') as f:
            for line in file:
                data = f.readlines()
                csv_reader = csv.reader(data, delimiter=',')
                for row in csv_reader:
                    if len(row)>5:
                        maxs = row[1]
                        if maxs.isdigit():
                            max_temps.append(int(maxs))
                    if len(row)>5:
                        maxs = row[2]
                        if maxs.isdigit():
                            min_temps.append(int(maxs))
                    if len(row)>5:
                        maxs = row[6]
                        if maxs.isdigit():
                            humid.append(int(maxs))
avg_max = sum(max_temps) // len(max_temps)
avg_min = sum(min_temps) // len(min_temps)
avg_humid = sum(humid) // len(humid) 
print(f'Highest Average: {avg_max}')
print(f'Lowest Average: {avg_min}')
print(f'Average Humidity: {avg_humid}')                                            

print("--------------------------------------3-----------------------------------------------------------")      
RED = "\033[91m"
BLUE = "\033[94m"
END = "\033[0m"

for file in os.listdir("/home/ahmed/Downloads/weatherdata (1)/weatherdata"):
   if "2011" in file and "Mar" in file:
        file_path = os.path.join("/home/ahmed/Downloads/weatherdata (1)/weatherdata", file)
        with open(file_path, 'r') as f:
            for line in file:
                data = f.readlines()
                csv_reader = csv.reader(data, delimiter=',')
                for row in csv_reader:
                    if len(row) > 5 and row[0] != "PKT":
                        day = row[0].split("-")[2]
                        max_temp = int(row[1])
                        min_temp = int(row[3])
                        print(f"{day} {RED}{'+' * 10}{END} {max_temp}C")
                        print(f"{day} {BLUE}{'+' * 10}{END} {min_temp}C")
