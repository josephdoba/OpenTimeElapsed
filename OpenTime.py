# OpenTime 0.0.1 - Created by Joseph Doba

# When this script runs. Setup a while loop to listen for the next program to be open 


# Once program opens, start log the time it started.
	# set a variable to the time it opened.

# When the program is closed, log the time it closed.
	# set a variable to the time it closed.

#show time elapsed. 

# option to export data into a spreadsheet
# https://docs.python.org/3/library/csv.html

# Eventually, have a GUI that allows the user to choose a specific program to trigger
# I would like to try out tkinter
# What modules do I need? System time probably

# import modules
import datetime
import time
import os
import tkinter

# setup GUI
# window = x
# window.title("OpenTime Application stopwatch")


# def convertToString():
# 	str()
# 	return()

print("Start timer... program is running")
timeStarted = 1
print(timeStarted)

time.sleep(5)

print("Stop timer... program is closed.")
timeStopped = 5
print(timeStopped)

timeElapsed = timeStopped - timeStarted
# print(timeElapsed)

# convertToString()
# print(timeElapsed)

def elapsed():
	print("You have spent " + str(timeElapsed) + " seconds in the program")

elapsed()



