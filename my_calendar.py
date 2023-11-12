# Project: Calendar
# This is a project that will keep track of assignments and show progress towards when they are due
# Author: Kellen Bell

import sys
import csv

# gets all of the events
def getEvents():
    file = open('calendar.csv')
    type(file)

    reader = csv.reader(file)

    headers = next(reader)

    print(headers)

    file.close()

# add an event to the list of events
def addEvent():
    pass

# we will take in different commands based on functionality we want
def handleArgs():

    # get rid of file name arg
    args = sys.argv[1:]

    # make sure we have a valid number of args
    n = len(args)

    if n != 1:
        print("Error: Invalid number of arguments\n")
        printHelpMessage()
        return

    command = args[0]

    if command == "h":
        printHelpMessage()
        return

    if command == "a":
        addEvent()

    if command == "g":
        getEvents()

# print the help message
def printHelpMessage():
    print("Expected format of command:")
    print("\tpython my_calendar -function")
    print("\n\tFunction may be:")
    print("\t\ta: add an event\n\t\tg: get event\n\t\th: help")

def main():
    handleArgs()

if __name__ == "__main__":
    main()
