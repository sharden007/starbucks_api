from flask import Flask, jsonify, request
import psycopg2
from urllib.parse import quote as url_quote  # Use urllib.parse.quote instead of werkzeug.urls.url_quote

app = Flask(__name__)

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(
            database="dashboard_db",
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        app.logger.error(f"Database connection failed: {e}")
        raise

# API endpoint to fetch sales data
@app.route('/data', methods=['GET'])
def fetch_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales_data;")  # Replace with your table name
        rows = cur.fetchall()
        cur.close()
        conn.close()

        # Format data as JSON
        data = [{"id": row[0], "product": row[1], "sales": row[2]} for row in rows]
        return jsonify(data), 200
    except Exception as e:
        app.logger.error(f"Error fetching data: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500

# Example usage of url_quote (if needed)
@app.route('/encode', methods=['GET'])
def encode_url():
    url = request.args.get('url', '')
    encoded_url = url_quote(url)  # Use urllib.parse.quote for encoding URLs
    return jsonify({"encoded_url": encoded_url})

# Error handler for 404
@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
