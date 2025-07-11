from agent import Buyer, Seller
from market import Market
from strategy import generate_strategy
from logger import save_logs
from plotter import plot_price, plot_wealth
import random

# Generate strategies using LLM or fallback
def generate_buyer_strategy():
    return {
        "price_threshold_buy": random.uniform(95, 105),
        "inventory_limit": 20,
        "risk_tolerance": round(random.uniform(0.1, 1.0), 2)
    }

def generate_seller_strategy():
    return {
        "price_threshold_sell": random.uniform(95, 105),
        "inventory_limit": 20,
        "risk_tolerance": round(random.uniform(0.1, 1.0), 2)
    }

# Create market and agents
market = Market()
agents = []

prompt = (
    "Generate a JSON strategy for an agent who wants to buy low and sell high "
    "over 10 simulation rounds. Include inventory limits and risk tolerance."
)

# Create buyers and sellers
for i in range(5):
    buyer = Buyer(f"B{i}", generate_buyer_strategy())
    seller = Seller(f"S{i}", generate_seller_strategy())
    seller.inventory = random.randint(5, 20)
    agents.append(buyer)
    agents.append(seller)

logs = []

# Run simulation
for tick in range(50):
    # Each agent submits order
    for agent in agents:
        order = agent.decide_action(market.last_price)
        if order:
            market.submit_order(order)

    # Match orders and update agents
    agents_by_id = {agent.agent_id: agent for agent in agents}
    market.match_orders(agents_by_id)

    # Log data
    logs.append({
        "tick": tick,
        "price": market.last_price,
        "agents": [
            {"id": a.agent_id, "cash": a.cash, "inventory": a.inventory}
            for a in agents
        ]
    })

# Save and visualize results
save_logs(logs)
plot_price(logs)
for agent in agents:
    plot_wealth(logs, agent.agent_id)
