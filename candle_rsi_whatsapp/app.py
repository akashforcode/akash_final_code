from flask import Flask, render_template, jsonify
import random
import numpy as np
import time

app = Flask(__name__)
app = Flask(__name__)
from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'ACb31e2c0607bfdf7a94056efeb6855b32'
auth_token = '387370462e5c2c9b09b199f28a1d7c99'
client = Client(account_sid, auth_token)


# Message details
from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
to_whatsapp_number = 'whatsapp:+919555711143'  # Your WhatsApp number
#message_body = 'Hello from Twilio!'

def sendm():
    global message
    message = client.messages.create(body='Check out this funny picture!',
                       media_url='https://raw.githubusercontent.com/dianephan/flask_upload_photos/main/UPLOADS/DRAW_THE_OWL_MEME.png',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
    print(f"Message SID: {message.sid}")
# Global variables
candle_data = []
rsi = 0

# Function to generate random candle data
def generate_candle_data():
    global candle_data
    candle_data = []
    for i in range(50):
        open_price = random.uniform(100, 200)
        close_price = random.uniform(100, 200)
        high_price = max(open_price, close_price, random.uniform(100, 200))
        low_price = min(open_price, close_price, random.uniform(100, 200))
        candle_data.append({
            'time': i,
            'open': open_price,
            'close': close_price,
            'high': high_price,
            'low': low_price
        })

# Function to calculate RSI
def calculate_rsi(data, period=14):
    deltas = np.diff(data)
    seed = deltas[:period + 1]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down
    rsi = np.zeros_like(data)
    rsi[:period] = 100. - 100. / (1. + rs)

    for i in range(period, len(data)):
        delta = deltas[i - 1]

        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up * (period - 1) + upval) / period
        down = (down * (period - 1) + downval) / period

        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)

    return rsi[-1]

# Function to check RSI and print "Hello" if RSI is less than 30
def check_rsi():
    global rsi
    rsi = calculate_rsi([candle['close'] for candle in candle_data])
    if rsi < 45:
        sendm()
        return "Hello"
    else:
        return ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_candle_data')
def get_candle_data():
    generate_candle_data()
    return jsonify(candle_data)

@app.route('/get_rsi')
def get_rsi():
    global rsi
    return jsonify({'rsi': rsi})

@app.route('/check_hello')
def check_hello():
    return check_rsi()

if __name__ == '__main__':
    app.run(debug=True)
