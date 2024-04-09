from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, jsonify, Response
from flask import Flask, render_template
from kite_trade import *
#import threading
import time
from datetime import datetime, timedelta
callstr=""
putstr=""
app = Flask(__name__)

# Define a route to render the HTML form
f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)
print(kite.ltp("NSE:BANKNIFTY24MAR48000PE"))
# Basic calls
print(kite.margins())
@app.route('/')
def index():
    return render_template('index.html')

############FUNCTIONS_for_AMO###############

import time
def buy_option(n):
    for i in range(1):
        #print(e2.get())
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=callstr,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=100,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option(n):
    for i in range(1):
        #print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=callstr,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=100,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)

        

def buy_option_put(n):
    for i in range(1):
        #print(e2.get())
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=putstr,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=100,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)




def sell_option_put(n):
    for i in range(1):
        #print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=putstr,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=100,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


#############FUNCTIONS_for_AMO###############

def next_wednesday():
    today = datetime.today()
    days_ahead = (2 - today.weekday()) % 7  # Calculate days until next Wednesday (Wednesday is represented by 2)
    next_wednesday_date = today + timedelta(days=days_ahead)
    return next_wednesday_date.strftime("%Y-%m-%d")

print("Date of upcoming Wednesday:", next_wednesday())

# Define a route to handle function execution
@app.route('/execute_function', methods=['POST'])
def execute_function():
    # Get the input data and function name from the AJAX request
    data = request.json
    input_data = data['input_data']
    func_name = data['func_name']

    yr=int(next_wednesday()[2:4])
    mm=int(next_wednesday()[5:7])
    dd=(next_wednesday()[8:10])
    print(yr,mm,dd)

    yr=str(yr)
    mm=str(mm)
    dd=str(dd)

    datew=yr+mm+dd
    callstr="BANKNIFTY"+datew+str(input_data)+"CE"
    putstr="BANKNIFTY"+datew+str(input_data)+"PE"
    # Execute different Python functions based on the button pressed
    if func_name == 'function1':
        result = function1(callstr)
    elif func_name == 'function2':
        result = function2(putstr)
    elif func_name == 'function3':
        result = function3(input_data)
    elif func_name == 'function4':
        result = function4(input_data)
    elif func_name == 'function5':
        result = function5(input_data)
    elif func_name == 'function6':
        result = function6(input_data)
    elif func_name == 'function7':
        result = function7(input_data)
    elif func_name == 'function8':
        result = function8(input_data)
    else:
        result = "Invalid function name"

    # Return the result as JSON
    return jsonify({'result': result})

# Define your Python functions here
def function1(input_data):
    # Implement your function logic here

    return "Function 1 executed with input: " + input_data

def function2(input_data):
    # Implement your function logic here
    return "Function 2 executed with input: " + input_data

# Define your Python functions here
def function3(input_data):
    # Implement your function logic here
    return "Function 3 executed with input: " + input_data

def function4(input_data):
    # Implement your function logic here
    return "Function 4 executed with input: " + input_data

# Define your Python functions here
def function5(input_data):
    # Implement your function logic here
    return "Function 5 executed with input: " + input_data

def function6(input_data):
    # Implement your function logic here
    return "Function 6 executed with input: " + input_data

# Define your Python functions here
def function7(input_data):
    # Implement your function logic here
    return "Function 7 executed with input: " + input_data

def function8(input_data):
    # Implement your function logic here
    return "Function 8 executed with input: " + input_data

# Define other functions similarly...

if __name__ == '__main__':
    app.run(debug=True)
