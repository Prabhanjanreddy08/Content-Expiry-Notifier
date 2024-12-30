from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('content.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            expiry_date DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('content.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM content')
    items = cursor.fetchall()
    conn.close()

    # Check if content is expiring soon
    today = datetime.now()
    expiring_soon = [
        item for item in items if datetime.strptime(item[3], '%Y-%m-%d') <= today + timedelta(days=3)
    ]
    
    return render_template('index.html', items=items, expiring_soon=expiring_soon)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        expiry_date = request.form['expiry_date']
        
        conn = sqlite3.connect('content.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO content (title, description, expiry_date) VALUES (?, ?, ?)', 
                       (title, description, expiry_date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:content_id>')
def delete(content_id):
    conn = sqlite3.connect('content.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM content WHERE id = ?', (content_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/content/<int:item_id>')
def content_detail(item_id):
    conn = sqlite3.connect('content.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM content WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    conn.close()

    if not item:
        return "Content not found", 404

    return render_template('content_detail.html', item=item)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
