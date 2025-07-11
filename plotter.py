import matplotlib.pyplot as plt

def plot_price(logs):
    prices = [log["price"] for log in logs]
    ticks = list(range(len(prices)))
    plt.figure(figsize=(8, 4))
    plt.plot(ticks, prices, label="Price", color="blue")
    plt.title("Market Price Over Time")
    plt.xlabel("Tick")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_wealth(logs, agent_id):
    cash = []
    inventory = []
    ticks = []

    for log in logs:
        for agent in log["agents"]:
            if agent["id"] == agent_id:
                cash.append(agent["cash"])
                inventory.append(agent["inventory"])
                ticks.append(log["tick"])
                break  

    fig, ax = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax[0].plot(ticks, cash, color="green")
    ax[0].set_title(f"{agent_id} Cash Over Time")
    ax[0].set_ylabel("Cash")
    ax[0].grid(True)

    ax[1].plot(ticks, inventory, color="orange")
    ax[1].set_title(f"{agent_id} Inventory Over Time")
    ax[1].set_xlabel("Tick")
    ax[1].set_ylabel("Inventory")
    ax[1].grid(True)

    plt.tight_layout()
    plt.show()
