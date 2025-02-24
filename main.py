from user import User
from trading_strategy import TradingStrategy
from trade_logger import TradeLogger
import time

def main():
    # Load users from the configuration file
    users = User.load_from_config("config.json")
    logger = TradeLogger()

    for user in users:
        print(f"Running strategy for User: {user.user_id}")
        strategy = TradingStrategy(user)
        executed_trades = set()  # Track executed trades

        while True:
            trades = strategy.backtest_trades()

            for trade in trades:
                # Add error handling and logging for missing keys
                try:
                    trade_id = (trade["type"], trade.get("entry_time", time.time()))  # Use current time as fallback
                    if trade_id not in executed_trades:
                        logger.log_trade(trade)
                        executed_trades.add(trade_id)
                except KeyError as e:
                    print(f"Warning: Missing required key in trade data: {e}")
                    continue

            print("Waiting for next update...\n")
            time.sleep(60)  # Fetch new data every 60 seconds

if __name__ == "__main__":
    main()