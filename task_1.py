from datetime import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def get_birthdays_per_week(users):
    list_of_birthdays = {'Monday': [], 
           'Tuesday': [],
           'Wednesday': [],
           'Thursday': [],
           'Friday': []}
    today = datetime.today().date()
    for user in users:
        user_name = user["name"]
        user_birthday = user["birthday"].date()
        
        birthday_this_year = user_birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = user_birthday.replace(year = today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        
        if delta_days <= 7:
            num_weekday = birthday_this_year.weekday()
            if num_weekday > 4:
                num_weekday = 0
                name_weekday = weekdays[num_weekday]
            else:
                name_weekday = weekdays[num_weekday]
                
            list_of_birthdays[name_weekday].append(user_name)
            
    for day, names in list_of_birthdays.items():
        if names:
            print(f"{day}: ", end = '')
            print(*names, sep = ", ")


users = [{"name": "Ronald McDonald", "birthday": datetime(2007, 4, 6)},
         {"name": "Thomas Kentucky", "birthday": datetime(2018, 4, 8)},
         {"name": "Julia May", "birthday": datetime(2001, 4, 16)}, 
         {"name": "Patick Andre", "birthday": datetime(1998, 5, 28)},
         {"name": "Ivon Figar", "birthday": datetime(1965, 3, 16)},
         {"name": "Drake Smith", "birthday": datetime(1989, 1, 3)},
         {"name": "Caroline Schneider", "birthday": datetime(1991, 11, 7)},
         {"name": "Julita Cortez", "birthday": datetime(2003, 3, 6)},
         {"name": "Carol Twick", "birthday": datetime(1982, 12, 20)},
         {"name": "John Swain", "birthday": datetime(1976, 4, 11)},
         {"name": "Barry Trotter", "birthday": datetime(2007, 4, 13)}
         ]

get_birthdays_per_week(users)