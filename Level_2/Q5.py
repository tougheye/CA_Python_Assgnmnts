"""
5. You are developing a program that analyzes weather data.
Write a Python function that takes a list of temperature readings
for a specific location and determines the average temperature,
highest temperature, and lowest temperature.
Input: temperature_readings = [25, 28, 21, 24, 27] Output:
Average Temperature: 25.0 Highest Temperature: 28 Lowest Temperature: 21
"""
from statistics import  mean
temper_reading = [25, 28, 21, 24, 27]

def temp_summary(temp_list):
    return f'Average Temperature: {float(mean(temp_list))} ' \
           f'Highest Temperature: {max(temp_list)} ' \
           f'Lowest Temperature: {min(temp_list)}'

print(temp_summary(temper_reading))
