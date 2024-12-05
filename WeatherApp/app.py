from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "3c283267d02a4a708b1144315240412"  # Replace with your actual WeatherAPI key
BASE_URL = "https://api.weatherapi.com/v1/current.json"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')  # Get city name from form input
        if city:
            try:
                response = requests.get(BASE_URL, params={
                    'key': API_KEY,
                    'q': city
                })
                # Debugging: Print the full API response
                print(response.status_code, response.json())
                
                if response.status_code == 200:
                    weather_data = response.json()
                else:
                    error_message = "City not found or an error occurred. Please try again."
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                error_message = "Unable to connect to the weather service. Please try later."
        else:
            error_message = "Please enter a valid city name."

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
