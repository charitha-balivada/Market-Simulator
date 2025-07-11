class Order:
    def __init__(self, agent_id, order_type, quantity, price):
        self.agent_id = agent_id
        self.order_type = order_type  # "buy" or "sell"
        self.quantity = quantity
        self.price = price
