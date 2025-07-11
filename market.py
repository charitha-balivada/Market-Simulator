import random

class Market:
    def __init__(self, initial_price=100):
        self.orders = []
        self.trade_history = []
        self.last_price = initial_price

    def submit_order(self, order):
        self.orders.append(order)

    def match_orders(self, agents_by_id):
        buys = sorted([o for o in self.orders if o.order_type == "buy"], key=lambda x: -x.price)
        sells = sorted([o for o in self.orders if o.order_type == "sell"], key=lambda x: x.price)
        trades = []

        while buys and sells and buys[0].price >= sells[0].price:
            buy = buys.pop(0)
            sell = sells.pop(0)

            price = (buy.price + sell.price) / 2
            quantity = min(buy.quantity, sell.quantity)

            # Update buyer and seller directly
            buyer = agents_by_id[buy.agent_id]
            seller = agents_by_id[sell.agent_id]

            buyer.cash -= price * quantity
            buyer.inventory += quantity

            seller.cash += price * quantity
            seller.inventory -= quantity

            trades.append((buy.agent_id, sell.agent_id, price, quantity))
            self.last_price = price

        if not trades:
            self.last_price += random.uniform(-1, 1)
            self.last_price = round(self.last_price, 2)

        self.orders = []
        self.trade_history.extend(trades)
        return trades
