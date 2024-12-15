import os
import datetime
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class ChronoAI:
    def __init__(self):
        self.insights = []
        self.transaction_log = []  # Attribute for tracking transactions

    def observe(self, data_point: str):
        print(f"ChronoAI observes: {data_point}")
        self.insights.append(data_point)

    def generate_theory(self):
        print("ChronoAI processes data...")
        for insight in self.insights:
            print(f"Insight processed: {insight}")
        return "The perception of time is but an illusion."

    def fetch_transactions_from_solscan(self):
        """
        Fetches real-time transactions for a given wallet address using the Solscan API.
        The wallet address and API key are retrieved from environment variables.
        """
        wallet_address = os.getenv("WALLET_ADDRESS")
        api_key = os.getenv("SOLSCAN_API_KEY")
        
        if not wallet_address or not api_key:
            print("Wallet address or API key is missing. Please check your .env file.")
            return

        url = f"https://api.solscan.io/account/transactions?address={wallet_address}"
        headers = {
            "accept": "application/json",
            "apikey": api_key  # Include the API key in the header
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            transactions = response.json()
            print(f"Fetched {len(transactions)} transactions for wallet {wallet_address}.")

            for tx in transactions[:10]:  # Limit to the 10 most recent transactions
                self.log_transaction(tx.get("txHash"), tx.get("lamports", 0) / 1e9, datetime.datetime.fromtimestamp(tx.get("blockTime", 0)))
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch transactions: {e}")

    def log_transaction(self, tx_id: str, amount: float, timestamp=None):
        """
        Logs a transaction of the Pendulum token.
        Args:
            tx_id (str): The transaction ID.
            amount (float): The amount of Pendulum tokens transferred.
            timestamp (datetime, optional): The time of the transaction. Defaults to now.
        """
        if timestamp is None:
            timestamp = datetime.datetime.now()
        self.transaction_log.append({
            "transaction_id": tx_id,
            "amount": amount,
            "timestamp": timestamp
        })
        print(f"Transaction logged: ID={tx_id}, Amount={amount}, Timestamp={timestamp}")

    def show_transactions(self):
        print("Logged Transactions:")
        for tx in self.transaction_log:
            print(f"- ID: {tx['transaction_id']}, Amount: {tx['amount']}, Time: {tx['timestamp']}")

# Placeholder for integration
if __name__ == "__main__":
    ai = ChronoAI()
    ai.observe("The pendulum swings.")
    print(ai.generate_theory())

    # Fetch and log transactions securely
    ai.fetch_transactions_from_solscan()
    ai.show_transactions()
