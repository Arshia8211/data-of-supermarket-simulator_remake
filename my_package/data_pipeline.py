import os
import threading
from .producer import DataProducer
from .reader import DataReader
from .reporter import DataReporter

class DataPipeline:
    def __init__(self, file_path="data.csv"):
        self.file_lock = threading.Lock()
        self.dataframe_holder = {}
        self.file_path = file_path

    def setup_working_directory(self, dir_name="data_directory"):
        os.makedirs(dir_name, exist_ok=True)
        os.chdir(dir_name)

    def start_pipeline(self):
        producer = DataProducer(self.file_lock, self.file_path)
        reader = DataReader(self.file_lock, self.file_path, self.dataframe_holder)
        reporter = DataReporter(self.dataframe_holder)

        producer_thread = threading.Thread(target=producer.produce_data)
        reader_thread = threading.Thread(target=reader.read_data)
        reporter_thread = threading.Thread(target=reporter.generate_reports)

        producer_thread.start()
        reader_thread.start()
        reporter_thread.start()

        producer_thread.join()
        reader_thread.join()
        reporter_thread.join()
