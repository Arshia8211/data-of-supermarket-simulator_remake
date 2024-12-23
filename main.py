from my_package import DataPipeline

if __name__ == "__main__":
    pipeline = DataPipeline()
    pipeline.setup_working_directory()
    pipeline.start_pipeline()
