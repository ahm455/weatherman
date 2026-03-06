import os
import csv
path = "/home/ahmed/Downloads/weatherdata (1)/weatherdata"

def yearly_report(year):
    maxtemp = None
    mintemp = None
    maxhumid = None
    date_maxtemp = ""
    date_mintemp = ""
    date_maxhumid = ""

    for file in os.listdir(path):
        if year in file:
            file_path = os.path.join(path, file)
            with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
                lines = [line for line in f if line.strip() and not line.startswith("<")]

                header = [h.strip() for h in lines[0].split(",")]
                csv_reader = csv.DictReader(lines[1:], fieldnames=header)

                for row in csv_reader:
                    row = { (k.strip() if k else ""): v for k, v in row.items() }
                    
                    if row.get('PKT') == 'PKT' or not row.get('PKT'):
                        continue

                    if not row.get('Max TemperatureC') or not row.get('Min TemperatureC') or not row.get('Max Humidity'):
                        continue

                    max_temp_row = int(row['Max TemperatureC'])
                    min_temp_row = int(row['Min TemperatureC'])
                    max_humid_row = int(row['Max Humidity'])
                    date = row['PKT']

                    if maxtemp is None or max_temp_row > maxtemp:
                        maxtemp = max_temp_row
                        date_maxtemp = date
                    if mintemp is None or min_temp_row < mintemp:
                        mintemp = min_temp_row
                        date_mintemp = date
                    if maxhumid is None or max_humid_row > maxhumid:
                        maxhumid = max_humid_row
                        date_maxhumid = date

    print(f"Max Temperature: {maxtemp} on {date_maxtemp}")
    print(f"Min Temperature: {mintemp} on {date_mintemp}")
    print(f"Max Humidity: {maxhumid} on {date_maxhumid}")



def average_report(year, month):
    max_temps = []
    min_temps = []
    humid = []
   

    for file in os.listdir(path):
            if year in file and month in file:
                file_path = os.path.join(path, file)
                with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
                    lines = [line for line in f if line.strip() and not line.startswith("<")]
                    header = [h.strip() for h in lines[0].split(",")]
                    csv_reader = csv.DictReader(lines[1:], fieldnames=header)
                    for row in csv_reader:
                        row = { (k.strip() if k else ""): v for k, v in row.items() }
                        if row.get('PKT') == 'PKT' or not row.get('PKT'):
                            continue
                        if not row.get('Max TemperatureC') or not row.get('Min TemperatureC') or not row.get('Max Humidity'):
                            continue
                        maxs = row['Max TemperatureC']
                        max_temps.append(int(maxs))
                        maxs = row['Min TemperatureC']
                        min_temps.append(int(maxs))
                        maxs = row['Max Humidity']
                        humid.append(int(maxs))
    avg_max = sum(max_temps) // len(max_temps)
    avg_min = sum(min_temps) // len(min_temps)
    avg_humid = sum(humid) // len(humid) 
    print(f'Highest Average: {avg_max}')
    print(f'Lowest Average: {avg_min}')
    print(f'Average Humidity: {avg_humid}')
                                            

def monthly_report(year, month):
        RED = "\033[91m"
        BLUE = "\033[94m"
        END = "\033[0m"

        for file in os.listdir(path):
            if year in file and month in file:
                file_path = os.path.join(path, file)
                with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
                    lines = [line for line in f if line.strip() and not line.startswith("<")]
                    header = [h.strip() for h in lines[0].split(",")]
                    csv_reader = csv.DictReader(lines[1:], fieldnames=header)
                    for row in csv_reader:
                        row = { (k.strip() if k else ""): v for k, v in row.items() }
                        if row.get('PKT') == 'PKT' or not row.get('PKT'):
                            continue
                        if not row.get('Max TemperatureC') or not row.get('Min TemperatureC') or not row.get('Max Humidity'):
                            continue
                        day = row['PKT'].split("-")[2]
                        max_temp = int(row['Max TemperatureC'])
                        min_temp = int(row['Min TemperatureC'])
                        print(f"{day} {RED}{'+' * 10} {max_temp}C{END}")
                        print(f"{day} {BLUE}{'+' * 10} {min_temp}C{END}")


def monthly_report_color(year, month):
        RED = "\033[91m"
        BLUE = "\033[94m"
        END = "\033[0m"

        for file in os.listdir(path):
            if year in file and month in file:
                file_path = os.path.join(path, file)
                with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
                    lines = [line for line in f if line.strip() and not line.startswith("<")]

                    header = [h.strip() for h in lines[0].split(",")]
                    csv_reader = csv.DictReader(lines[1:], fieldnames=header)

                    for row in csv_reader:
                        row = { (k.strip() if k else ""): v for k, v in row.items() }
                        
                        if row.get('PKT') == 'PKT' or not row.get('PKT'):
                            continue

                        if not row.get('Max TemperatureC') or not row.get('Min TemperatureC') or not row.get('Max Humidity'):
                            continue
                        day = row['PKT'].split("-")[2]
                        max_temp = int(row['Max TemperatureC'])
                        min_temp = int(row['Min TemperatureC'])
                        print(f"{day} {'+' * 10} {RED}{max_temp}C{END} - {BLUE}{min_temp}C{END}")

yearly_report("2003")
average_report("2005", "Jun")
monthly_report("2011", "Mar")
monthly_report_color("2011", "Mar")
