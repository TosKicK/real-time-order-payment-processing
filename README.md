# Real-Time Order Payment Processing System

## Overview

This project is a distributed event processing system that simulates real-time order and payment streams using Apache Kafka. The system processes events, performs stream joining, applies watermark logic for late events, stores processed results in SQLite, and visualizes the results through a React dashboard.

---

## Features

* Real-time Order and Payment event streaming
* Apache Kafka Producer-Consumer architecture
* Stream Join Logic
* Watermark-based event expiration
* SQLite database persistence
* FastAPI REST APIs
* React Dashboard
* Live Statistics
* Event Visualization using Pie Chart
* Auto-refreshing UI

---

## System Architecture

```text
React Dashboard
       │
       ▼
    FastAPI
       │
       ▼
     Kafka
   ┌────┴────┐
   ▼         ▼
Orders    Payments
   │         │
   └────┬────┘
        ▼
  Python Consumer
  (Join + Watermark)
        │
        ▼
     SQLite
```

---

## Technology Stack

### Frontend

* React
* Axios
* Chart.js
* CSS

### Backend

* FastAPI
* Uvicorn

### Streaming

* Apache Kafka
* Zookeeper

### Database

* SQLite

### Containerization

* Docker
* Docker Compose

---

# Project Structure

```text
dsproject
│
├── backend
│   └── app.py
│
├── processor
│   ├── consumer.py
│   ├── database.py
│   └── events.db
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# Prerequisites

Install:

* Python 3.10+
* Node.js
* Docker Desktop
* Git

---

# Installation Guide

## 1. Clone Repository

```bash
git clone <repository-url>
cd dsproject
```

---

## 2. Start Kafka and Zookeeper

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

Expected containers:

```text
kafka
zookeeper
```

---

## 3. Create Kafka Topics

```bash
docker exec -it kafka bash
```

Create Orders Topic:

```bash
kafka-topics \
--create \
--topic orders \
--bootstrap-server localhost:9092
```

Create Payments Topic:

```bash
kafka-topics \
--create \
--topic payments \
--bootstrap-server localhost:9092
```

Verify:

```bash
kafka-topics \
--list \
--bootstrap-server localhost:9092
```

Expected:

```text
orders
payments
```

---

## 4. Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn kafka-python
```

Start server:

```bash
uvicorn app:app --reload
```

Backend available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Consumer Setup

Open a new terminal:

```bash
cd processor
```

Install dependency:

```bash
pip install kafka-python
```

Run consumer:

```bash
python consumer.py
```

Expected output:

```text
Consumer running...
```

---

## 6. Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
npm install axios
npm install chart.js react-chartjs-2
```

Run:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# Usage

## Create Order

Using Swagger:

```text
POST /order
```

Example:

```text
order_id = 1
```

---

## Create Payment

```text
POST /payment
```

Example:

```text
order_id = 1
```

---

# Event Processing Logic

## MATCHED

Payment arrives within 10 seconds of order.

```text
Order -> Payment (<=10 sec)
```

Status:

```text
MATCHED
```

---

## DISCARDED

Payment arrives after 10 seconds.

```text
Order -> Payment (>10 sec)
```

Status:

```text
DISCARDED
```

---

## EXPIRED

No payment received within 30 seconds.

Status:

```text
EXPIRED
```

---

# API Endpoints

| Method | Endpoint | Description              |
| ------ | -------- | ------------------------ |
| GET    | /        | Health Check             |
| POST   | /order   | Create Order Event       |
| POST   | /payment | Create Payment Event     |
| GET    | /events  | Get Processed Events     |
| GET    | /stats   | Get Dashboard Statistics |

---

# Dashboard Features

* Live Event Monitoring
* Real-time Statistics
* Pie Chart Visualization
* Event History Table
* Auto Refresh Every 3 Seconds

---

# Future Enhancements

* Dockerized FastAPI and Consumer
* PostgreSQL Integration
* Redis Caching
* Authentication
* Multi-Broker Kafka Cluster
* Kubernetes Deployment

---

# Author

Abhiroop Banerjee

Distributed Systems Project

Apache Kafka • FastAPI • React • Docker • SQLite
