import schedule
import time

def drink_water():
    # Code to remind and track water intake
    print("It's time to drink water!")

def exercise():
    # Code to initiate exercise routine
    print("Time for exercise!")

def meditate():
    # Code to start a meditation session
    print("Let's meditate!")

# Define the schedule for each habit
schedule.every(1).hour.do(drink_water)
schedule.every().day.at("08:00").do(exercise)
schedule.every().day.at("18:00").do(meditate)

while True:
    schedule.run_pending()
    time.sleep(1)