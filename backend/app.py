import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kafka import KafkaProducer
from datetime import datetime
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


@app.get("/")
def home():
    return {"message": "Kafka Producer Running"}


@app.post("/order")
def send_order(order_id: int):

    data = {
        "orderId": order_id,
        "timestamp": datetime.now().isoformat()
    }

    producer.send("orders", data)
    producer.flush()

    return {
        "status": "success",
        "data": data
    }


@app.post("/payment")
def send_payment(order_id: int):

    data = {
        "orderId": order_id,
        "timestamp": datetime.now().isoformat()
    }

    producer.send("payments", data)
    producer.flush()

    return {
        "status": "success",
        "data": data
    }
    
    
@app.get("/events")
def get_events():

    conn = sqlite3.connect("../processor/events.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM events
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


@app.get("/stats")
def get_stats():

    conn = sqlite3.connect("../processor/events.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM events")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM events
        WHERE status='MATCHED'
    """)
    matched = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM events
        WHERE status='DISCARDED'
    """)
    discarded = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM events
        WHERE status='EXPIRED'
    """)
    expired = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "matched": matched,
        "discarded": discarded,
        "expired": expired
    }