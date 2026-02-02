#FutureTime.py
#Name: Addy Duering
#Date: 2/1/2026
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour + 18
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  input_hours = int(input("Enter hours to add: "))
  #Ask user for minutes
  input_minutes = int(input("Enter minutes to add: "))
  #Calculate the time after the user-supplied time has passed.
  futureMinute = (currentMinute + input_minutes) % 60
  futureHour = (currentHour + input_hours + (currentMinute + input_minutes) // 60) % 24
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("Future time is {:02}:{:02}".format(futureHour, futureMinute))

if __name__ == '__main__':
  main()
