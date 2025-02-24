import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class User:
    def __init__(self, user_id, buy_threshold=30, sell_threshold=70):
        self.user_id = user_id
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_SECRET_KEY")
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    @staticmethod
    def load_from_config(config_file="config.json"):
        with open(config_file, "r") as file:
            data = json.load(file)
        # Iterate over the list of users
        return [User(**user_data) for user_data in data["user"]]
