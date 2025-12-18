from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    db = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )
    cursor = db.cursor()
    cursor.execute("SELECT 'Two Tier Docker App Running Successfully!'")
    result = cursor.fetchone()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
