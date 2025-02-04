import json
import os
import requests
from datetime import datetime
import matplotlib.pyplot as plt

class StockTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.queries = self.load_queries()

    def load_queries(self):
        """Load queries from the JSON file."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            except IOError as e:
                print(f"Error loading queries: {e}")
        return []

    def save_queries(self):
        """Save queries to the JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.queries, file, indent=4)
        except IOError as e:
            print(f"Error saving queries: {e}")

    def fetch_stock_price(self, symbol):
        """Fetch the current stock price using a free API."""
        API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "YOUR_DEFAULT_API_KEY")  # Replace with your Alpha Vantage API key
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if "Global Quote" in data:
                price = float(data["Global Quote"]["05. price"])
                return price
            else:
                print("Error: No data found for the given symbol.")
                return None
        except requests.RequestException as e:
            print(f"Error fetching stock price: {e}")
            return None

    def plot_historical_data(self, symbol):
        """Plot historical stock price data."""
        API_KEY = "TT61EACSPTGKYXSX"  # Replace with your Alpha Vantage API key
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=compact"
        response = requests.get(url)
        data = response.json()

        if "Time Series (Daily)" in data:
            time_series = data["Time Series (Daily)"]
            dates = []
            prices = []

            for date, values in sorted(time_series.items(), reverse=True)[:30]:  # Last 30 days
                dates.append(date)
                prices.append(float(values["4. close"]))

            plt.figure(figsize=(10, 5))
            plt.plot(dates, prices, marker='o')
            plt.title(f"{symbol} Stock Price (Last 30 Days)")
            plt.xlabel("Date")
            plt.ylabel("Closing Price ($)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("Failed to fetch historical data. Please check the symbol.")

    def log_query(self, symbol):
        """Log the query with a timestamp."""
        query = {
            "symbol": symbol,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.queries.append(query)
        self.save_queries()

    def get_all_queries(self):
        """Return all logged queries."""
        return self.queries