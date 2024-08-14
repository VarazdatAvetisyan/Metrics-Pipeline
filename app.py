import os
import psycopg2
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://user:password@db:5432/metrics_db')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/ingest/talked_time', methods=['POST'])
def ingest_talked_time():
    metrics = request.json

    if not metrics:
        return jsonify({"error": "No data provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO talked_time_metrics (user_id, session_id, talked_time, timestamp)
    VALUES (%s, %s, %s, %s)
    """

    data = []
    for metric in metrics:
        data.append((
            metric.get('user_id', str(uuid.uuid4())),
            metric.get('session_id', str(uuid.uuid4())),
            metric.get('talked_time', 0),
            metric.get('timestamp', datetime.utcnow())
        ))

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "success"}), 200

@app.route('/ingest/microphone_used', methods=['POST'])
def ingest_microphone_used():
    metrics = request.json

    if not metrics:
        return jsonify({"error": "No data provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO microphone_used_metrics (user_id, session_id, microphone_used, timestamp)
    VALUES (%s, %s, %s, %s)
    """

    data = []
    for metric in metrics:
        data.append((
            metric.get('user_id', str(uuid.uuid4())),
            metric.get('session_id', str(uuid.uuid4())),
            metric.get('microphone_used', False),
            metric.get('timestamp', datetime.utcnow())
        ))

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "success"}), 200

@app.route('/ingest/speaker_used', methods=['POST'])
def ingest_speaker_used():
    metrics = request.json

    if not metrics:
        return jsonify({"error": "No data provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO speaker_used_metrics (user_id, session_id, speaker_used, timestamp)
    VALUES (%s, %s, %s, %s)
    """

    data = []
    for metric in metrics:
        data.append((
            metric.get('user_id', str(uuid.uuid4())),
            metric.get('session_id', str(uuid.uuid4())),
            metric.get('speaker_used', False),
            metric.get('timestamp', datetime.utcnow())
        ))

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "success"}), 200

@app.route('/ingest/voice_sentiment', methods=['POST'])
def ingest_voice_sentiment():
    metrics = request.json

    if not metrics:
        return jsonify({"error": "No data provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO voice_sentiment_metrics (user_id, session_id, sentiment_score, timestamp)
    VALUES (%s, %s, %s, %s)
    """

    data = []
    for metric in metrics:
        data.append((
            metric.get('user_id', str(uuid.uuid4())),
            metric.get('session_id', str(uuid.uuid4())),
            metric.get('sentiment_score', None),
            metric.get('timestamp', datetime.utcnow())
        ))

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
