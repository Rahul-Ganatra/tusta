# 📌 Indicator-Based Trading System

## 📖 Overview
This project is a **backend system** for an **RSI-based trading strategy** that fetches **real-time market data** from Binance and executes trades based on **user-defined RSI thresholds**.

---

## 🚀 Features
- ✅ **Fetches live market data** from Binance API.
- ✅ **Calculates RSI (Relative Strength Index)** using `pandas-ta`.
- ✅ **Executes Buy/Sell trades** based on RSI thresholds.
- ✅ **Supports multiple users** with unique trading parameters.
- ✅ **Logs trade execution details** to `trade_log.txt`.
- ✅ **Secure API Key storage** using `.env` file.

---

## 🛠️ Technology Stack
- **Python 3.8+**
- **Binance API (`python-binance`)** – Fetches real-time market data.
- **pandas & pandas-ta** – Processes and calculates technical indicators.
- **dotenv** – Secures API credentials in an `.env` file.
- **logging** – Logs trade execution details.

---

## 🔧 Setup & Installation

### 1️⃣ Install Dependencies
```bash
pip install python-binance pandas pandas-ta python-dotenv
```

### 2️⃣ Create a `.env` File
Store your Binance API credentials **securely** in a `.env` file:
```plaintext
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key
```

### 3️⃣ Update `config.json`
Define **user-specific RSI parameters** in `config.json`:
```json
{
    "user": [
        {
            "user_id": "user1",
            "buy_threshold": 30,
            "sell_threshold": 70
        }
    ]
}
```

### 4️⃣ Run the Trading System
```bash
python main.py
```

---

## 📂 Project Structure
```
/trading_system
│── .env                  # Binance API credentials
│── user.py               # User class for RSI parameters
│── trade_strategy.py     # TradingStrategy class for handling trade logic
│── trade_logger.py       # TradeLogger class for logging trades
│── main.py               # Main execution script
│── config.json           # User-specific RSI parameters
│── trade_log.txt         # Trade execution logs
│── README.md             # Setup and usage instructions
```

---

## 📊 How It Works
1️⃣ **Loads API Credentials** securely from `.env`.

2️⃣ **Fetches historical market data** from Binance.

3️⃣ **Calculates RSI values** using `pandas-ta`.

4️⃣ **Executes BUY/SELL trades** when RSI crosses the defined thresholds.

5️⃣ **Logs all trade executions** into `trade_log.txt`.

6️⃣ **Repeats every 60 seconds** to analyze market conditions.

---

## 📄 Example Trade Log (`trade_log.txt`)
```
2025-02-24 19:19:11,839 - SELL Trade | Exit Time: 1740085200000 | Exit Price: 98089.46 | RSI at Exit: 64.32744897154689
2025-02-24 19:19:11,840 - SELL Trade | Exit Time: 1740146400000 | Exit Price: 98777.77 | RSI at Exit: 61.458536113089274
```
✅ **Profit from this trade:** `98777.77 - 98089.46 = 688.31 USDT`
