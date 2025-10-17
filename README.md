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


## 🧠 How It Works

1. The user enters a city name.  
2. Flask fetches live weather data from OpenWeatherMap API.  
3. Data is stored in `weather_data.csv`.  
4. Linear Regression models predict the next 5 days of **temperature** and **humidity**.  
5. Forecast is visualized in an interactive Plotly chart with dual Y-axes.

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



```markdown
## ⚙️ Installation & Setup

1️⃣ **Clone this repository**  

```bash
git clone https://github.com/<your-username>/weather-forecast-dashboard.git
cd weather-forecast-dashboard

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt

3️⃣ **Add your OpenWeatherMap API key**

```python
API_KEY = "YOUR_API_KEY"

4️⃣ **Run the Flask app**

```bash
python app.py


---


```markdown
## 🧩 Tech Stack

| Layer           | Technology                        |
|-----------------|----------------------------------|
| Backend         | Flask                             |
| Frontend        | HTML, CSS, JavaScript             |
| Data Processing | Pandas                            |
| Machine Learning| scikit-learn (LinearRegression)   |
| Visualization   | Plotly.js                         |
| API             | OpenWeatherMap                    |




   
