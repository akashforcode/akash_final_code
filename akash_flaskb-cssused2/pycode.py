from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, jsonify, Response
from flask import Flask, render_template
from kite_trade import *
#import threading
import time
from datetime import datetime, timedelta


app = Flask(__name__)

callstr=""
putstr=""

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


import pandas as pd
# Define a global variable to store input_data
input_data_global = None
callstr =None
putstr=None
def generate_data():
    global input_data_global  # Access the global variable
    global callstr
    global putstr
    while True:
        if input_data_global is not None:
            print("Input Data:", input_data_global)
            print("Input Data:", 'NFO:'+callstr)
            print("Input Data:", 'NFO:'+putstr)
        new1 = pd.DataFrame.from_dict((kite.ltp("NSE:NIFTY BANK")))
        print(new1.iat[1, 0])
        nbr = new1.iat[1, 0]
        new2 = pd.DataFrame.from_dict((kite.ltp('NFO:'+callstr)))
        new3 = pd.DataFrame.from_dict((kite.ltp('NFO:'+putstr)))
        strc = new2.iat[1, 0]
        strp = new3.iat[1, 0]
        nbr = str(nbr)
        strc = str(strc)
        strp = str(strp)
        time.sleep(1)
        yield f"data: {'BANK::'+nbr+'-------'+'CALL STRIKE::'+strc+'-------'+'PUT STRIKE::'+strp}\n\n"





@app.route('/data')
def data():
    return Response(generate_data(), mimetype='text/event-stream')
 



############FUNCTIONS_for_AMO###############

import time
def buy_option(n,op):
    for i in range(1):
        #print(e2.get())
        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=op,
                              #tradingsymbol="BANKNIFTY2441048000CE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_MARKET,
                              price=None,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option(n, op):
    for i in range(1):
        #print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=op,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_MARKET,
                              price=None,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)

        

def buy_option_put(n, op):
    for i in range(1):
        #print(e2.get())
        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=op,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_BUY,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_MARKET,
                              price=None,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)




def sell_option_put(n, op):
    for i in range(1):
        #print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_REGULAR,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=op,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_MARKET,
                              price=None,
                              validity=None,
                              disclosed_quantity=None,
                              trigger_price=None,
                              squareoff=None,
                              stoploss=None,
                              trailing_stoploss=None,
                              tag="TradeViaPython")
        print(order)


def sell_option_dumy(n, op):
    for i in range(1):
        #print(str(e2.get()))
        order = kite.place_order(variety=kite.VARIETY_AMO,
                              exchange=kite.EXCHANGE_NFO,
                              tradingsymbol=op,
                              #tradingsymbol="BANKNIFTY24MAR46600PE",
                              transaction_type=kite.TRANSACTION_TYPE_SELL,
                              quantity=n,
                              #quantity=15,
                              product=kite.PRODUCT_MIS,
                              order_type=kite.ORDER_TYPE_LIMIT,
                              price=10,
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
    global input_data_global  # Access the global variable
    global callstr
    global putstr
    # Get the input data and function name from the AJAX request
    data = request.json
    input_data = data['input_data']
    func_name = data['func_name']
    input_data_global = input_data  # Store input_data in the global variable
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
    print("Input data:", input_data)
    print("Input data:", callstr)
    print("Input data:", putstr)
    # Execute different Python functions based on the button pressed
    if func_name == 'function1':
        result = function1(callstr)
    elif func_name == 'function2':
        result = function2(callstr)
    elif func_name == 'function3':
        result = function3(callstr)
    elif func_name == 'function4':
        result = function4(callstr)
    elif func_name == 'function5':
        result = function5(callstr)
    elif func_name == 'function6':
        result = function6(callstr)
    elif func_name == 'function7':
        result = function7(callstr)
    elif func_name == 'function8':
        result = function8(callstr)
    elif func_name == 'function9':
        result = function9(callstr)
    elif func_name == 'function10':
        result = function10(callstr)
    elif func_name == 'function11':
        result = function11(callstr)
    elif func_name == 'function12':
        result = function12(callstr)     
        #####################

    elif func_name == 'function13':
        result = function13(putstr)
    elif func_name == 'function14':
        result = function14(putstr)
    elif func_name == 'function15':
        result = function15(putstr)
    elif func_name == 'function16':
        result = function16(putstr)
    elif func_name == 'function17':
        result = function17(putstr)
    elif func_name == 'function18':
        result = function18(putstr)
    elif func_name == 'function19':
        result = function19(callstr)
    elif func_name == 'function20':
        result = function20(callstr)
    elif func_name == 'function21':
        result = function21(putstr)
    elif func_name == 'function22':
        result = function22(putstr)
    elif func_name == 'function23':
        result = function23(putstr)
    elif func_name == 'function24':
        result = function24(putstr)
    elif func_name == 'function25':
        result = function25(putstr)
    else:
        result = "Invalid function name"
    # Return the result as JSON
    return jsonify({'result': result})
# Define your Python functions here
def function1(callstr):
    # Implement your function logic here
    buy_option(15,callstr)
    return "Function 1 executed to buy a lot of 15 with input: " + callstr
def function2(callstr):
    # Implement your function logic here
    sell_option(15,callstr)
    return "Function 2 executed to sell a lot of 15 with input: " + callstr
# Define your Python functions here
def function3(callstr):
    # Implement your function logic here
    buy_option(30,callstr)
    return "Function 3 executed to buy a lot of 30 with input: " + callstr
def function4(callstr):
    # Implement your function logic here
    sell_option(30,callstr)
    return "Function 4 executed to sell a lot of 30 with input: " + callstr
# Define your Python functions here
def function5(callstr):
    # Implement your function logic here
    buy_option(60,callstr)
    return "Function 5 executed to buy a lot of 60 with input: " + callstr
def function6(callstr):
    # Implement your function logic here
    sell_option(60,callstr)
    return "Function 6 executed to sell a lot of 60 with input: " + callstr
# Define your Python functions here
def function7(callstr):
    # Implement your function logic here
    buy_option(90,callstr)
    return "Function 7 executed to buy a lot of 90 with input: " + callstr
def function8(callstr):
    # Implement your function logic here
    sell_option(90,callstr)
    return "Function 8 executed to sell a lot of 90 with input: " + callstr
def function9(callstr):
    # Implement your function logic here
    buy_option(150,callstr)
    return "Function 9 executed to buy a lot of 150 with input: " + callstr
def function10(callstr):
    # Implement your function logic here
    sell_option(150,callstr)
    return "Function 10 executed to sell a lot of 150 with input: " + callstr
def function11(callstr):
    # Implement your function logic here
    buy_option(300,callstr)
    return "Function 11 executed to buy a lot of 300 with input: " + callstr
def function12(callstr):
    # Implement your function logic here
    sell_option(300,callstr)
    return "Function 12 executed to sell a lot of 300 with input: " + callstr





# Define your Python functions here
def function13(putstr):
    # Implement your function logic here
    buy_option_put(15,putstr)
    return "Function 13 executed to buy a lot of 15 with input: " + putstr
def function14(putstr):
    # Implement your function logic here
    sell_option_put(15,putstr)
    return "Function 14 executed to sell a lot of 15 with input: " + putstr
# Define your Python functions here
def function15(putstr):
    # Implement your function logic here
    buy_option_put(30,putstr)
    return "Function 15 executed to buy a lot of 30 with input: " + putstr
def function16(putstr):
    # Implement your function logic here
    sell_option_put(30,putstr)
    return "Function 16 executed to sell a lot of 30 with input: " + putstr
# Define your Python functions here
def function17(putstr):
    # Implement your function logic here
    buy_option_put(60,putstr)
    return "Function 17 executed to buy a lot of 60 with input: " + putstr
def function18(putstr):
    # Implement your function logic here
    sell_option_put(60,putstr)
    return "Function 18 executed to sell a lot of 60 with input: " + putstr
# Define your Python functions here
def function19(putstr):
    # Implement your function logic here
    buy_option_put(90,putstr)
    return "Function 19 executed to buy a lot of 90 with input: " + putstr
def function20(putstr):
    # Implement your function logic here
    sell_option_put(90,putstr)
    return "Function 20 executed to sell a lot of 90 with input: " + putstr
# Define your Python functions here
def function21(putstr):
    # Implement your function logic here
    buy_option_put(150,putstr)
    return "Function 21 executed to buy a lot of 150 with input: " + putstr
def function22(putstr):
    # Implement your function logic here
    sell_option_put(150,putstr)
    return "Function 22 executed to sell a lot of 150 with input: " + putstr
# Define your Python functions here
def function23(putstr):
    # Implement your function logic here
    buy_option_put(300,putstr)
    return "Function 23 executed to buy a lot of 300 with input: " + putstr
def function24(putstr):
    # Implement your function logic here
    sell_option_put(300,putstr)
    return "Function 24 executed to sell a lot of 300 with input: " + putstr
def function25(putstr):
    # Implement your function logic here
    sell_option_put(0,putstr)
    return "Function 25 executed for dumy to submit input data: " + putstr

# Define put other functions similarly...
if __name__ == '__main__':
    app.run(debug=True)
