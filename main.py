import time
import threading
import queue

class Node:
    def __init__(self, name):
        self.name = name
        self.log_queue = queue.Queue()
        self.running = True

    def run(self):
        while self.running:
            if not self.log_queue.empty():
                log_entry = self.log_queue.get()
                print(f"[{self.name}] {log_entry}")

            time.sleep(1)

    def log(self, message):
        self.log_queue.put(message)


def berkeley_sync(coordinator_node, slave_nodes):

    slave_times = {coordinator_node: time.time()}

    for node in slave_nodes:
        node_time = time.time()
        slave_times[node] = node_time

    print("Tiempos antes de la sincronización:")
    for node, node_time in slave_times.items():
        print(f"{node.name}: {node_time}")

    avg_time = sum(slave_times.values()) / len(slave_times)

    for node, node_time in slave_times.items():
        correction = avg_time - node_time
        node.log(f"sincronizando con el coordinador. Tiempo: {node_time + correction}")


def main():
    coordinator_node = Node("Coordinator")
    slave_nodes = [
        Node("Slave1"),
        Node("Slave2"),
        Node("Slave3")
    ]

    threads = [threading.Thread(target=node.run) for node in [coordinator_node] + slave_nodes]

    for thread in threads:
        thread.start()

    while coordinator_node.running:
        time.sleep(5) 
        berkeley_sync(coordinator_node, slave_nodes)

if __name__ == "__main__":
    main()

