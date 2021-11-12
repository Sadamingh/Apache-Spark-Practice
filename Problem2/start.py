from pyspark import SparkContext


def start_service():
    global sc
    sc = SparkContext(appName="Problem2").getOrCreate()


def end_service():
    sc.stop()


# Q1
# Read the file "input.csv"
# Return the first three lines
def Q1():
    global rdd   # RDD should be global
    pass


# Q2
# Print the maximum number per line
def Q2():
    pass


# Q3
# Print the average of values from step 2 up to the second decimal place
def Q3():
    pass
