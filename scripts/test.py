from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("Example").getOrCreate()

# Example: Creating a DataFrame with some data
data = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Display schema
df.printSchema()

# Show first few rows
df.show()



