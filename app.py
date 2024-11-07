from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# MySQL configuration for connecting to AWS RDS
db_config = {
    'host': 'database-1.c9s0wmuw2ri0.ap-south-1.rds.amazonaws.com',  # Replace with your RDS endpoint
    'user': 'user01',      # Replace with your MySQL username
    'password': 'Admin123',  # Replace with your MySQL password
    'database': 'flask_input_db'   # Replace with your database name
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name parameter is required!"}), 400

    # Connect to the MySQL database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    try:
        # Insert data into the `flask-input-db` table
        cursor.execute("INSERT INTO `flasktable` (name) VALUES (%s)", (name,))
        connection.commit()
        return jsonify({"message": "Data saved successfully!"}), 201
    except Exception as e:
        print("Error:", e)  # Log the error to the console
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
