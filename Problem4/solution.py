from pyspark import SparkContext


def start_service():
    global sc
    sc = SparkContext(appName="Problem2").getOrCreate()


def end_service():
    sc.stop()


# Q1
# Generate two RDDs of list1 and list2
# Return the elements in rdd1 and rdd2 as a tuple
def Q1():
    list1 = [[1, 2], [6, 3, 4, 7]]
    list2 = [[1, 9], [3, 4, 2], [8, 5]]

    global rdd1   # RDD should be global
    global rdd2  # RDD should be global
    rdd1 = sc.parallelize(list1)
    rdd2 = sc.parallelize(list2)

    return rdd1.count(), rdd2.count()


# Q2
# Flatten rdd1 and rdd2 then return the count of
# numbers in rdd1 and rdd2 as a tuple
def Q2():
    global rdd1
    global rdd2
    rdd1 = rdd1.flatMap(lambda x: x)
    rdd2 = rdd2.flatMap(lambda x: x)
    return rdd1.count(), rdd2.count()


# Q3
# Return a list of all the numbers
# in these two RDDs
def Q3():
    return rdd1.union(rdd2).collect()


# Q4
# Return a list of numbers rdd1 but
# not in rdd2
def Q4():
    return rdd1.subtract(rdd2).collect()


# Q5
# Return a list of numbers both in rdd1
# and rdd2
def Q5():
    return rdd1.intersection(rdd2).collect()
