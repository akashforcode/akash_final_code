from flask import Flask, render_template, request, jsonify, Response
from flask import Flask, render_template
from kite_trade import *
#import threading
import time


#########EXIT SERVER



app = Flask(__name__)


#xx=input("enter strike")


##########KITE login####################
#################VARIABLE DEFINE#############
call_strike="aa"
put_strike="bb"


xx=""


lb=[47100, 47200, 47300, 47400, 47500]

#cspb=int(input("input strike price for current banknifty:::"))
cspb=46000
lb=[cspb-200,cspb-100,cspb,cspb+100,cspb+200]


f = open("token.txt", "r")
enctoken=f.read()
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.margins())
print(kite.ltp("NSE:BANKNIFTY24MAR46000PE"))
################all option strike price###
from datetime import datetime, timedelta

def next_wednesday():
    today = datetime.today()
    days_ahead = (2 - today.weekday()) % 7  # Calculate days until next Wednesday (Wednesday is represented by 2)
    next_wednesday_date = today + timedelta(days=days_ahead)
    return next_wednesday_date.strftime("%Y-%m-%d")

print("Date of upcoming Wednesday:", next_wednesday())



yr=int(next_wednesday()[2:4])
mm=int(next_wednesday()[5:7])
dd=(next_wednesday()[8:10])
print(yr,mm,dd)

yr=str(yr)
mm=str(mm)
dd=str(dd)

datew=yr+mm+dd
bankoptionputpe="BANKNIFTY"+datew+"46800"+"PE"
print(bankoptionputpe)

#lb=[47100, 47200, 47300, 47400, 47500]

lbsp=[]
lbsc=[]
for i in range(5):
    bankoptionputpe="BANKNIFTY"+datew+str(lb[i])+"PE"
    bankoptionputce="BANKNIFTY"+datew+str(lb[i])+"CE"
    lbsp.append(bankoptionputpe)
    lbsc.append(bankoptionputce)
print(bankoptionputpe)
print(bankoptionputce)

print(lbsp)
print(lbsc)

callstr="BANKNIFTY"+datew+str(xx)+"CE"
putstr="BANKNIFTY"+datew+str(xx)+"PE"

print(callstr)
print(putstr)


#options = ['Option 1', 'Option 2', 'Option 3']
options =lbsp
options =lbsc


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



##############FUCNTION_FOR_MARKET#############



#
#import time
#def buy_option(n):
#    for i in range(1):
#        #print(e2.get())
#        order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                              exchange=kite.EXCHANGE_NFO,
#                              tradingsymbol=callstr,
#                              #tradingsymbol="BANKNIFTY24MAR46600PE",
#                              transaction_type=kite.TRANSACTION_TYPE_BUY,
#                              quantity=n,
#                              #quantity=15,
#                              product=kite.PRODUCT_MIS,
#                              order_type=kite.ORDER_TYPE_MARKET,
#                              price=None,
#                              validity=None,
#                              disclosed_quantity=None,
#                              trigger_price=None,
#                              squareoff=None,
#                              stoploss=None,
#                              trailing_stoploss=None,
#                              tag="TradeViaPython")
#        print(order)
#
#
#def sell_option(n):
#    for i in range(1):
#        #print(str(e2.get()))
#        order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                              exchange=kite.EXCHANGE_NFO,
#                              tradingsymbol=callstr,
#                              #tradingsymbol="BANKNIFTY24MAR46600PE",
#                              transaction_type=kite.TRANSACTION_TYPE_SELL,
#                              quantity=n,
#                              #quantity=15,
#                              product=kite.PRODUCT_MIS,
#                              order_type=kite.ORDER_TYPE_MARKET,
#                              price=None,
#                              validity=None,
#                              disclosed_quantity=None,
#                              trigger_price=None,
#                              squareoff=None,
#                              stoploss=None,
#                              trailing_stoploss=None,
#                              tag="TradeViaPython")
#        print(order)
#
#        
#
#def buy_option_put(n):
#    for i in range(1):
#        #print(e2.get())
#        order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                              exchange=kite.EXCHANGE_NFO,
#                              tradingsymbol=putstr,
#                              #tradingsymbol="BANKNIFTY24MAR46600PE",
#                              transaction_type=kite.TRANSACTION_TYPE_BUY,
#                              quantity=n,
#                              #quantity=15,
#                              product=kite.PRODUCT_MIS,
#                              order_type=kite.ORDER_TYPE_MARKET,
#                              price=None,
#                              validity=None,
#                              disclosed_quantity=None,
#                              trigger_price=None,
#                              squareoff=None,
#                              stoploss=None,
#                              trailing_stoploss=None,
#                              tag="TradeViaPython")
#        print(order)
#
#
#
#
#def sell_option_put(n):
#    for i in range(1):
#        #print(str(e2.get()))
#        order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                              exchange=kite.EXCHANGE_NFO,
#                              tradingsymbol=putstr,
#                              #tradingsymbol="BANKNIFTY24MAR46600PE",
#                              transaction_type=kite.TRANSACTION_TYPE_SELL,
#                              quantity=n,
#                              #quantity=15,
#                              product=kite.PRODUCT_MIS,
#                              order_type=kite.ORDER_TYPE_MARKET,
#                              price=None,
#                              validity=None,
#                              disclosed_quantity=None,
#                              trigger_price=None,
#                              squareoff=None,
#                              stoploss=None,
#                              trailing_stoploss=None,
#                              tag="TradeViaPython")
#        print(order)
#


##############FUCNTION_FOR_MARKET#############



###########LIVE
import pandas as pd


def generate_data():
    while True:
        #print(kite.ltp("NFO:BANKNIFTY24MAR46000PE"))
        new1 = pd.DataFrame.from_dict((kite.ltp("NSE:NIFTY BANK")))#print(new1)
        print(new1.iat[1, 0])
        nbr=(new1.iat[1, 0])
        #nbr=int((round((new1.iat[1, 0])/100))*100)
        #print(nbr)
        #nbrsl=[nbr-200,nbr-100,nbr,nbr+100,nbr+200]
        #print(nbrsl)
        nbr=str(nbr)
        time.sleep(1)
        yield f"data: {nbr}\n\n"

##def generate_data():
#    count = 0
#    while True:
#        yield f"data: {count}\n\n"
#        count += 1
#        time.sleep(1)

@app.route('/data')
def data():
    return Response(generate_data(), mimetype='text/event-stream')
 

###########LIVE







def function1():
    buy_option(15)
    # This is the first function you want to execute
    return "1 LOT QUANTITY BUY OPTION EXECUTED!"

def function2():
    sell_option(15)   
    # This is the second function you want to execute
    return "1 LOT QUANTITY SELL OPTION EXECUTED!"

def function3():
    buy_option(30)
    # This is the first function you want to execute
    return "2 LOT QUANTITY  BUY OPTION EXECUTED!"

def function4():
    sell_option(30)   
    # This is the second function you want to execute
    return "2 LOT QUANTITY SELL OPTION EXECUTED!"

def function5():
    buy_option(60)
    # This is the first function you want to execute
    return "4 LOT QUANTITY BUY OPTION EXECUTED!"

def function6():
    sell_option(60)   
    # This is the second function you want to execute
    return "4 LOT QUANTITY SELL OPTION EXECUTED!"

def function7():
    buy_option(90)
    # This is the first function you want to execute
    return "6 LOT QUANTITY  BUY OPTION EXECUTED!"

def function8():
    sell_option(90)   
    # This is the second function you want to execute
    return "6 LOT QUANTITY SELL OPTION EXECUTED!"



def function9():
    buy_option_put(15)
    # This is the first function you want to execute
    return "1 LOT QUANTITY BUY OPTION EXECUTED!"

def function10():
    sell_option_put(15)   
    # This is the second function you want to execute
    return "1 LOT QUANTITY SELL OPTION EXECUTED!"

def function11():
    buy_option_put(30)
    # This is the first function you want to execute
    return "2 LOT QUANTITY  BUY OPTION EXECUTED!"

def function12():
    sell_option_put(30)   
    # This is the second function you want to execute
    return "2 LOT QUANTITY SELL OPTION EXECUTED!"

def function13():
    buy_option_put(60)
    # This is the first function you want to execute
    return "4 LOT QUANTITY BUY OPTION EXECUTED!"

def function14():
    sell_option_put(60)   
    # This is the second function you want to execute
    return "4 LOT QUANTITY SELL OPTION EXECUTED!"

def function15():
    buy_option_put(90)
    # This is the first function you want to execute
    return "6 LOT QUANTITY  BUY OPTION EXECUTED!"

def function16():
    sell_option_put(90)   
    # This is the second function you want to execute
    return "6 LOT QUANTITY SELL OPTION EXECUTED!"





@app.route('/execute_function1', methods=['POST'])
def execute_function1():
    if request.method == 'POST':
        result = function1()
        return jsonify({'result': result})

@app.route('/execute_function2', methods=['POST'])
def execute_function2():
    if request.method == 'POST':
        result = function2()
        return jsonify({'result': result})

@app.route('/execute_function3', methods=['POST'])
def execute_function3():
    if request.method == 'POST':
        result = function3()
        return jsonify({'result': result})

@app.route('/execute_function4', methods=['POST'])
def execute_function4():
    if request.method == 'POST':
        result = function4()
        return jsonify({'result': result})

@app.route('/execute_function5', methods=['POST'])
def execute_function5():
    if request.method == 'POST':
        result = function5()
        return jsonify({'result': result})

@app.route('/execute_function6', methods=['POST'])
def execute_function6():
    if request.method == 'POST':
        result = function6()
        return jsonify({'result': result})

@app.route('/execute_function7', methods=['POST'])
def execute_function7():
    if request.method == 'POST':
        result = function7()
        return jsonify({'result': result})

@app.route('/execute_function8', methods=['POST'])
def execute_function8():
    if request.method == 'POST':
        result = function8()
        return jsonify({'result': result})
    




@app.route('/execute_function9', methods=['POST'])
def execute_function9():
    if request.method == 'POST':
        result = function9()
        return jsonify({'result': result})

@app.route('/execute_function10', methods=['POST'])
def execute_function10():
    if request.method == 'POST':
        result = function10()
        return jsonify({'result': result})

@app.route('/execute_function11', methods=['POST'])
def execute_function11():
    if request.method == 'POST':
        result = function11()
        return jsonify({'result': result})

@app.route('/execute_function12', methods=['POST'])
def execute_function12():
    if request.method == 'POST':
        result = function12()
        return jsonify({'result': result})

@app.route('/execute_function13', methods=['POST'])
def execute_function13():
    if request.method == 'POST':
        result = function13()
        return jsonify({'result': result})

@app.route('/execute_function14', methods=['POST'])
def execute_function14():
    if request.method == 'POST':
        result = function14()
        return jsonify({'result': result})

@app.route('/execute_function15', methods=['POST'])
def execute_function15():
    if request.method == 'POST':
        result = function15()
        return jsonify({'result': result})

@app.route('/execute_function16', methods=['POST'])
def execute_function16():
    if request.method == 'POST':
        result = function16()
        return jsonify({'result': result})
    

############################
    



#def print_continuously():
#    global global_input
#    while True:
#        if global_input:
#            print("Input from HTML:", global_input)
#            time.sleep(1)  # Adjust sleep time as needed
#
#
## Start the printing thread
#print_thread = threading.Thread(target=print_continuously)
#print_thread.daemon = True
#print_thread.start()
#


@app.route('/', methods=['GET', 'POST'])
def index():
    selected_option = None

    if request.method == 'POST':
        selected_option = request.form['option']

    return render_template('index.html', options=options, selected_option=selected_option)

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        selected_option = request.form['selected_option']
        action = request.form['action']
        result = f"Processing with {action} for {selected_option}"
        return jsonify({'result': result})


########TAKE DATA OF DROPDOWN OPTION#######
@app.route('/process_dropdown', methods=['POST'])
def process_dropdown():
    selected_option = request.form["option"]
    # Do something with the selected option, for example:
    if selected_option == lbsp[0]:
        result =print(lbsp[0])
    elif selected_option ==lbsp[1]:
        result = lbsp[1]
    elif selected_option == lbsp[2]:
        result = lbsp[2]
    elif selected_option == lbsp[3]:
        result = lbsp[3]
    elif selected_option == lbsp[4]:
        result = lbsp[4]
    return result   

###########################################


strikevalue=""

def update():
    global global_input 
    global strikevalue
    global_input = strikevalue
    print(global_input)

#def update():
#    global xx 
#    global strikevalue
#    xx = strikevalue
#    print(xx)


@app.route('/process_strikevalue', methods=['POST'])
def process_strikevalue():
    global strikevalue  # Declare strikevalue as global
    strikevalue = request.form['strikevalue']
    #print("Input strikevalue:", strikevalue)  # Print input variable to terminal

    # Call the update function after the value is assigned
    update()

    #print(strikevalue)

    # Do something with the variable, for example:
    result = f"The entered strikevalue is {strikevalue}"
    
    return result  






if __name__ == '__main__':
    app.run(debug=True)
