from pyspark import SparkContext


def start_service():
    global sc
    sc = SparkContext(appName="Problem2").getOrCreate()


def end_service():
    sc.stop()


# Q1
# Read the file "input.txt"
# Return the first three lines
def Q1():
    global rdd   # RDD should be global
    rdd = sc.textFile("input.txt")
    return rdd.take(3)


# Q2
# Print the maximum number per line
def Q2():
    rdd_split_nums = rdd.map(lambda x: [int(value) for value in x.split(",")])
    rdd_max = rdd_split_nums.map(lambda x: max(x))
    return rdd_max.collect()


# Q3
# Print the average of values from step 2 up to the second decimal place
def Q3():
    rdd_split_nums = rdd.map(lambda x: [int(value) for value in x.split(",")])
    rdd_max = rdd_split_nums.map(lambda x: max(x))
    return round(rdd_max.mean(), 2)


def main():

    start_service()
    Q1()
    print(Q3())
    end_service()


if __name__ == '__main__':
    main()
