import time

class Node:
    def __init__(self, name):
        self.name = name
        self.running = True

def berkeley_sync(coordinator_node, slave_nodes):

    slave_times = {coordinator_node: time.time()}

    for node in slave_nodes:
        node_time = time.time()
        slave_times[node] = node_time

    print("Tiempos antes de la sincronización:")
    for node, node_time in slave_times.items():
        print(f"{node.name}: {node_time}")

    avg_time = sum(slave_times.values()) / len(slave_times)

    print("Tiempos depues de la sincronización:")
    for node, node_time in slave_times.items():
        correction = avg_time - node_time
        print(f"{node.name}: {node_time + correction}")

def main():
    coordinator_node = Node("Coordinator")
    slave_nodes = [
        Node("Slave1"),
        Node("Slave2"),
        Node("Slave3")
    ]

    while coordinator_node.running:
        time.sleep(5) 
        berkeley_sync(coordinator_node, slave_nodes)

if __name__ == "__main__":
    main()

