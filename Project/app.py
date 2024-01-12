from flask import Flask, request, render_template
import csv
import time
from CustomPymata4 import *
import datetime


board = CustomPymata4(baud_rate = 57600, com_port = "COM4")

BUZZER = [3] 

app = Flask(__name__)
#============================================Login page============================================#

@app.route('/', methods =["GET", "POST"])

def gfg():

    cookCode = "12345"
    cashierCode = "112233"

    if request.method == "POST":
        cook_code = request.form.get("ckCode") 
        cashier_code = request.form.get("cshCode") # get the input from webpage

#==================================Csv headings==================================#
        if cookCode == cook_code: # if the input is matching the code open the cook page         
            fields = ['dateTime', 'pizzaNumber', 'pizzaStatus']

            with open('data.csv', 'r+', newline="") as f: #print the headers in the csv file
                write = csv.writer(f)
                write.writerow(fields)
                f.close()
            return render_template("cook.html") 

        elif cashierCode == cashier_code: # if the input is matching the code open the cashier page        
            headers = ['PizzaQuantity', 'PizzaName', 'PizzaQuantity', 'PizzaName', 'PizzaQuantity', 'PizzaName']

            with open('orders.csv', 'r+', newline="") as f: # print headers in the csv file
                write = csv.writer(f)
                write.writerow(headers)
                f.close()
            return render_template("cashier.html")

        elif cookCode != cook_code or cashierCode != cashier_code: # if the codes are wrong stay in the same
            return render_template("index.html") 
        
    return render_template("index.html")

#============================================Render menu page============================================#

@app.route('/menu.html', methods =["GET", "POST"])
    
def menu():
    if request.method == "POST":
        orders = []
        
        #===Pizza Margharita===#
        pMargharita = request.form.get("pMargharita")
        qMargharita  =int(request.form.get("qMargharita"))
        nMargharita = request.form.get("nMargharita")

        if qMargharita > 0: # put the order in the orders list
            orders.append(qMargharita)
            orders.append(nMargharita)
            
        #===Pizza Funghi===#
        priceF = request.form.get("priceF")
        quantityF =int(request.form.get("quantityF"))
        name = request.form.get("pizzaFunghi")

        if quantityF > 0: # put the order in the orders list
            orders.append(quantityF)
            orders.append(name)

        #===Pizza Meatlover===#
        pMeatlover = request.form.get("pMeatlover")
        qMeatlover =int(request.form.get("qMeatlover"))
        Meatlover = request.form.get("pizzaMeatlover")

        if qMeatlover > 0: # put the order in the orders list
            orders.append(qMeatlover)
            orders.append(Meatlover)

        #===Pizza SHOARMA===#
        pShoarma = request.form.get("pShoarma")
        qShoarma =int(request.form.get("qShoarma"))
        Shoarma = request.form.get("pizzaShoarma")

        if qShoarma > 0: # put the order in the orders list
            orders.append(qShoarma)
            orders.append(Shoarma)

        #===Pizza VEGGI===#
        pVeggi = request.form.get("pVeggi")
        qVeggi =int(request.form.get("qVeggi"))
        Veggi = request.form.get("pizzaVeggi")

        if qVeggi > 0: # put the order in the orders list
            orders.append(qVeggi)
            orders.append(Veggi)
            
        with open('orders.csv', 'a', newline="") as f: #print order information in the csv file
            write = csv.writer(f)
            write.writerow(orders)
            f.close()

        return render_template("cashier.html")
    return render_template("menu.html")
    
#============================================Customer page============================================#
@app.route('/customer.html')

def open_customer_page():  
    with open('data.csv', mode ='r')as file: #reading the data from csv file and storing them in variables
        csvFile = csv.DictReader(file)
        line_count = 0

        for line in csvFile:

            if line_count == 0:
                print(", ".join(line))

            else:
                pizzaNumber = line['pizzaNumber']
                pizzaStatus = line['pizzaStatus'] 
                

            line_count += 1
    return render_template("customer.html", pizzaNumber=pizzaNumber, pizzaStatus=pizzaStatus)

#============================================Cook printing============================================#
@app.route('/cook.html', methods =["GET", "POST"])

def buttons():

    status = request.form.get("inlineRadioOptions")
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")


    with open('orders.csv', mode ='r')as file: #print the latest order
        recent_order = file.readlines()[-1]
#==================================Csv Writing==================================#
    
    with open('data.csv', 'a', newline="") as f: #print order status in the csv file
        write = csv.writer(f)
        write.writerow([date_time,"#1",status])
        f.close()

        if status=="waiting":
            board.digital_pin_write(7,1) #turn on the yellow LED
            board.digital_pin_write(6,0) #turn off the blue LED
            board.digital_pin_write(5,0) #turn off the green LED
            board.digital_pin_write(4,0) #turn off the red LED
        elif status=="inProgress":
            board.digital_pin_write(6,1) #turn on the blue LED
            board.digital_pin_write(7,0) #turn off the yellow LED
            board.digital_pin_write(5,0) #turn off the green LED
            board.digital_pin_write(4,0) #turn off the red LED
        elif status=="inOven":
            board.digital_pin_write(4,1) #turn on the red LED
            board.digital_pin_write(7,0) #turn off the yellow LED
            board.digital_pin_write(6,0) #turn off the blue LED
            board.digital_pin_write(5,0) #turn off the green LED
            time.sleep(5)
            state = 0

            if state == 0: #turn the green LED on and off 3 times when the pizza is "Done"
                time.sleep(0.2)
                board.digital_write(5, 1)
                time.sleep(0.5)
                board.digital_write(5, 0)
                time.sleep(0.2)
                board.digital_write(5, 1)
                time.sleep(0.5)
                board.digital_write(5, 0) 
                time.sleep(0.2)
                board.digital_write(5, 1)
                time.sleep(0.5)
                board.digital_write(5, 0)  
                state = 1
                if state == 1: #if the status is "Done" turn on the buzzer
                    for PIN in BUZZER:
                        board.digital_pin_write(PIN, 1)
                        time.sleep(3)
                        board.digital_pin_write(PIN, 0)
                        break
            
        elif status == "Done":
            state = 0

            if state == 0: #turn the green LED on and off 3 times when the pizza is "Done"
                time.sleep(0.2)
                board.digital_write(5, 1)
                time.sleep(0.5)
                board.digital_write(5, 0)
                time.sleep(0.2)
                board.digital_write(5, 1)
                time.sleep(0.5)
                board.digital_write(5, 0) 
                time.sleep(0.2)
                board.digital_write(5, 1)
                time.sleep(0.5)
                board.digital_write(5, 0)  
                state = 1
                if state == 1: #if the status is "Done" turn on the buzzer
                    for PIN in BUZZER:
                        board.digital_pin_write(PIN, 1)
                        time.sleep(3)
                        board.digital_pin_write(PIN, 0)
                        break
                
        else: #turn all LEDs off

            board.digital_pin_write(7,0)
            board.digital_pin_write(6,0)
            board.digital_pin_write(5,0)
            board.digital_pin_write(4,0)
            
                   
    return render_template("cook.html",recent_order=recent_order )
    

    

if __name__=='__main__':
    app.run()
