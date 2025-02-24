from binance.client import Client
import pandas as pd
import pandas_ta as ta

class TradingStrategy:
    def __init__(self, user, symbol="BTCUSDT", timeframe="1h"):
        self.user = user
        self.symbol = symbol
        self.timeframe = timeframe
        self.client = Client(user.api_key, user.api_secret)

    def fetch_historical_data(self):
        # Calculate the number of data points needed for 5 days
        if self.timeframe == "1h":
            limit = 5 * 24  # 5 days of hourly data
        elif self.timeframe == "1d":
            limit = 5  # 5 days of daily data
        else:
            raise ValueError("Unsupported timeframe")

        klines = self.client.get_klines(symbol=self.symbol, interval=self.timeframe, limit=limit)
        df = pd.DataFrame(klines, columns=["timestamp", "open", "high", "low", "close", "volume", "_", "_", "_", "_", "_", "_"])
        df = df[["timestamp", "open", "high", "low", "close", "volume"]]
        df["close"] = df["close"].astype(float)
        df["RSI"] = ta.rsi(df["close"], length=14)  # Calculate RSI
        return df

    def backtest_trades(self):
        df = self.fetch_historical_data()
        trade_log = []

        for i in range(1, len(df)):
            curr_rsi = df["RSI"].iloc[i]
            prev_rsi = df["RSI"].iloc[i - 1]

            if prev_rsi < self.user.buy_threshold and curr_rsi > self.user.buy_threshold:
                entry_price = df["close"].iloc[i]
                entry_time = df["timestamp"].iloc[i]
                trade_log.append({
                    "type": "BUY",
                    "entry_time": entry_time,
                    "entry_price": entry_price,
                    "entry_rsi": curr_rsi
                })

            if prev_rsi > self.user.sell_threshold and curr_rsi < self.user.sell_threshold:
                exit_price = df["close"].iloc[i]
                exit_time = df["timestamp"].iloc[i]
                trade_log.append({
                    "type": "SELL",
                    "exit_time": exit_time,
                    "exit_price": exit_price,
                    "exit_rsi": curr_rsi
                })

        return trade_log
