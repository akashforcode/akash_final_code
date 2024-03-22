from flask import Flask, render_template, request, send_file
from twilio.rest import Client
from selenium import webdriver
import os
import time
from urllib3 import request

app = Flask(__name__)

# Twilio credentials
account_sid = 'ACb31e2c0607bfdf7a94056efeb6855b32'
auth_token = '387370462e5c2c9b09b199f28a1d7c99'
client = Client(account_sid, auth_token)

# Function to take screenshot of webpage
def take_screenshot(url, screenshot_path):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.save_screenshot(screenshot_path)
    driver.quit()

# Function to send screenshot via Twilio WhatsApp
def send_whatsapp_message(screenshot_path, to_number):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Screenshot of the current page:',
        #media_url=[f'file://{screenshot_path}'],
        media_url=[f'file://{http://127.0.0.1:5000/}'],

        to=f'whatsapp:{+919555711143}'
    )
    print("Message sent successfully!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-screenshot', methods=['POST'])
def send_screenshot():
    to_number = request.form['to_number']
    screenshot_path = 'screenshot.png'
    
    # Delete previous screenshot if exists
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
    
    # Take screenshot
    take_screenshot(request.url_root, screenshot_path)
    
    # Send screenshot via WhatsApp
    send_whatsapp_message(screenshot_path, to_number)
    
    return 'Screenshot sent to WhatsApp'

if __name__ == '__main__':
    app.run(debug=True)
