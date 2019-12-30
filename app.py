from flask import Flask, render_template, request
from Data.data import getData
from Data.totaldevice import totalDeviceChar

app = Flask(__name__)#Flask 


@app.route('/', methods=['POST', 'GET'])
def home():
    total = totalDeviceChar()#Total availables device
    if request.method == 'POST' and len(request.form['search'].replace(' ', '')) > 0:
        device = request.form['search']
        phones = getData(device)#List that contains dicts with device with features
        return render_template('index.html', phones=phones, totalDevices=total)
    return render_template('index.html', firstSearch=True, totalDevices=total)


if __name__ == "__main__":
    app.run(debug=True)