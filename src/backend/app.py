from flask import Flask, session, request, render_template, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import smtplib  
import os
import schedule 
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
app = Flask(__name__)
from threading import Thread

import secrets
app.secret_key = secrets.token_hex(16)  # A secure, randomly generated key


# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["WATERHYDRATOR"]
users_collection = db["users"]

# Route to render the signup form
@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

# Route to handle form submission
@app.route('/signup', methods=['POST'])
def signup():
    # Get form data
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if the user already exists
    if users_collection.find_one({"email": email}):
        flash("Email already registered. Please use a different email or log in.", "error")
        return redirect(url_for('signup_form'))

    # Hash the password and insert user
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": hashed_password
    })

    # Redirect to index.html after successful signup
    return redirect(url_for('index'))

# Route for index page
@app.route('/index')
def index():
    return render_template('index.html')


# Route to render the login form
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Find the user in the database
        user = users_collection.find_one({"email": email})

        if user:
            # Check if the password is correct
            if check_password_hash(user['password'], password):
                session['user_id'] = str(user["_id"])
                return redirect(url_for('index'))  # Redirect to the main page after login
            else:
                # Password mismatch
                flash("Incorrect password. Please try again.", "error")
        else:
            # User not found
            flash("User not found. Please check your email or sign up.", "error")

    return render_template('login.html')  # Render the login page for GET requests

# Route for the home page (index)
@app.route('/index', methods=['GET'])
def home():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login_form'))

# Route to display account information
@app.route('/account', methods=['GET'])
def account():
    if 'user_id' in session:
        # Retrieve the user's information from the database
        user = users_collection.find_one({"_id": ObjectId(session['user_id'])})
        if user:
            return render_template('account.html', user=user)
    return redirect(url_for('login_form'))

# Route to render the help page
@app.route('/help', methods=['GET'])
def help_page():
    return render_template('help.html')
    
# Route to render the forget password form
@app.route('/forgot_password', methods=['GET'])
def forgot_password_form():
    return render_template('forgot_password.html')

# Route to handle forget password form submission
@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    email = request.form.get('email')
    user = users_collection.find_one({"email": email})

    if user:
        # Generate a secure token for password reset
        reset_token = secrets.token_urlsafe(16)

        # Store the reset token in the database (you can also add an expiry time)
        users_collection.update_one({"email": email}, {"$set": {"reset_token": reset_token}})

        # Send the email with the reset link
        reset_link = f"http://127.0.0.1:5000/reset_password/{reset_token}"
        try:
            send_email(email, reset_link)
            return jsonify({"status": "success", "message": "Password reset link has been sent to your email."}), 200
        except Exception as e:
            print("Error sending email:", e)
            return jsonify({"status": "error", "message": "An error occurred while sending the email. Please try again later."}), 500
    else:
        return jsonify({"status": "error", "message": "Email not found. Please try again."}), 404

# Function to send email
def send_email(to_email, reset_link):
    from_email = "sreelikhitha333@gmail.com"
    from_password = "fmpk fwbk oumm nmjf"  
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, from_password)
        message = f"Subject: Password Reset\n\nClick the link to reset your password: {reset_link}"
        server.sendmail(from_email, to_email, message)

# Route to handle the reset password logic
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'GET':
        return render_template('reset_password.html', token=token)
    else:
        # Handle the form submission
        new_password = request.form.get('password')
        hashed_password = generate_password_hash(new_password)

        # Update the password in the database
        result = users_collection.update_one(
            {"reset_token": token},
            {"$set": {"password": hashed_password}, "$unset": {"reset_token": ""}}
        )

        if result.modified_count > 0:
            # Return a success JSON response
            return jsonify({"status": "success", "message": "Your password has been reset successfully."}), 200
        else:
            # Return an error JSON response if the token is invalid or update failed
            return jsonify({"status": "error", "message": "Failed to reset password. Please try again."}), 400



def send_hydration_email(to_email):
    # Configure email settings
    from_email = "sreelikhitha333@gmail.com"
    from_password = "fmpk fwbk oumm nmjf" 

    # Email content
    subject = "Hydration Reminder"
    body = """
    Hi there!

    This is a friendly reminder to drink water and stay hydrated. 
    Your health matters, and drinking water is a key part of staying healthy!

    Stay hydrated,
    The AquaSync Team
    """
    # Create the email
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.send_message(message)
            print(f"Hydration reminder sent to {to_email}.")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")
      
def send_email_to_all_users():
    current_hour = datetime.now().hour
    if 8 <= current_hour <= 20:  # Send emails between 8 AM and 8 PM
        users = users_collection.find()
        for user in users:
            send_hydration_email(user['email'])
            
# Schedule the task to run every 2 hours
schedule.every(0.1).hours.do(send_email_to_all_users)

def run_scheduler():
    print("Starting the scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait 1 second between checks


if __name__ == "__main__":
    # Start the scheduler in a separate thread
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    # Start the Flask app
    app.run(debug=True)
