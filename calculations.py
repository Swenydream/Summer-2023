# Import Libraries needed to create a pie chart. 
from matplotlib import pyplot as plt              # requires the mathplotlib library to graph plots for pie chart. 
import numpy as np

import mysql.connector             # library that is needed to connect to the mysql server to connect to the database where the table is stored.

connection = mysql.connector.connect(
    host='localhost', 
    user='Swen', 
    password='Ese', 
    database='elevator'
    )

if connection.is_connected():  # if connection is sucessful
    print('Connection Sucess')

    mycursor = connection.cursor()

    mycursor.execute("SELECT requestedFloor FROM elevatorNetwork")

    myresult = mycursor.fetchall()

    for row in myresult:

        print(row)

else:                          #if connection fails
    print('Connection failed')
    
connection.close()

requestedFloor=[1,2,3,1,1,1,2,3,2,3,1,2,2,3,1,1,2,3,3,2,1,1,1,2,3,2,1,1,2,3,3,3,2,1]
print("requestedFloors: ",requestedFloor)

#initialize the variables for 
inc1=0
inc2=0
inc3=0

# Counts the floor numbers by looping
for i in requestedFloor:
    if (i == 1):
       inc1 = inc1 + 1  # for every 1 the loop sees it records the value and it keeps of recording the ## of times it sees the number desginated that if statement.
    if (i == 2):
        inc2 = inc2 + 1
    if (i == 3):
        inc3 = inc3 + 1
print("1 appears: ",inc1)    # Prints the # of times each nubmer appears.
print("2 appears: ",inc2)
print("3 appears: ",inc3)

#Get the total amount of variables 
tot = inc1 + inc2 + inc3

# Use the tot to find the percentage by dividing the inc's by the tot to find the percentage
percentage1 = (inc1/tot)*100      
percentage2 = (inc2/tot)*100
percentage3 = (inc3/tot)*100
print("% appearence of 1: ",percentage1)
print("% appearence of 2: ",percentage2)
print("% appearence of 3: ",percentage3)

#Creating a text file to place the data in
f= open("diagonstics.txt","w+")      # Creates the textfile to store the data
for i in range(1):
     f.write("First Floor Requested Percentage %d\r\n" % percentage1)       # Writes the data inside the text for Floor 1
     f.write("Second Floor Requested Percentage %d\r\n" % percentage2)      # Writes the data inside the text for Floor 2
     f.write("Third Floor Requested Percentage %d\r\n" % percentage3)       # Writes the data inside the text for Floor 3

f.close()       #Once finishes writing inside the text file then it closes the text file

#Create the Pie Chart for graph

floors =['1', '2', '3']
per =[percentage1, percentage2, percentage3]
fig = plt.figure(figsize =(15, 10))
plt.pie(per, labels = floors)
plt.show()
