from flask import Flask, request, jsonify, render_template
import sqlite3
import time
import threading
import random

app = Flask(__name__)

# Initialize database for structured data storage
def init_db():
    conn = sqlite3.connect('luel_parser.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS parsed_logs
                 (id INTEGER PRIMARY KEY, modality TEXT, status TEXT, parsing_time REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # Serves your glassmorphism UI
    return render_template('index.html')

@app.route('/api/parse', methods=['POST'])
def parse_stream():
    data = request.json
    modality = data.get('modality', 'unknown')
    
    # Simulate an optimized asynchronous chunking and parsing blueprint
    start_time = time.time()
    # Your optimized script logic would run here; we simulate a fast parse
    time.sleep(random.uniform(0.05, 0.25)) 
    parsing_time = time.time() - start_time
    
    # Log the lifecycle stage to the database
    conn = sqlite3.connect('luel_parser.db')
    c = conn.cursor()
    c.execute("INSERT INTO parsed_logs (modality, status, parsing_time) VALUES (?, ?, ?)", 
              (modality, 'Success', parsing_time))
    conn.commit()
    conn.close()
    
    return jsonify({
        "status": "success", 
        "parsing_time": parsing_time, 
        "modality": modality
    })

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    # Fetch real-time system monitor metrics
    conn = sqlite3.connect('luel_parser.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*), AVG(parsing_time) FROM parsed_logs")
    row = c.fetchone()
    conn.close()
    
    return jsonify({
        "total_parsed": row[0] or 0,
        "avg_parse_time": row[1] or 0.0,
        "active_threads": threading.active_count()
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)