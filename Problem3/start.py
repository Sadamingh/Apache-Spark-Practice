from pyspark import SparkContext
from datetime import datetime


def start_service():
    global sc
    sc = SparkContext(appName="Problem3").getOrCreate()


def end_service():
    sc.stop()


# Q1
# Read the file "FoodTruckSF.csv"
# Return the first line
def Q1():
    global rdd
    pass


# Q2
# Delete the first line, and then return a list of
# distinct numbers in the first column and sort it
# by ascending order
def Q2():
    pass


# Q3
# Delete the first line, then turn the 12th (index = 11) column to datetime,
# return a list of the first 3 datatime values of that column
def Q3():
    pass


# Q4
# Delete the first line, then
# Sum the locationid (index = 6) column for all the Monday trucks
# Note that you should only use rdd.reduce
def Q4():
    pass


# Q5
# Delete the first line, then calculate the
# time intervals between the 12th (index = 11) column and the
# 13th (index = 12) column ignore the line without time values
# in these two columns
# Return a list of the first 5 time intervals in seconds
def Q5():
    pass
