import sqlite3
from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Email configuration
# Install the smtplib library (if you haven't already) by running "pip install secure-smtplib".
EMAIL_ADDRESS = 'your_email@example.com' # make sure you have a verified email account (e.g., Gmail) that you can use to send emails.
EMAIL_PASSWORD = 'your_email_password' # If your email account has 2-step verification use this link to generate a password "https://myaccount.google.com/apppasswords"
SMTP_SERVER = 'smtp.example.com' # For gmail, the most common SMTP server is smtp.gmail.com
SMTP_PORT = 587
DATABASE_URL = "database.db"
AGENTS_DB = "agents.db"
CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contact TEXT, email TEXT)"
CREATE_AGENT_SQL = "CREATE TABLE IF NOT EXISTS agents (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT)"

# Fetch data from the database
def fetch_data_from_database():
    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        print("Error fetching data from database:", e)
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login_page')
def login():
    return render_template('login.html')

@app.route('/images')
def gallery():
    return render_template('gallery.html')

@app.route('/registration_form')
def registration_form():
    return render_template('registration_form.html')

@app.route('/register.action', methods=['POST'])
def register():
    name = request.form['name']
    contact = request.form['contact']
    email = request.form['email']
    
    # Send notification email
    recipient_email = 'agent_email@example.com'
    subject = 'New Form Submission'
    message = 'A new form has been submitted. Please contact ' + name + ' on ' + contact + ' or email ' + email + ' to confirm a viewing.'
    send_notification_email(recipient_email, subject, message)

    try:
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_SQL)
        cursor.execute("INSERT INTO contacts (name, contact, email) VALUES (?, ?, ?)", (name, contact, email))
        conn.commit()
        conn.close()
        return render_template('success.html')
    except Exception as e:
        print("Error submitting form:", str(e))
        return "Error submitting form. Please try again later.", 500
    
@app.route('/new_agent', methods=['POST'])
def add_agent():
    email_address = request.form['email']
    
    try:
        conn = sqlite3.connect(AGENTS_DB)
        cursor = conn.cursor()
        cursor.execute(CREATE_AGENT_SQL)
        cursor.execute("INSERT INTO agents (email) VALUES (?)", (email_address,))
        conn.commit()
        conn.close()
        return render_template('login.html')
    except Exception as e:
        print("Error submitting form:", str(e))
        return "Error submitting form. Please try again later.", 500
    
def send_notification_email(recipient_email, subject, message):
    # Create message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()  
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  
        smtp.send_message(msg)  

@app.route('/view_database', methods=['POST'])
def view_database():
    submitted_email = request.form['email']

    # Check if submitted email is in the agents database
    try:
        conn = sqlite3.connect(AGENTS_DB)
        cursor = conn.cursor()
        cursor.execute(CREATE_AGENT_SQL)
        cursor.execute("SELECT * FROM agents WHERE email=?", (submitted_email,))
        agent = cursor.fetchone()
        conn.close()
        if agent:
            # Email is found in the database, proceed to fetch data
            data = fetch_data_from_database()
            return render_template('view_database.html', data=data)
        else:
            # Email is not found in the database, render verification page
            return render_template('verify_agent.html')
    except sqlite3.Error as e:
        print("Error checking email in database:", e)
        return "Error occurred. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)
