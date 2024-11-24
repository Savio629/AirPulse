# AirPulse - Air Quality Data Pipeline using Kafka, Spark, Prometheus & Grafana
This project demonstrates a real-time data processing pipeline using Kafka for data streaming, Spark for data consumption, and Prometheus & Grafana for monitoring and visualization.

### Video Demo
https://drive.google.com/file/d/1l4r6creOCans7qDsRqUkSANjrbVG9z7K/view?usp=sharing

Directory Structure
```
.
├── kafka-producer
│   ├── producer.py
│   ├── air_quality_data.csv
│   └── requirements.txt
├── spark-consumer
│   ├── consumer.py
│   └── requirements.txt
├── Dockerfile.kafka
├── Dockerfile.spark
├── prometheus.yml
├── docker-compose.yml
└── README.md
```
Prerequisites

Make sure you have the following software installed on your system:

- Docker
- Docker Compose

Setup Instructions
1. Clone the Repository
```
git clone <repository-url>
cd <repository-directory>
```
2. Prepare Docker Environment
Ensure that Docker is running on your machine.

3. Build and Run Containers
Use Docker Compose to build and run all the services:
```
docker-compose up --build
```
This command will:

Set up Zookeeper and Kafka for handling the data pipeline.
Spin up Spark for consuming Kafka data.
Launch Prometheus and Grafana for monitoring and visualization.

4. Access the Services
-  Prometheus: http://localhost:9090 

- Grafana: http://localhost:3000

- Default credentials: admin/admin

5. Running the Producer and Consumer
Kafka Producer
The producer sends data from the air_quality_data.csv file to the Kafka topic air_quality.

To run the producer:
Open a terminal window.
Enter the Kafka container:
```
docker-compose exec kafka
```
Inside the container, run the producer script:
```
python3 /kafka-producer/producer.py
```
Spark Consumer

The consumer reads data from the Kafka topic air_quality and prints it to the console.

To run the consumer:
Open another terminal window.
Enter the Spark container:
```
docker-compose exec spark 
```
Inside the container, run the consumer script:
```
python3 /spark-consumer/consumer.py
```
6. Visualization in Grafana
Add Prometheus Data Source in Grafana:

- Go to Configuration > Data Sources > Add data source.
- Select Prometheus.
- Set the URL to http://prometheus:9090 and save.

Create Dashboard:

- Go to Create > Dashboard.
- Add a new panel.

Use the following example queries:

For Kafka producer messages sent:
```
kafka_producer_messages_sent_total
```

For Spark consumer messages consumed:

```
spark_consumer_messages_consumed_total
```

Save the dashboard to visualize the data flow.

Explanation of Components

Kafka Producer
- Reads the air quality dataset and sends each row to the Kafka topic air_quality.

Spark Consumer
- Reads the streaming data from the Kafka topic and prints it to the console.

Prometheus
- Monitors the metrics from Kafka Producer and Spark Consumer.

Grafana
- Visualizes the real-time data and metrics using graphs, counters, and dashboards.

Stopping the Project
To stop the entire setup, run:

```
docker-compose down
```

Troubleshooting

Kafka Not Connecting
Ensure that Kafka is connected to Zookeeper by checking the logs.

Restart the Kafka service if necessary:
```
docker-compose restart kafka
```

Grafana and Prometheus Connection Issues

- Make sure the Prometheus URL in Grafana is set correctly (http://prometheus:9090).
- Ensure all containers are running:
```
docker ps
```
