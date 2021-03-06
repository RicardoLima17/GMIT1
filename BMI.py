
# Author Ricardo

#set variables weight and height and collect user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

#perform BMI calculation conversion of height cm to meters
height_meters = height / 100
bmi = weight / (height_meters  ** 2)

#print formatting method may not work in older versions python
print('BMI is: {}.'.format(round(bmi, 2)))


# References:
# https://www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula
# Lectures
