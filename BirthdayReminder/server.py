import requests, json
from datetime import datetime
import time as timeb

while True:
    with open("data.json", "r") as file:
        data = json.load(file)

    for name in data["names"]:
        person = data["names"][name]
        user_birthday = person["birthday"]

        try:
            birthday_data = user_birthday.split("/")
            time = datetime.now()

            month = birthday_data[0]
            day = birthday_data[1]
            day = int(day) + 1
            year = birthday_data[2]

            next_birthday = datetime(int(time.year), int(month), int(day))
            age = time.year - int(year)

            if time < next_birthday:
                age -= 1

            if time < next_birthday:
                days_until_birthday = (next_birthday - time).days
            else:
                next_year_birthday = datetime(time.year + 1, month, day)
                days_until_birthday = (next_year_birthday - time).days
            if days_until_birthday <= 7:
                data_to_send = f"{name}'s birthday is in {days_until_birthday} days! 🥳"
                
                while True: #requests can be unstable, will retry on random fails
                    try: 
                        requests.post("https://ntfy.sh/RemindBirthday222",data=data_to_send.encode(encoding='utf-8'))
                        break

                    except:
                        print("web request failed, no internet connect likely issue")
        except ValueError:
            print("Invalid date format. for", person, user_birthday)

        timeb.sleep(86400) #will send daily reminders
