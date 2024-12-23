# WhatsApp Message Scheduler

A simple Flask-based web application that allows users to schedule WhatsApp messages to be sent at a specific time using the [Twilio API](https://www.twilio.com/). This project enables users to send messages to WhatsApp numbers at a scheduled time, making it easier to automate notifications, reminders, or important messages.

## Features

- Schedule WhatsApp messages at a specific time.
- Simple and user-friendly interface.
- Built using Flask for the backend and HTML for the frontend.
- Uses Twilio API to send messages to WhatsApp numbers.

## Prerequisites

Before you start, make sure you have the following:

- Python installed on your system.
- A Twilio account with your **Account SID** and **Auth Token**.
- Flask and Twilio Python SDK installed.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kshitizjangra/whatsapp-message-scheduler.git
   cd whatsapp-message-scheduler

2. Install required python packages.
3. After that, replace the ACCOUNT SID and AUTH TOKEN with yours in main.py.
4. Also, open index.html, from Templates.
5. Then, run the main.py
6. After running main.py, open the flask url in your browser, (http://127.0.0.1:5000/)
7. Later on, Enter the following details in the form:
Phone Number: The recipient's phone number (must be in WhatsApp format, e.g., +91XXXXXXXXXX).
Message: The message you want to send.
Scheduled Time: The time you want to send the message (in 12-hour format).
Click on the Schedule Message button.
The message will be sent at the specified time via WhatsApp.


### Important Notes:

- **Replace** `your_account_sid` and `your_auth_token` with the values from your ---**Twilio Console** in the `main.py` file. Do not share them publicly.
