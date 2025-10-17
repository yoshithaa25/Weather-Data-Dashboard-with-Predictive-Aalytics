# 🌦️ Weather-Data-Dashboard-with-Predictive-Aalytics

A simple yet powerful Flask web app that fetches real-time weather data and generates a 5-day forecast using **Linear Regression**.  
It uses the **OpenWeatherMap API** for live weather and **Plotly.js** for interactive charts.


## 🚀 Features

- ✅ Fetches current weather (temperature & humidity) for any city
- ✅ Uses Linear Regression (scikit-learn) to predict 5-day weather trends
- ✅ Stores data in CSV automatically for continuous learning
- ✅ Interactive charts (Temperature & Humidity) using Plotly
- ✅ Option to download stored weather data
- ✅ Clean, modern UI built with HTML, CSS, and JavaScript


## 🗂️ Project Structure

```text
weather-forecast-dashboard/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Frontend HTML
│
├── static/
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
│
├── weather_data.csv        # Auto-created data file
└── README.md               # Documentation
```

---

## ⚙️ Installation & Setup

1️⃣ **Clone this repository**  

```
git clone https://github.com/<your-username>/weather-forecast-dashboard.git
cd weather-forecast-dashboard
```

2️⃣ **Install dependencies**

```
pip install -r requirements.txt
```

3️⃣ **Add your OpenWeatherMap API key**

```
API_KEY = "YOUR_API_KEY"
```

4️⃣ **Run the Flask app**

```
python app.py
```

---
## 🧩 Tech Stack

| Layer           | Technology                        |
|-----------------|-----------------------------------|
| Backend         | Flask                             |
| Frontend        | HTML, CSS, JavaScript             |
| Data Processing | Pandas                            |
| Machine Learning| scikit-learn (LinearRegression)   |
| Visualization   | Plotly.js                         |
| API             | OpenWeatherMap                    |
```









   
