import numpy as np
import matplotlib.pyplot as plt
import time

class DataReporter:
    def __init__(self, dataframe_holder):
        self.dataframe_holder = dataframe_holder

    def generate_reports(self):
        plt.ion()  
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))  
        bar_ax = axes[0]  
        stat_ax = axes[1]  

        while True:
            data = self.dataframe_holder.get("dataframe")
            if data is not None and len(data) > 0:
                print("Generating live reports...")

                product_names, quantities = np.unique(data["Product"], return_counts=True)
                bar_ax.clear()
                bar_ax.bar(product_names, quantities, color='skyblue')
                bar_ax.set_title("Total Quantity per Product")
                bar_ax.set_xlabel("Product")
                bar_ax.set_ylabel("Total Quantity")

                prices = data["Price"]
                stats = [np.mean(prices), np.min(prices), np.max(prices), np.std(prices)]
                stat_labels = ["Mean", "Min", "Max", "Std Dev"]
                stat_ax.clear()
                stat_ax.bar(stat_labels, stats, color='orange')
                stat_ax.set_title("Price Statistics")
                stat_ax.set_xlabel("Statistic")
                stat_ax.set_ylabel("Value")

                plt.tight_layout()
                plt.pause(0.1)

            time.sleep(5)  
