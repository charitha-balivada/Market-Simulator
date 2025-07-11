from order import Order
import random

class Agent:
    def __init__(self, agent_id, strategy, cash=1000, inventory=0):
        self.agent_id = agent_id
        self.strategy = strategy
        self.cash = cash
        self.inventory = inventory

    def decide_action(self, market_price):
        pass


class Buyer(Agent):
    def decide_action(self, market_price):
        threshold = self.strategy["price_threshold_buy"]
        risk = self.strategy["risk_tolerance"]
        inventory_limit = self.strategy["inventory_limit"]

        # More aggressive buying
        dynamic_threshold = threshold + random.uniform(0, 5 * risk)

        if market_price <= dynamic_threshold and self.cash >= market_price and self.inventory < inventory_limit:
            bid_price = market_price + random.uniform(0.5, 1.5)  # Raise bid
            bid_price = min(bid_price, self.cash)  # Don't overbid
            return Order(self.agent_id, "buy", 1, round(bid_price, 2))
        return None


class Seller(Agent):
    def decide_action(self, market_price):
        threshold = self.strategy["price_threshold_sell"]
        risk = self.strategy["risk_tolerance"]

        # More aggressive selling
        dynamic_threshold = threshold - random.uniform(0, 5 * risk)

        if market_price >= dynamic_threshold and self.inventory > 0:
            ask_price = market_price - random.uniform(0.5, 1.5)  # Lower ask
            ask_price = max(0.01, ask_price)  # Price can't go below 0
            return Order(self.agent_id, "sell", 1, round(ask_price, 2))
        return None
