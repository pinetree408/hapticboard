# For Arduino
import serial
import time

ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

# For Flask
from flask import Flask
from flask import render_template
from flask import redirect, url_for, request

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/connect", methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        json_data = request.get_json()
        input_value = json_data['input']
        if input_value == '1':
            print 'serial on (P)'
            ser.write('1')
        elif input_value == '2':
            print 'serial on (N)'
            ser.write('2')
        elif input_value == '9':
            print 'serial on (C)'
            ser.write('9')
        elif int(input_value) > 999:
            realVol = int(input_value) - 1000
            print realVol
	    if realVol < 10:
                ser.write('3')
	    elif realVol < 20:
                ser.write('4')
	    elif realVol < 30:
                ser.write('5')
	    elif realVol < 40:
                ser.write('6')
	    elif realVol < 50:
                ser.write('7')
            else:
                ser.write('8')
        else:
            print 'serial off'
            ser.write('0')
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
