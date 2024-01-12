import sqlite3
import datetime

conn = sqlite3.connect("physical.db")
cur = conn.cursor()

while True:
    print("Select an option:")
    print("1. Enter a new activity")
    print("2. View activity report")

    choice = int(input())

    if choice == 1:
        date = input("Enter the date of the activity (YYYY-MM-DD): ")
        description = input("Enter the description of the activity: ")

        cur.execute("SELECT DISTINCT category FROM activities")

        categories = cur.fetchall()

        print("Select a category by number: ")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category[0]}")
        print(f"{len(categories) + 1}. Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter the new category name: ")
        else:
            category = categories[category_choice - 1][0]
            
        total_distance = int(input("Enter the total distance of the activity (KMs): "))

        total_steps = int(input("Enter the total steps of the activity (Number): "))

        kcal_burned = int(input("Enter the total kcal burned (Number): "))



        cur.execute("INSERT INTO activities (Date, description, category, total_distance, total_steps, kcal_burned) VALUES (?,?,?,?,?,?)", (date, description, category, total_distance, total_steps,kcal_burned))

        conn.commit()

    elif choice == 2:
        print("Select an option:")
        print("1. View all activities")
        print("2. View monthly activities by category")


        view_choice = int(input())
        if view_choice == 1:
            cur.execute("SELECT * FROM activities")
            activities = cur.fetchall()
            for activity in activities:
                print(activity)
        elif view_choice == 2:
            month = input("Enter the month (MM): ")
            year = input("Enter the year(YYYY): ")
            cur.execute("""SELECT category, SUM(total_distance),SUM(total_steps),SUM(kcal_burned)
                        FROM activities
                        WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ?
                        GROUP BY category""", (month,year))
            activities = cur.fetchall()
            for activity in activities:
                print(f"Category: {activity[0]}, Total Distance: {activity[1]}, Total Steps: {activity[2]}, Calories burned: {activity[3]}")
        else:
            exit()
    else:
        exit()

    repeat = input("Would you like to do something else (y/n)?\n")
    if repeat.lower() != "y":
        break


conn.close()
