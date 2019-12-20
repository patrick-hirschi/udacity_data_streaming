"""Configures a Kafka Connector for Postgres Station data"""
import json
import logging

import requests


logger = logging.getLogger(__name__)


KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
CONNECTOR_NAME = "stations"

def configure_connector():
    """Starts and configures the Kafka Connect connector"""
    logging.debug("creating or updating kafka connect connector...")

    rest_method = requests.post
    resp = requests.get(f"{KAFKA_CONNECT_URL}/{CONNECTOR_NAME}")
    if resp.status_code == 200:
        return

    resp = rest_method(
        KAFKA_CONNECT_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(
            {
                "name": CONNECTOR_NAME,
                "config": {
                    "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
                    "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                    "key.converter.schemas.enable": "false",
                    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                    "value.converter.schemas.enable": "false",
                    "connection.url": "jdbc:postgresql://127.0.0.1:5432/cta", # Thanks to: elisa romondia: https://github.com/elisaromondia/CTA-KAFKA-APACHE
                    "connection.user": "cta_admin",
                    "connection.password": "chicago",
                    "table.whitelist": "stations",
                    "mode": "incrementing",
                    "incrementing.column.name": "stop_id",
                    "topic.prefix": "org.chicago.cta.",
                    "poll.interval.ms": "3600000",
                    "batch.max.rows": "500",
                },
            }
        ),
    )

    # Ensure a healthy response was given
    resp.raise_for_status()
    logging.debug("connector created successfully")


if __name__ == "__main__":
    configure_connector()