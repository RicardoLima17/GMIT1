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


<b>References:</b><br> https://djangocentral.com/reverse-a-sentence/<br>lecture.


## 3-Collatz.py week 04
<p>1- Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.<br>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.<br>Have the program end if the current value is one.</p>

### Code
<p><b>#defining the function</b><br>def collatz(number):<p/>

<p><b>#If the number is negative print "Unfortunately this is not a positive Integer."</b><br> if number <= 0:<br>print("Unfortunately this is not a positive Integer.")<br>   quit() 
       
<p><b>#looping through and if number found is even divide it by 2</b><br> elif number % 2 == 0:<br>print(number // 2)<br>return number // 2<br> <br>elif number % 2 == 1:<br>result = 3 * number + 1<br>print(result)<br>return result
       
<p><b>#type the number</b><br>n = input("Type a number: ")</br>
<p><b>#running the function togethe final result number 1</b></br>while n != 1:<br>n = collatz(int(n))


<p><b>References:</b></br>https://stackoverflow.com/questions/45990261/implementing-the-collatz-function-using-python<br>lecture



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
   
<p><b>#if the date are saturday or sunday</b><br>else:<br>#if is not 0 = monday, 1 = tuesday, 3 = wednesday, 4 = thursday or 5 = friday<br>#print satuday and sunday<br>print("It is the weekend, yay!")</br>    

<p><b>References:</b></br>https://www.w3schools.com/python/python_datetime.asp<br>lecture.<br>

## 5-Squareroot.py week 06
<p>1-Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called <tt>sqrt</tt> that does this. I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 
This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.</p>

### Code

<p><b>#variable number with input a positive number</b><br>number = float(input("Please enter a positive number: "))<br>

<p><b>#conditional if bigger than 0 go ahead if not closed the programme</b><br>if number <= 0.0:</br>print("Unfortunately this is not a positive number.")</br>quit()</br>

<p><b>#variables to use in your formula</b><br>a = 1/2<br>b = 5</br>

<p><b>#first calculation with variables</b><br>cal1 = a*(number/b+b)<br>

<p><b>#second calculation with variables</b><br>cal2 = a*(number/cal1+cal1)<br>

<p><b>#last calculation with variables</b><br>cal3 = a*(number/cal2+cal2)<br>

<p><b>#print first calculation with round 1 decimal</b><br>print (round(cal1, 1))<br>

<p><b>#print second calculation with round 1 decimal</b><br>print (round(cal2, 1))<br>

<p><b>#print the final calculation</b><br>print ("The square root of {} is approx. {}." .format(number, (round(cal3, 1,))))<br>

<p><b>References:</b></br>https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD_fZWj7Tcs<br>lecture</br>


## 6-Es.py week 07
<p>1- Write a program that reads in a text file and outputs the number of e's it contains.The program should take the filename from an argument on the command line.</p>

### Code


<p><b>#import collection to use Counter</b><br>import collections<br>filename = "moby-dick.txt"<br>
       
<p><b>#open file to read</b><br>with open (filename, "r") as info:<br>
       
<p><b>#this line count all characteres</b><br>count = collections.Counter(info.read())<br>
       
<p><b>#variable to store count</b><br> value = (count)<br>
       
<p><b>#print all counter in value</b><br>print(value)<br></p>

<p> </p>
   
<p><b>#Now we know "e" has 116960</b><br>N = 0<br>
       
<p><b>#open file to read</b><br>with open (filename, "r") as info:<br>
       
<p><b>#new line</b><br>for line in info:<br>

<p><b>#split variable line and store in new variable words</b><br>words = line.split()<br>

<p><b>#words store in new variable i</b><br>for i in words:<br>

<p><b>#create a new variable letter</b><br>for letter in i:<br>

<p><b>#letter "e"</b><br>if letter == "e":<br>

<p><b>#count n = 0 and count once n + 1 if you use N + 2 count twice "e"</b><br>N = N + 1<br>

<p><b>#print "e" = 116960</b><br>print (N)<br>    


<p><b>References</b></br>https://programminghistorian.org/en/lessons/counting-frequencies<br>https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php<br>lectures<br>



## 7-Plottask.py week 08
<p>1- Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. Some marks will be given for making the plot look nice..</p>

### Code
<br>import numpy as np
import matplotlib.pyplot as plt

#first function x
#range 0 to 4
x = np.linspace(0,4)
y=  x

#naming the label for each function
plt.plot(x,y, label= "f(x)= x")

#second function x2^2
# range 0 to 4
x2= np.linspace(0,4)
y2= x2**2

#naming the label for each function
plt.plot(x2,y2, label= "g(x)= $x^2$")

#third function x3^3
# range 0 to 4
x3= np.linspace(0,4)
y3= x3 **3

#naming the label for each function
plt.plot(x3, y3, label= "h(x)= $x^3$")

#y-axis and x-axis
plt.xlabel("x-axis")
plt.ylabel("y-axis")


#this places the legend on the upper left of the plot
plt.legend(loc="upper left")

#title to plot
plt.title("Function x")

#adding grid
plt.grid()

#show plot
plt.show()

<p><b>References</b></br>
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
#https://www.w3schools.com/python/matplotlib_pyplot.asp
#lectures



