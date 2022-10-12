import json
from os.path import exists
from calendar import month_name


def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}
    
def write_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def max_temperature(data, date):
    temp = []
    for i in data:
        if date == i[:8]:
            temp.append(data[i]['t'])
    return max(temp) if len(temp) else None
            
def min_temperature(data, date):
    temp = []
    for i in data:
        if date == i[:8]:
            temp.append(data[i]['t'])
    return min(temp) if len(temp) else None

def max_humidity(data, date):
    humidity = []
    for i in data:
        if date == i[:8]:
            humidity.append(data[i]['h'])
    return max(humidity) if len(humidity) else None

def min_humidity(data, date):
    humidity = []
    for i in data:
        if date == i[:8]:
            humidity.append(data[i]['h'])
    return min(humidity) if len(humidity) else None
    
def tot_rain(data, date):
    rainfalls = []
    for i in data:
        if date == i[:8]:
            rainfalls.append(data[i]['r'])
    return sum(rainfalls) if len(rainfalls) else None
    
def report_daily(data, date):
    print("="*25, "{}".format("DAILY REPORT"), "="*24)
    print("{:<20}  {:>8}  {:>11}  {:>8}  {:>8}".format("Date", "Time", "Temperature", "Humidity", "Rainfall"))
    print("{:<20}  {:>8}  {:>11}  {:>8}  {:>8}".format("="*20, "="*8, "="*11, "="*8, "="*8))
    
    for i in data:
        if i[:8] == date:
            fdate = "{} {}, {}".format(month_name[int(i[4:6])], int(i[6:8]), int(i[:4]))
            ftime = "{:02d}:{:02d}:{:02d}".format(int(i[8:10]), int(i[10:12]), int(i[12:14]))
            temp = str(data[i]["t"])
            humidity = str(data[i]["h"])
            rainfall = str(data[i]["r"])
            rainfall2 = "{:.2f}".format(float(rainfall))
            print("{:<20}  {:^8}  {:>11}  {:>8}  {:>8}".format(fdate, ftime, temp, humidity, rainfall2))
    print()
        
def report_historical(data):
    print("="*30, "{}".format("HISTORICAL REPORT"), "="*27)
    print("{:<20}  {:>11}  {:>11}  {:>8}  {:>8}  {:>8}".format("", "Minimum", "Maximum", "Minimum", "Maximum", "Total") + "\n{:<20}  {:>11}  {:>11}  {:>8}  {:>8}  {:>8}".format("Date", "Temperature", "Temperature", "Humidity", "Humidity", "Rainfall"))
    print("{:<20}  {:>11}  {:>11}  {:>8}  {:>8}  {:>8}".format("="*20, "="*11, "="*11, "="*8, "="*8, "="*8))
    
    historical_data = []
    for i in data:
        fdate = "{} {}, {}".format(month_name[int(i[4:6])], int(i[6:8]), int(i[:4]))
        if fdate not in historical_data:
            max_temp = str(max_temperature(data, i[:8]))
            min_temp = str(min_temperature(data, i[:8]))
            max_hum = str(max_humidity(data, i[:8]))
            min_hum = str(min_humidity(data, i[:8]))
            total_rain = str(tot_rain(data, i[:8]))
            total_rain2 = "{:.2f}".format(float(total_rain))
            print("{:<20}  {:>11}  {:>11}  {:>8}  {:>8}  {:>8}".format(fdate, min_temp, max_temp, min_hum, max_hum, total_rain2))
            historical_data.append(fdate)
    print()
            