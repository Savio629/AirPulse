# spark-consumer/consumer.py
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Kafka Spark Consumer") \
    .getOrCreate()

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "air_quality") \
    .load()

# Convert the value from Kafka to string
df = df.selectExpr("CAST(value AS STRING)")

# Print the data to the console
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
