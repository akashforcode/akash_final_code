from flask import Flask, render_template, request, jsonify
import random
from kite_trade import *
import pandas as pd




app = Flask(__name__)


f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

print(kite.margins())
print(kite.ltp("MCX:CRUDEOIL24APR6800PE"))

print(type(random.uniform(100, 200)))
#print(type(pd.DataFrame.from_dict(kite.ltp("MCX:CRUDEOIL24APR6800PE"))).iat[1, 0])



# Function to fetch live market data (Replace with actual API call)
def fetch_live_data():
    return {
        #live_price = pd.DataFrame.from_dict(kite.ltp("MCX:CRUDEOIL24APR6800PE"))
        'price':pd.DataFrame.from_dict(kite.ltp("MCX:CRUDEOIL24APR6800PE")).iat[1,0]
        #'price': random.uniform(100, 200)  # Random price between 100 and 200 for demonstration
        #'price': live_buy 
        
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_price', methods=['POST'])
def fetch_price():
    action = request.form['action']
    price = fetch_live_data()['price']
    return jsonify({'action': action, 'price': price})

if __name__ == '__main__':
    app.run(debug=True)