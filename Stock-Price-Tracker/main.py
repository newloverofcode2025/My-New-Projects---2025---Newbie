from stock_tracker import StockTracker
import os
import json

def initialize_queries():
    """Initialize the queries.json file if it doesn't exist."""
    if not os.path.exists('queries.json'):
        try:
            with open('queries.json', 'w') as file:
                json.dump([], file)
        except IOError as e:
            print(f"Error initializing queries.json: {e}")

def fetch_stock_price(stock_tracker):
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    try:
        price = stock_tracker.fetch_stock_price(symbol)
        if price:
            print(f"Current price of {symbol}: ${price:.2f}")
        else:
            print("Failed to fetch stock price. Please check the symbol.")
    except Exception as e:
        print(f"Error fetching stock price: {e}")

def view_historical_data(stock_tracker):
    # Placeholder for viewing historical data
    print("Viewing historical data...")

def view_all_queries(stock_tracker):
    # Placeholder for viewing all queries
    print("Viewing all queries...")

def main():
    # Initialize the queries.json file
    initialize_queries()

    # Initialize the StockTracker
    stock_tracker = StockTracker("queries.json")

    while True:
        print("\n=== Stock Price Tracker ===")
        print("1. Fetch Stock Price")
        print("2. View Historical Data")
        print("3. View All Queries")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            fetch_stock_price(stock_tracker)
        elif choice == "2":
            view_historical_data(stock_tracker)
        elif choice == "3":
            view_all_queries(stock_tracker)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()