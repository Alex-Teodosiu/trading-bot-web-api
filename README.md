# Automated Trading Bot Web API

This is a Flask-based web API for an automated trading bot. The application provides the many endpoints that are documented using Swagger UI.

The application is no longer hosted due to avoid costs.

## Description

This is the application tier of the project, designed to facilitate trading activities through a set of RESTful API endpoints. The bot integrates with the Alpaca trading platform and uses JWT for secure access to its functionalities.

### Features

#### Users

- **DELETE** /users/deleteuser
- **GET** /users/get-email-by-id/{id}
- **GET** /users/getuser/{email}
- **POST** /users/signin
- **POST** /users/signup
- **PUT** /users/updateuser

#### Trading Accounts

- **DELETE** /trading-accounts/deleteaccount
- **GET** /trading-accounts/get-account-by-user-id
- **POST** /trading-accounts/validateaccount

#### Assets

- **GET** /assets/getAMEXstockassets
- **GET** /assets/getARCAstockassets
- **GET** /assets/getBATSstockassets
- **GET** /assets/getNASDAQstockassets
- **GET** /assets/getNYSEstockassets
- **GET** /assets/getOTCstockassets
- **GET** /assets/getcryptoassets

#### Orders

- **DELETE** /orders/cancel-all-orders
- **DELETE** /orders/cancel-order-by-id
- **POST** /orders/create-limit-order
- **POST** /orders/create-order
- **GET** /orders/get-all-orders

#### Positions

- **DELETE** /positions/close-all-open-positions
- **DELETE** /positions/close-position-by-symbol
- **GET** /positions/get-all-open-positions

#### Market Data

- **GET** /market-data/crypto_historical_market_data
- **GET** /market-data/crypto_last_quote
- **GET** /market-data/stock_historical_market_data
- **GET** /market-data/stock_last_quote

#### Algorithms

- **GET** /algorithm/get-all-algorithms-by-user
- **POST** /algorithm/save-algorithm-run
- **DELETE** /algorithm/stop-algorithm

#### Market Status

- **GET** /market-status/get-market-status


## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Virtualenv (for creating virtual environments)

### Setup Virtual Environment

1. **Create a virtual environment:**

   ```bash
   python -m venv .venv

2. **Activate the virtual environment**

Windows:

.venv\Scripts\activate

Linux and macOS:
source .venv/bin/activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Environmental Variables**

Create a .env file in the root directory of the project and add the MANDATORY environment variables:

ALPACA_API_KEY=your_alpaca_api_key
ALPACA_API_SECRET=your_alpaca_api_secret
JWT_SECRET_KEY=your_jwt_secret_key

### Run App

python app.py


### Run Tests

python -m unittest discover -s tests
