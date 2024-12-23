import csv
import random
import time

class DataProducer:
    def __init__(self, file_lock, file_path):
        self.file_lock = file_lock
        self.file_path = file_path

    def produce_data(self):
        fieldnames = ["ID", "Product", "Category", "Price", "Quantity"]
        products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"]
        categories = ["Electronics", "Accessories"]

        with self.file_lock:
            with open(self.file_path, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

        for i in range(1, 101):
            row = {
                "ID": i,
                "Product": random.choice(products),
                "Category": random.choice(categories),
                "Price": round(random.uniform(10.0, 1000.0), 2),
                "Quantity": random.randint(1, 20),
            }
            with self.file_lock:
                with open(self.file_path, "a", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(row)
            time.sleep(0.1)
