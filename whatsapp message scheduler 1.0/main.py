from flask import Flask, render_template, request
from twilio.rest import Client
from datetime import datetime
import time

app = Flask(__name__)

# Twilio credentials (from your free trial account)
account_sid = 'AC237a347c5679e025031c3087d4a801fd'
auth_token = '2c22da73fcf71dfa0c2312021687ea43'
client = Client(account_sid, auth_token)

@app.route("/", methods=["GET", "POST"])
def schedule_message():
    """
    Main route to handle the message scheduling.
    It renders the form and processes the scheduling logic.
    """
    if request.method == "POST":
        # Fetching input data from the form
        phone_number = request.form.get("phone")
        message = request.form.get("message")
        scheduled_time = request.form.get("time")  # format (12 Hrs.): HH:MM:AM/PM

        try:
            # Getting the current time
            current_time = datetime.now()

            # Parsing the scheduled time into a datetime object
            scheduled_time_obj = datetime.strptime(scheduled_time, "%H:%M")

            # Setting the scheduled time with today's date
            scheduled_time_obj = scheduled_time_obj.replace(
                year=current_time.year, month=current_time.month, day=current_time.day
            )

            # Calculating the delay (in seconds) until the scheduled time
            delay_seconds = (scheduled_time_obj - current_time).total_seconds()

            # Validate the delay
            if delay_seconds < 0:
                return "Error: Scheduled time must be in the future.."

            # Waiting for the scheduled time to send the message
            time.sleep(delay_seconds)

            # Sending the WhatsApp message using Twilio API
            client.messages.create(
                body=message,
                from_='whatsapp:+14155238886',  # Twilio's sandbox number
                to=f'whatsapp:{phone_number}'
            )

            return f"Message sent successfully at {scheduled_time_obj.strftime('%H:%M')}."

        except Exception as e:
            # Handling any unexpected errors
            return f"Something went wrong: {str(e)}"

    # Render the form for GET requests
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
