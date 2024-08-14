"""Create a class 'Time' and initialize it with hours and minutes.
Create a method addTime() which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime() which should print the time.
Also, create a method displayMinute() which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minutes."""

# Defining the time class
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.total_mins = (self.hours * 60) + self.minutes

# defining the add time method that would take 2 Time objects and return total time formatted
    def addTime(self, other):
        if isinstance(other, Time):
            disp_hour = (self.total_mins + other.total_mins) // 60
            disp_mins = (self.total_mins + other.total_mins) % 60
            return f'({self.hours} hours and {self.minutes}) + ' \
                   f'({other.hours} hours and {other.minutes}) is ' \
                   f'({disp_hour} hr and {disp_mins} min)'

# defining the display time function which will subsequently be used in the displayMinute function
    def displayTime(self):
        return f'{self.hours} hours and {self.minutes} minutes'

# defnining the display minute function that utilizes displayTime function and prints total minutes
    def displayMinute(self):
        return f'({self.displayTime()}) is total {self.total_mins} minutes'


time1 = Time(hours=2,minutes=42)
time2 = Time(hours=1,minutes=18)

print(time1.displayTime())
print(time1.addTime(time2))
print(time1.displayMinute())