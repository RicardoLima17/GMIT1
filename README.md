# Programming and Scripting Problem Set Solutions 2021

## Summary of Assignment
<p>This repository contains my programming and scripting problem sheet 2021. In this eight weeks, was developed skills in, github, Matplolib, Seaborn, NumPy and Pandas.</p>


## 1-BMI.py week 02
<p>1- Write a program that calculates somebody’s Body Mass Index (BMI) The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared. Body Mass Index is a method for screening the relative weight of a person, and is measured by taking the person's weight in kilograms divided by the square of height in metres.</p>

### Code

<p><b>#set variables weight and height and collect user input</b> <br> weight = float(input("Enter your weight in kilograms: "))<br>height = float(input("Enter your height in centimeters: "))</p>

<p><b>#perform BMI calculation conversion of height cm to meters</b> <br> height_meters = height / 100<br> bmi = weight / (height_meters  ** 2)</p>

<p><b>#print formatting method may not work in older versions python</b><br> print('BMI is: {}.'.format(round(bmi, 2)))</p>

<b>References:</b><br>https://www.ramsayhealth.co.uk/weight-loss-surgery/bmi/bmi-formula<br>Lectures



## 2-Secondstring.py week 03
<p>1- Write a program that takes asks a user to input a string and outputs every second letter in reverse order.<br>Reverse() is an inbuilt method in Python programming language that reverses objects of list in place. Returns: The reverse() method does not return any value but reverse the given object from the list.</p>

### Code
<p><b>#type:  The quick brown fox jumps over the lazy dog.</b><br>sentence = input("Type a sentence that you want reversed:")</p>

<p><b>#reverse a sentence every second letter in reverse order. [::-2] get 2 in 2 letters</b><br>
print(sentence[::-2])


<b>References:</b><br> https://djangocentral.com/reverse-a-sentence/<br>Used lecture on Tuesday program as a base for the problem.


## 3-Collatz.py week 04
<p>1- Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.<br>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.<br>Have the program end if the current value is one.</p>

### Code
<p><b>#defining the function</b><br>def collatz(number):<p/>

<p><b>#If the number is negative print "Unfortunately this is not a positive Integer."</b><br> if number <= 0:<br>print("Unfortunately this is not a positive Integer.")<br>   quit() 
       
<p><b>#looping through and if number found is even divide it by 2</b><br> elif number % 2 == 0:<br>print(number // 2)<br>return number // 2<br> <br>elif number % 2 == 1:<br>result = 3 * number + 1<br>print(result)<br>return result
       
<p><b>#type the number</b><br>n = input("Type a number: ")</br>
<p><b>#running the function togethe final result number 1</b></br>while n != 1:<br>n = collatz(int(n))


<p><b>Reference:</b></br>https://stackoverflow.com/questions/45990261/implementing-the-collatz-function-using-python<br>Used lecture



## 4-Weekday.py week 05
<p>1- Write a program that outputs whether or not today is a weekday.(You will need to search the web to find how you work out what day it is) An example of running this program on a Thursday is given below.</p>

### Code

import datetime

<p><b>#function</b><br>dayOfweek =datetime.datetime.today().weekday()</br>

<p><b>#print the date today</b><br>print (dayOfweek)</br>

<p><b>#if the date is monday</b><br>if dayOfweek == 0: # you can use @if dayOfweek == monday:<br>#print this message below<br>print ("Yes, unfortunately today is a weekday.")</br>

<p><b>#if the date is tuesday</b><br>elif dayOfweek == 1: # you can use @if dayOfweek == tuesday:<br>#print this message below<br>print ("Yes, unfortunately today is a weekday.")</br>

<p><b>#if the date is wednesday</b><br>elif dayOfweek == 2: # you can use @if dayOfweek == wednesday:<br>#print this message below<br>print ("Yes, unfortunately today is a weekday.")</br>

<p><b>#if the date is thursday</b><br>elif dayOfweek == 3: # you can use @if dayOfweek == thursday:<br>#print this message below<br>print ("Yes, unfortunately today is a weekday.")</br>

<p><b>#if the date is friday</b><br>elif dayOfweek == 4: # you can use @if dayOfweek == friday:<br>#print this message below<br>print ("Yes, unfortunately today is a weekday.")</br>
   
<b>#if the date are saturday or sunday</b><br><br>else:<br>#if is not 0 = monday, 1 = tuesday, 3 = wednesday, 4 = thursday or 5 = friday<br>#print satuday and sunday<br>print("It is the weekend, yay!")</br>    

<p><b>Reference:</b></br>https://www.w3schools.com/python/python_datetime.asp<br>Used lecture on Tuesday program as a base for the problem.<br>

## 5-Squareroot.py week 06
<p>1- Write a program that calculates somebody’s Body Mass Index (BMI) The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared.</p>

### Code

## 6-Es.py week 07
<p>1- Write a program that calculates somebody’s Body Mass Index (BMI) The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared.</p>

### Code

## 7-Plottask.py week 08
<p>1- Write a program that calculates somebody’s Body Mass Index (BMI) The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared.</p>

### Code




