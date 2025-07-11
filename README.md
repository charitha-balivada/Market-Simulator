# Market Simulator with Agent Strategies

This project simulates a market with multiple agents (buyers and sellers) interacting based on individual strategies. Each agent makes buy/sell decisions depending on price thresholds, risk tolerance, and inventory/cash constraints. The market matches orders and adjusts prices dynamically over time.

---

## Project Structure

```
market-simulator/
├── agent.py         # Buyer and Seller agent logic
├── order.py         # Order class to represent buy/sell orders
├── market.py        # Market class to process and match orders
├── logger.py        # Utility to save simulation logs
├── plotter.py       # Visualizations (market price & agent wealth)
├── strategy.py      # Strategy generator (rule-based or LLM)
├── main.py          # Main simulation script
├── logs.json        # Sample output of the simulation
├── README.md        # Project documentation
└── screenshots/     # Folder for output plots (optional)
```

How to Run the Simulator?
1. Install all the required packages using `pip install -r requirements.txt`
2. Run the simulation using `python main.py`

What happens?
* The simulation runs for 50 ticks.
* 5 buyers and 5 sellers place buy/sell orders based on their individual strategies.
* The market processes and matches orders.
* Logs are saved to logs.json.
* Plots are displayed showing market price trends and each agent’s wealth (Attached in the Plots folder in the repository).

Output:
1. Logs: Logs are stored in logs.json, one of them I added in the repository.
2. Plots: 
* Market Price Over Time: A line plot showing how the price fluctuates over 50 ticks.
* Agent Wealth Over Time:
  For each agent, a plot showing:
  1. Cash on hand
  2. Inventory held
