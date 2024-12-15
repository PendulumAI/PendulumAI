import os
import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

class TemporalConfig:
    def __init__(self):
        self.session_insights = []

    def process_time_patterns(self, timestamp):
        components = {
            "hour": timestamp.hour,
            "minute": timestamp.minute,
            "second": timestamp.second
        }
        self.session_insights.append(components)

    def analyze_temporal_patterns(self, transactions):
        for tx in transactions:
            components = {
                "hour": tx["timestamp"].hour,
                "minute": tx["timestamp"].minute,
                "second": tx["timestamp"].second
            }
            self.session_insights.append(components)
            print(f"Transaction ID: {tx['transaction_id']}")
            print(f"Time Components: {components}")

if __name__ == "__main__":
    config = TemporalConfig()

    mock_transactions = [
        {"transaction_id": "tx001", "timestamp": datetime.datetime(2024, 12, 12, 14, 30, 15)},
        {"transaction_id": "tx002", "timestamp": datetime.datetime(2024, 12, 12, 15, 45, 20)},
        {"transaction_id": "tx003", "timestamp": datetime.datetime(2024, 12, 12, 16, 5, 10)}
    ]

    config.analyze_temporal_patterns(mock_transactions)
