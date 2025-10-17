from flask import Flask, render_template, request, jsonify, send_file
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime
import os
import random

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
CSV_FILE = "weather_data.csv"


# ---------------- Fetch Current Weather ----------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


# ---------------- Store Weather Data ----------------
def save_weather_data(city, temp, humidity):
    now = datetime.datetime.now()
    new_data = pd.DataFrame({
        'date': [now.strftime('%Y-%m-%d')],
        'city': [city],
        'temp': [temp],
        'humidity': [humidity]
    })

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, new_data], ignore_index=True)
        df = df.groupby('city').tail(30)  # Keep last 30 records per city
    else:
        df = new_data

    df.to_csv(CSV_FILE, index=False)


# ---------------- Forecast (Linear Regression) ----------------
def forecast_weather(city, current_temp=None, current_humidity=None):
    if not os.path.exists(CSV_FILE):
        if current_temp is not None and current_humidity is not None:
            today = datetime.datetime.now()
            forecast_dates = [(today + datetime.timedelta(days=i+1)).strftime('%Y-%m-%d') for i in range(5)]
            return {
                'forecast': [(forecast_dates[i], round(current_temp,1), round(current_humidity)) for i in range(5)],
                'temp_range': [max(0, current_temp-5), current_temp+5],
                'hum_range': [max(0, current_humidity-5), min(100, current_humidity+5)]
            }
        return {'forecast': [], 'temp_range':[0,50], 'hum_range':[0,100]}

    df = pd.read_csv(CSV_FILE)
    df = df[df['city'] == city]

    if df.empty:
        return forecast_weather(city, current_temp, current_humidity)

    df['time_index'] = range(len(df))
    model_temp = LinearRegression()
    model_humidity = LinearRegression()

    model_temp.fit(df[['time_index']], df['temp'])
    model_humidity.fit(df[['time_index']], df['humidity'])

    future_index = [[i] for i in range(len(df), len(df)+5)]

    # Slight jitter for clarity
    future_temp = [round(t + random.uniform(-0.3,0.3),1) for t in model_temp.predict(future_index)]
    future_humidity = [round(h + random.uniform(-1,1),0) for h in model_humidity.predict(future_index)]

    # Optional: tiny offset for plotting to reduce overlap (not affecting tooltips)
    future_temp_plot = [t + 0.2 for t in future_temp]
    future_humidity_plot = [h - 0.2 for h in future_humidity]

    forecast_dates = [(datetime.datetime.now() + datetime.timedelta(days=i+1)).strftime('%Y-%m-%d') for i in range(5)]
    forecast_list = list(zip(forecast_dates, future_temp_plot, future_humidity_plot))

    # Large axis with no negative values
    temp_min = max(0, min(future_temp + df['temp'].tolist()) - 10)
    temp_max = max(future_temp + df['temp'].tolist()) + 10
    hum_min = max(0, min(future_humidity + df['humidity'].tolist()) - 10)
    hum_max = min(100, max(future_humidity + df['humidity'].tolist()) + 10)

    return {'forecast': forecast_list, 'temp_range':[temp_min, temp_max], 'hum_range':[hum_min, hum_max]}


# ---------------- Routes ----------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather_data():
    city = request.form['city']

    if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
        return jsonify({'error': "API key not set. Please add a valid OpenWeatherMap API key."})

    data = get_weather(city)
    cod = str(data.get('cod'))
    if cod != "200":
        message = data.get('message', 'Unknown error')
        return jsonify({'error': f"{message} ({cod})"})

    temp = data['main']['temp']
    humidity = data['main']['humidity']

    save_weather_data(city, temp, humidity)
    forecast_data = forecast_weather(city, current_temp=temp, current_humidity=humidity)

    return jsonify({
        'city': city,
        'temp': temp,
        'humidity': humidity,
        'forecast': forecast_data['forecast'],
        'temp_range': forecast_data['temp_range'],
        'hum_range': forecast_data['hum_range']
    })


@app.route('/download_csv')
def download_csv():
    if os.path.exists(CSV_FILE):
        return send_file(CSV_FILE, as_attachment=True)
    else:
        return "No data available yet."


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store"
    return response


# ---------------- Run the App ----------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




