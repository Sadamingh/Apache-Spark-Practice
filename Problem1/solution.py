from pyspark import SparkContext


def start_serive():
    global sc
    sc = SparkContext(appName="Problem1").getOrCreate()


def end_serive():
    sc.stop()


# Q1
# Read the file "data.tsv" split it in 3 partitions
# Return the first line
def Q1():
    global rdd
    rdd = sc.textFile("data.tsv", 3)
    return rdd.take(1)


# Q2
# Sort the data by the number in the first column in descending order
# Return the result by collect
def Q2():
    rdd_split_int = rdd.map(
        lambda x: [int(x.split(",")[0]), int(x.split(",")[1])])
    rdd_split_int_sort = rdd_split_int.sortBy(lambda x: x[0], ascending=False)
    return rdd_split_int_sort.collect()


# Q3
# Return a list of distinct numbers in the first column
# Sort it by ascending order
def Q3():
    rdd_int_dist = rdd.map(lambda x: int(x.split(",")[0])).distinct()
    rdd_int_dist_sort = rdd_int_dist.sortBy(lambda x: x)
    return rdd_int_dist_sort.collect()


# Q4
# Count and return the even numbers in the second column
def Q4():
    rdd_code = rdd.map(lambda x: int(x.split(",")[1]))
    rdd_even = rdd_code.filter(lambda x: x % 2 == 0)
    return rdd_even.count()
