import weather
filename = "w.dat"
data = weather.read_data(filename)

while True:
    print("\t*** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set data filename \n2. Add weather data \n3. Print daily report\n4. Print historical report \n5. Exit the program\n")
    menu_choice = int(input("Enter menu choice: "))
    
    if (menu_choice == 1):
        print()
        newfile = input("Enter data file name: ")
        filename = newfile
        
    elif (menu_choice == 2):
        print()
        date = input("Enter data (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        temperature = int(input("Enter temperature: "))
        humidity = int(input("Enter humidity: "))
        rainfall = float(input("Enter rainfall: "))
        data[date + time] = {"t": temperature, "h": humidity, "r": rainfall}
        weather.write_data(data, filename)
        
    elif (menu_choice == 3):
        print()
        date = input("Enter date (YYYYMMDD): ")
        weather.report_daily(data, date)
        
    elif (menu_choice == 4):
        print()
        weather.report_historical(data)
        
    elif (menu_choice == 5):
        break
    
    else:
        print("Invalid Choice.")