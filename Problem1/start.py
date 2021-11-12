from pyspark import SparkContext


def start_service():
    global sc
    sc = SparkContext(appName="Problem1").getOrCreate()


def end_service():
    sc.stop()


# Q1
# Read the file "data.tsv" split it in 3 partitions
# Return the first line
def Q1():
    global rdd   # RDD should be global
    pass


# Q2
# Sort the data by the number in the first column in descending order
# Return the result by collect
def Q2():
    pass


# Q3
# Return a list distinct numbers in the first column
# Sort it by ascending order
def Q3():
    pass


# Q4
# Count and return the even numbers in the second column
def Q4():
    pass
