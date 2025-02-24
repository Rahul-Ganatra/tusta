import logging

class TradeLogger:
    def __init__(self, log_file="trade_log.txt"):
        logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
        self.logger = logging.getLogger()

    def log_trade(self, trade):
        if trade["type"] == "BUY":
            log_message = (
                f"BUY Trade | Entry Time: {trade['entry_time']} | Entry Price: {trade['entry_price']} | "
                f"RSI at Entry: {trade['entry_rsi']}"
            )
        elif trade["type"] == "SELL":
            log_message = (
                f"SELL Trade | Exit Time: {trade['exit_time']} | Exit Price: {trade['exit_price']} | "
                f"RSI at Exit: {trade['exit_rsi']}"
            )
        self.logger.info(log_message)
        print(log_message)  # Print to console
