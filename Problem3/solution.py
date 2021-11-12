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
    global rdd   # RDD should be global
    rdd = sc.textFile("FoodTruckSF.csv")
    return rdd.first()


# Q2
# Delete the first line, and then return a list of
# distinct numbers in the first column and sort it
# by ascending order
def Q2():
    rdd_split = rdd.map(lambda x: x.split(","))
    rdd_data = rdd_split.filter(lambda x: x[0] != "DayOrder")
    rdd_first_col_dist = rdd_data.map(
        lambda x: int(
            x[0])).distinct().sortBy(
        lambda x: x)
    return rdd_first_col_dist.collect()


# Q3
# Delete the first line, then turn the 12th (index = 11) column to datetime,
# return a list of the first 3 datatime values of that column
def Q3():
    rdd_split = rdd.map(lambda x: x.split(","))
    rdd_data = rdd_split.filter(lambda x: x[0] != "DayOrder")
    rdd_time = rdd_data.map(
        lambda x: datetime.strptime(
            x[11], "%m/%d/%Y %H:%M:%S %p"))
    return rdd_time.take(3)


# Q4
# Delete the first line, then
# Sum the locationid (index = 6) column for all the Monday trucks
# Note that you should only use rdd.reduce
def Q4():
    rdd_split = rdd.map(lambda x: x.split(","))
    rdd_data = rdd_split.filter(lambda x: x[0] != "DayOrder")
    rdd_blocks = rdd_data.map(lambda x: int(x[6]))
    return rdd_blocks.reduce(lambda x, y: x + y)


# Q5
# Delete the first line, then calculate the
# time intervals between the 12th (index = 11) column and the
# 13th (index = 12) column ignore the line without time values
# in these two columns
# Return a list of the first 5 time intervals in seconds
def Q5():
    rdd_split = rdd.map(lambda x: x.split(","))
    rdd_data = rdd_split.filter(lambda x: x[0] != "DayOrder")
    rdd_data_reduced = rdd_data.filter(lambda x: x[11] != "" and x[12] != "")
    rdd_times = rdd_data_reduced.map(
        lambda x: [
            datetime.strptime(
                x[11],
                "%m/%d/%Y %H:%M:%S %p"),
            datetime.strptime(
                x[12],
                "%m/%d/%Y %H:%M:%S %p")])
    rdd_time_intervals = rdd_times.map(lambda x: (x[1] - x[0]).total_seconds())
    return rdd_time_intervals.take(5)
