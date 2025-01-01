from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'alexkingaus99@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'X5$E@8CFGHQ!$'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'alexkingaus99@gmail.com'

mail = Mail(app)

@app.route('/submit', methods=['POST'])
def submit_contact_form():
    try:
        data = request.json  # Parse JSON data sent from the frontend
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        # Send email
        msg = Message(subject=f"New Contact Form Submission: {subject}",
                      recipients=['alexkingaus99@gmail.com'])  # Replace with recipient email
        msg.body = f"From: {name} <{email}>\n\n{message}"
        mail.send(msg)

        return jsonify({"success": True, "message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
