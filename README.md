# Apache-Spark-Practice

This is a practice problem set of Apache Spark.



### 1 Set Up the Environment

Before you start, you need to have,

* `Python 3.8+`
* `PySpark 3.2.0+`
* A Python IDE (e.g. `Pycharm` is recommended)

Then, clone this repository somewhere,

```bash
$ git clone https://github.com/Sadamingh/Apache-Spark-Practice.git
```

<br>

### 2 What to Do?

For each problem, what you have to do is to,

* Implement the `start.py` script by following the instructions in that script
* Make sure you followed the PEP8 pattern (or you won't pass the sanity test)

You can test the result by,

```bash
$ pytest -v start_test.py
```

A successful result should be something like,

![passimage](./image/passimage.png)

For the solutions, you can refer to the `solution.py` file in each problem folder.

<br>



### 3. Spark SQL Questions

* How to transfer RDD to dataframes?

```
.toDF()
```

* How to transfer dataframes to RDD?

```
.rdd
```

* How to create a Spark session?

```
ss = SparkSession.builder.getOrCreate()
```

* How to create a Spark context from Spark session?

```
sc = ss.sparkContext
```

* What is the method we should call when transfer RDD to dataframes with schema?

```
createDataFrame
```

* How to show only the column with `column_name`?

```
select
```

* How to show the columns without `column_name`?

```
drop
```



### 4. Spark SQL R/W

* How to save the spark DataFrame as a table in the database?

```
use .write.saveAsTable()
```

* Suppose we have a spark dataframe `df`, then how to save it as a table named `test` in the database?

```
df.write.saveAsTable("test")
```

* What will be the content in the output? Suppose we have all the used variables defined.

```
ss = SparkSession.builder.getOrCreate()
df = ss.createDataFrame(business, business_schema)
df.write.saveAsTable('Business')
ss.stop()

ss = SparkSession.builder.getOrCreate()
ss.sql("select * from Business").show(5)
ss.stop()
```

Answer:

```
Error in line 7, because table path should be assigned.
```

* What will be the content in the output? Suppose we have all the used variables defined.

```
ss = SparkSession.builder.getOrCreate()
df = ss.createDataFrame(business, business_schema)
df.write.saveAsTable('Business')
ss.stop()

ss = SparkSession.builder.getOrCreate()
ss.sql("select * from parquet.`./spark-warehouse/Business`").show(5)
ss.stop()
```

Answer:

```
This code will print the first 5 lines of the table `Business`.
```

* What will be in the `./spark-warehouse` directory after executing the following program?

```
ss = SparkSession.builder.getOrCreate()
df = ss.createDataFrame(business, business_schema)
df.write.saveAsTable('Business')
ss.sql("drop table IF EXISTS Business")
ss.stop()
```

Answer:

```
Empty
```

* How to read a json file with name `./Business.json` and schema `business_schema` to spark dataframe `df`?

```
df = ss.read.json("./Business.json", business_schema)
```

* What's the data types in schema for the spark dataframe `df` after the following read?

```
df = ss.read.json("./Business.json")
```

Answer:

```
inferred data types
```

* How to read a csv file with name `./Business.csv` and schema `business_schema` to spark dataframe `df`?

```
df = ss.read.csv("./Business.csv", business_schema)
```

* What's the data types in schema for the spark dataframe `df` after the following read?

```
df = ss.read.csv("./Business.json")
```

Answer:

```
strings
```

* What's the data types in schema for the spark dataframe `df` after the following read?

```
df = ss.read.csv("./Business.json", inferSchema=True)
```

Answer:

```
inferred data types
```

* How to read parquet files from directory `./spark-warehouse/Business` and schema  `business_schema` to spark dataframe `df`?

```
df = ss.read.parquet("./spark-warehouse/Business", business_schema)
```

* How to write a json file to path `to/json/path` from spark dataframe `df`?

```
df.write.json("to/json/path")
```

* How to write a json file to path `to/csv/path` from spark dataframe `df`?

```
df.write.csv("to/csv/path")
```

* How to write parquet files to path `to/parquet/path` from spark dataframe `df`?

```
df.write.parquet("to/parquet/path")
```

* How to write parquet files to path `to/parquet/path` from spark dataframe `df` named as `Business`?

```
df.write.option("path", "to/parquet/path").saveAsTable("Business")
```

* Suppose the default partition number is 3. Then how many files in the `business_sf` directory after executing the following code?

```
business_df.write.csv("business_sf")
```

Answer:

```
4, 3 with a _SUCCESS file
```

* Suppose the default partition number is 3. How many files in the `business_sf` directory after executing the following code?

```
business_df.coalesce(1).write.csv("business_sf")
```

Answer:

```
2
```

* Suppose the default partition number is 3. How many files in the `business_sf` directory after executing the following code?

```
business_df.coalesce(2).write.csv("business_sf")
```

Answer:

```
3
```

* Suppose the default partition number is 3. How many files in the `business_sf` directory after executing the following code?

```
business_df.coalesce(5).write.csv("business_sf")
```

Answer:

```
4
```

* Suppose the default partition number is 3. How many files in the `business_sf` directory after executing the following code?

```
business_df.repartition(2).write.csv("business_sf")
```

Answer:

```
3
```

* Suppose the default partition number is 3. How many files in the `business_sf` directory after executing the following code?

```
business_df.repartition(5).write.csv("business_sf")
```

Answer:

```
6
```

* To read from/write to s3 bucket or MongoDB using Spark, it requires extra Jar files.

Answer:

```
True
```

* How to read spark dataframe from `s3a://example-test/mydata.json`?

```
df = ss.read.json("s3a://example-test/mydata.json")
```

* How to write parquet files to spark dataframe `df` to `s3a://example-test`?

```
df.write.parquet("s3a://example-test/mydata")
```

* Which field should we modify if we want to read from `mongodb+srv://...`?

```
spark.mongodb.input.uri
```

* Which field should we modify if we want to write to  `mongodb+srv://...`?

```
spark.mongodb.output.uri
```

* How to read spark dataframe from default MongoDB database?

```
df = spark.read.format('com.mongodb.spark.sql.DefaultSource').load()
```

* How to write spark dataframe `df` to the given uri with database `db` and collection `business`?

```
df.write.format("com.mongodb.spark.sql.DefaultSource")\
        .mode("overwrite")\
        .option("database","db")\
        .option("collection", "business")\
        .save()
```



### 5. Spark MLlib

* Spark ML are designed to run in parallel.

```
True
```

* What are the three components for spark ML?

```
transformers, estimators, evaluators
```

* What are the two Machine Learning API for Spark?

```
RDD-based, DataFrame-based
```

* What is the primary machine learning API for Spark now?

```
DataFrame-based
```

* Which of the following algorithm is not present in MLlib?
  *  Streaming Linear Regression
  *  Streaming KMeans
  *  None of the above

```
None of the above
```

* What is the definition of a transformer in Spark MLlib?

```
A transformer is an algorithm that transforms one dataframe into another dataframe.
```

* What is the definition of an estimator in Spark MLlib?

```
An estimator is an algorithm that can be applied on a dataframe to produce a Transformer.
```

* What is the definition of pipeline in Spark MLlib?

```
A Pipeline chains multiple Transformers and Estimators together to specify an ML workflow.
```

* Give three examples of transformers.

```
VectorAssembler, or the estimator after fitting the data
```

* Give four examples of estimators.

```
StringIndexer, OneHotEncoder, KMeans, RandomForestClassifier, DecisionTreeClassifier, LogisticRegression
```

* Give two examples of evaluators.

```
BinaryClassificationEvaluator, MulticlassClassificationEvaluator, RegressionEvaluator, ClusteringEvaluator
```

* Why do we use `.cache()` for ML models?

```
We don't have to reload the data or processing the data for a second time.
```

* Suppose we have an evaluator `eval` and a model `rf`, and we are give the validation set `valid_data`. Then how can we know the default evaluation of `eval` with `valid_data` for `rf`?

```
eval.evaluate(rf.transform(valid_data))
```

* Suppose we have a transformer `ohe` and the training and validation data are given as `train_data` and `valid_data`. Then what will be the output of the following program?

```
ohe.fit(train_data)
valid_data = ohe.transform(valid_data)
valid_data.show(5)
```

Answer:

```
Error. We should store thee ohe as oheModel and use this model to transform.

oheModel = ohe.fit(train_data)
valid_data = oheModel.transform(valid_data)
valid_data.show(5)
```

* Suppose we have a spark dataframe `df` and we want to split it into training and testing set with a proportion of 8:2. Then which method should we called?

```
training, testing = df.randomSplit([0.8, 0.2])
```

* It makes sense to use StandardScaler for decision tree. 

```
False
```

* It makes sense to use VectorAssembler for decision tree and logistic regression. 

```
True
```

* Suppose we have the transforms  work in the order of `si` , `ohe` , `va`. And we have a estimator of `rf`. Build a pipeline for showing for this workflow.

```
pipeline = Pipeline(stages=[si, ohe, va, rf])
```

* Suppose we have a pipeline estimator `p`. Then how to make predictions of `valid_data` based on `train_data`?

```
pModel = p.fit(train_data)
pred = pModel.transform(valid_data)
```

* Suppose we have a variable `paramGrid = ParamGridBuilder()` and a model `dt`. Then how to build a grid search of its attribute `maxDepth` with value of `grid_list`?

```
paramGridMap = paramGrid.addGrid(dt.maxDepth, grid_list).build()
```

* Kmeans prediction value is the same as the label.

```
False
```

* Spark MLlib algorithms are distributed.

```
True
```





### 6. Spark H2O

* H2O machine learning algorithms are distributed.

```
True
```

* H2O services on each node of a Spark cluster.

```
True
```

* What's the relationship between Sparkling water and Spark?

```
Sparkling water is the integration of H2O into spark.
```

* How to create a H2O context?

```
hc = H2OContext.getOrCreate()
```

* Which method should we call if we want to import a csv file with `file_path` as `h2o` dataframe?

```
h2o.import_file(file_path)
```

* What will be the column names for the output of the following code?

```
h2odf = h2o.import_file(file_path)
h2odf.show()
```

Answer:

```
C1, C2, ...
```

* What will be the column names for the output of the following code?

```
h2odf = h2o.import_file(file_path)
h2odf.set_names(col_names)
```

Answer:

```
col_names
```

* What will be the column names for the output of the following code?

```
h2odf = h2o.import_file(file_path)
h2odf = h2odf.set_names(col_names)
```

Answer:

```
col_names
```

* How can we convert a spark dataframe `df` to a h2o dataframe?

```
hc.asH2OFrame(df, frameName)
```

* How can we convert a h2o dataframe `df` to a spark dataframe?

```
hc.asSparkFrame(df)
```

* All the schma of the original Spark Dataframe is preserved when you convert to an h2o dataframe.

```
False
```

* What's Auto ML?

```
Auto ML means automatic training and tuning of many models within a time limit or model count.
```

* H2O autoML builds ensemble models as well.

```
True
```

* Suppose we have a H2O AutoML model `model` after training. Then which method should we call to see the rank of tried models?

```
model.leaderboard
```

* Suppose we have a H2O AutoML model `model` after training. Then which method should we call to see the details of best tried models?

```
model.leaderboard.get_best_model()
```

* How to see the performance of a H2O model `model` on the validation set `val`?

```
model.explain(val)
```

* How to get the predictions of a H2O model `model` on the validation set `val`?

```
model.predict(val)
```



