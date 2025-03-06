from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")

@app.route('/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    if not API_KEY:
        return jsonify({"error": "API key not set"}), 500
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if "Time Series (1min)" in data:
        return jsonify(data["Time Series (1min)"])
    else:
        return jsonify({"error": "Stock data not found"}), 404

@app.route('/trade', methods=['POST'])
def execute_trade():
    data = request.get_json()
    print(f"Trade received: {data}")
    # Simulate trade execution logic here.
    return jsonify({"message": "Trade executed successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
