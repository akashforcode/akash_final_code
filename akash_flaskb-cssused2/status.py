from flask import Flask, render_template
from kite_trade import *

app = Flask(__name__)

##########KITE login####################
#################VARIABLE DEFINE#############
call_strike="aa"
put_strike="bb"

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

# Function to generate options for the combo boxes
def generate_combo_options():
    #combo1_options = ["Option 1", "Option 2", "Option 3"]
    combo1_options = lbsc
    #combo2_options = ["Choice A", "Choice B", "Choice C"]
    combo2_options =lbsp
    return combo1_options, combo2_options

@app.route('/')
def index():
    combo1_options, combo2_options = generate_combo_options()
    return render_template('index.html', combo1_options=combo1_options, combo2_options=combo2_options)

if __name__ == '__main__':
    app.run(debug=True)
