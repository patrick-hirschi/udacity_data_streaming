## Data Streaming Nanodegree - SF Crime Statistics with Spark Streaming 

**Commands used**

  1. Start Zookeeper: /usr/bin/zookeeper-server-start config/zookeeper.properties
  2. Start: Kafka Server: /usr/bin/kafka-server-start config/server.properties
  3. Initialize Workspace: .start.sh
  4. Start Kafka Console Consumer: /usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.dep.police.service --from-beginning
  5. Spark Submit: spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

**1. SparkSession Parameters affecting Throughput and Latency**

spark.streaming.receiver.maxRate:  Setting this configuration to 0 or a negative number will put no limit on the rate.


**2. Most efficient SparkSession Property Key-Value Pairs**

spark.streaming.kafka.maxRatePerPartition: The maximum rate (in messages per second) at which each Kafka partition will be read by this direct API
spark.default.parallelism: Defaults to the number of all cores on all machines. Best fitting number can be calculated by dividing the total input dataset size by the partition size. E.G. an input of 1.5 gigabytes with a partition size of 128MB would result in 1500 / 128 = 11.71 = 12 partitions.