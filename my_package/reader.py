import numpy as np
import time

class DataReader:
    def __init__(self, file_lock, file_path, dataframe_holder):
        self.file_lock = file_lock
        self.file_path = file_path
        self.dataframe_holder = dataframe_holder

    def read_data(self):
        while True:
            with self.file_lock:
                try:
                    data = np.genfromtxt(self.file_path, delimiter=",", dtype=None, encoding=None, names=True)
                    self.dataframe_holder["dataframe"] = data
                except Exception:
                    pass
            time.sleep(1)
