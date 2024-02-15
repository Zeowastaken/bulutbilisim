import json
from flask import Flask, request, Response,jsonify
import requests

app = Flask(__name__)

@app.route('/weather-forecast', methods=['GET'])
def get_weather_forecast():

    api_url = f'https://api.open-meteo.com/v1/forecast?latitude=39&longitude=35&current=temperature_2m,relative_humidity_2m&hourly=temperature_2m&past_days=2&forecast_days=3'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        return Response(json_data, content_type='application/json; charset=utf-8')
    else:
        return jsonify({'error': 'Hava durumu bilgisi alınamadı.'}), 500

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
