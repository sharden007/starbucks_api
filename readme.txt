Complete implementation for integrating a PostgreSQL database 
with a Flask backend and updating the frontend to periodically fetch 
data from the backend API. The solution includes robust error handling 
for both the backend and frontend.

Run:
Ensure PostgreSQL is running and configured.

Run the Flask app:

$ python app.py

http://localhost:3000/data


Error Handling:
Backend:
Database connection issues are logged and returned as JSON error responses.
Custom error handlers are defined for HTTP 404 and 500 errors.

If CORS error:
Enable CORS in your Flask app using Flask-CORS: (app.py) file

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins

or Alternatively, restrict access to specific origins: (app.py) file

CORS(app, resources={r"/data": {"origins": "http://localhost:5500"}})