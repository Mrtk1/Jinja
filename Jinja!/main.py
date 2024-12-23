# Import / İçe Aktarma
from flask import Flask, render_template

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

def energy_consumption_calculate(size, lights, device):
    # Enerji tüketimini hesaplamak için yeni bir fonksiyon
    energy_consumption = result_calculate(size, lights, device) / 1000  # kW cinsinden
    return energy_consumption

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')

# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    energy_consumption = energy_consumption_calculate(int(size), int(lights), int(device))
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    ),
                            energy_consumption=energy_consumption
                        )
app.run(debug=True)