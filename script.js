document.getElementById("weatherForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const city = document.getElementById("city").value.trim();
    const resultDiv = document.getElementById("weatherResult");
    const chartDiv = document.getElementById("forecastChart");

    resultDiv.innerHTML = "<em>Loading...</em>";
    chartDiv.innerHTML = "";

    fetch("/get_weather", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `city=${encodeURIComponent(city)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
            return;
        }

        // Display current weather
        resultDiv.innerHTML = `
            <h3>${data.city}</h3>
            <p>🌡️ Temperature: ${data.temp.toFixed(1)} °C</p>
            <p>💧 Humidity: ${data.humidity}%</p>
        `;

        const dates = data.forecast.map(f => f[0]);
        const temps = data.forecast.map(f => parseFloat(f[1]));
        const hums = data.forecast.map(f => parseFloat(f[2]));

        const tempTrace = {
            x: dates,
            y: temps,
            name: "Temperature (°C)",
            type: "scatter",
            mode: "lines+markers+text",
            line: { color: "#e74c3c", width: 3, shape: "linear" },
            marker: { size: 8, symbol: "circle" },
            text: temps.map(t => t.toFixed(1) + "°C"),
            textposition: "top center",
            hovertemplate: "%{x}<br>Temp: %{y} °C<extra></extra>"
        };

        const humTrace = {
            x: dates,
            y: hums,
            name: "Humidity (%)",
            type: "scatter",
            mode: "lines+markers+text",
            line: { color: "#3498db", width: 3, dash: "dot", shape: "linear" },
            marker: { size: 8, symbol: "diamond" },
            yaxis: "y2",
            text: hums.map(h => h + "%"),
            textposition: "bottom center",
            hovertemplate: "%{x}<br>Humidity: %{y}%<extra></extra>"
        };

        const layout = {
            title: `${data.city} — 5-Day Forecast`,
            xaxis: { title: "Date" },  // Keep X-axis same as original
            yaxis: {
                title: "Temperature (°C)",
                titlefont: { color: "#e74c3c" },
                tickfont: { color: "#e74c3c" },
                range: data.temp_range
            },
            yaxis2: {
                title: "Humidity (%)",
                titlefont: { color: "#3498db" },
                tickfont: { color: "#3498db" },
                overlaying: "y",
                side: "right",
                range: data.hum_range
            },
            legend: { orientation: "h", x: 0.5, xanchor: "center", y: -0.2 },
            margin: { t: 60, b: 70 },  // Keep original bottom margin
            hovermode: "closest"
        };

        Plotly.purge(chartDiv);  // Clear old plot
        Plotly.newPlot(chartDiv, [tempTrace, humTrace], layout, { responsive: true });
    })
    .catch(err => {
        console.error(err);
        resultDiv.innerHTML = `<p style="color:red;">Error fetching data</p>`;
    });
});







