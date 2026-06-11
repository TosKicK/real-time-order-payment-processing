import json
import sqlite3
import threading
import time
from datetime import datetime

from kafka import KafkaConsumer

# Database
conn = sqlite3.connect("events.db", check_same_thread=False)
cursor = conn.cursor()

# In-memory storage
orders = {}


def save_event(order_id, order_time, payment_time, status):
    cursor.execute(
        """
        INSERT INTO events
        (order_id, order_time, payment_time, status)
        VALUES (?, ?, ?, ?)
        """,
        (order_id, order_time, payment_time, status)
    )
    conn.commit()


# Orders Consumer
orders_consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="orders-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

# Payments Consumer
payments_consumer = KafkaConsumer(
    "payments",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="payments-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)


def consume_orders():
    for message in orders_consumer:
        data = message.value

        order_id = data["orderId"]

        orders[order_id] = {
            "timestamp": datetime.fromisoformat(
                data["timestamp"]
            )
        }

        print(f"ORDER RECEIVED: {order_id}")


def consume_payments():
    for message in payments_consumer:
        data = message.value

        order_id = data["orderId"]

        payment_time = datetime.fromisoformat(
            data["timestamp"]
        )

        if order_id not in orders:
            print(f"PAYMENT WITHOUT ORDER: {order_id}")
            continue

        order_time = orders[order_id]["timestamp"]

        diff = (
            payment_time - order_time
        ).total_seconds()

        if diff <= 10:
            status = "MATCHED"
        else:
            status = "DISCARDED"

        save_event(
            order_id,
            order_time.isoformat(),
            payment_time.isoformat(),
            status
        )

        print(f"{status}: Order {order_id}")

        del orders[order_id]


def watermark_checker():
    while True:
        current_time = datetime.now()

        expired = []

        for order_id, value in orders.items():
            diff = (
                current_time -
                value["timestamp"]
            ).total_seconds()

            if diff > 30:
                save_event(
                    order_id,
                    value["timestamp"].isoformat(),
                    None,
                    "EXPIRED"
                )

                expired.append(order_id)

                print(f"EXPIRED: {order_id}")

        for order_id in expired:
            del orders[order_id]

        time.sleep(5)


threading.Thread(
    target=consume_orders,
    daemon=True
).start()

threading.Thread(
    target=consume_payments,
    daemon=True
).start()

threading.Thread(
    target=watermark_checker,
    daemon=True
).start()

print("Consumer running...")

while True:
    time.sleep(1)