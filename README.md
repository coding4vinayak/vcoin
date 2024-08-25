### README for VCoin

---

# VCoin

## Overview

VCoin is a simple web-based cryptocurrency simulation built with Flask, Python, and JSON. It gamifies the concept of cryptocurrency mining by allowing users to solve math questions to earn coins. The application provides a leaderboard to track users' progress and coin value based on total supply and mined coins.

## Features

- **Interactive Math Questions:** Users solve simple math problems to earn coins.
- **Coin Mining:** Each correct answer awards a fixed number of coins.
- **Leaderboard:** Displays the top users based on the number of coins mined.
- **Dynamic Coin Value:** The value of a coin is calculated based on the total supply and the number of coins mined.
- **Data Persistence:** User data and mining history are stored in a JSON file.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/coding4vinayak/vcoin.git
   cd vcoin
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv vcoin-env
   source vcoin-env/bin/activate  # On Windows use `vcoin-env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Homepage:** Users are greeted with a math question. They need to solve it to earn coins.
2. **Answer Submission:** Users submit their answers through a form. If the answer is correct, they earn coins.
3. **Leaderboard:** Users can view the leaderboard, which shows the top miners and the value of the coin.

## File Structure

- **app.py:** Main application file containing Flask routes and logic.
- **templates/index.html:** HTML template for the homepage.
- **templates/leaderboard.html:** HTML template for the leaderboard.
- **data.json:** JSON file storing user data and mining history.
- **requirements.txt:** List of Python dependencies.

## Data Storage

- **data.json:** Stores user data (`users` dictionary) and total mined coins (`total_mined_coins`). 
- **Example Content:**
  ```json
  {
    "users": {
      "user1": {"coins": 5, "solved_questions": 10},
      "user2": {"coins": 3, "solved_questions": 5}
    },
    "total_mined_coins": 8
  }
  ```

## How Cryptocurrency Works

### **1. Blockchain Technology:**

- **Definition:** A blockchain is a decentralized, distributed ledger that records transactions across many computers. It ensures that the recorded transactions are secure, immutable, and transparent.
- **Components:** 
  - **Blocks:** Containers of transaction data.
  - **Chain:** A sequence of blocks linked together.
  - **Nodes:** Computers in the network that maintain copies of the blockchain.

### **2. Mining:**

- **Definition:** Mining is the process of validating transactions and adding them to the blockchain. Miners compete to solve complex mathematical problems, and the first to solve the problem gets to add the new block to the blockchain.
- **Proof of Work (PoW):** A consensus mechanism where miners solve computationally intensive puzzles. The first to solve the puzzle is rewarded with new cryptocurrency.

### **3. Cryptographic Hash Functions:**

- **Purpose:** Hash functions ensure data integrity and security. They convert input data into a fixed-size string of characters, which appears random.
- **Usage:** Hash functions are used in the mining process to create a unique identifier for each block.

### **4. Cryptocurrency Wallets:**

- **Definition:** A digital wallet is used to store, send, and receive cryptocurrencies. It holds the public and private keys needed for transactions.
- **Types:**
  - **Hot Wallets:** Connected to the internet, convenient but potentially less secure.
  - **Cold Wallets:** Offline storage, more secure but less convenient.

### **5. Transactions:**

- **Definition:** Transactions involve transferring cryptocurrency from one wallet to another. Each transaction is recorded on the blockchain.
- **Process:**
  - **Initiation:** A user initiates a transaction by creating a digital signature using their private key.
  - **Verification:** The transaction is broadcasted to the network and verified by miners.
  - **Confirmation:** Once verified, the transaction is added to a block and recorded on the blockchain.

### **6. Coin Value and Supply:**

- **Value:** The value of a cryptocurrency can fluctuate based on supply and demand, market sentiment, and external factors.
- **Supply:** The total supply of a cryptocurrency is the maximum number of coins that can ever exist. For example, Bitcoin has a maximum supply of 21 million coins.

### **Conclusion**

VCoin is a fun and educational way to understand the basics of cryptocurrency mining and blockchain technology. By interacting with the app, users can gain insights into how cryptocurrencies work while enjoying a gamified experience.

---
