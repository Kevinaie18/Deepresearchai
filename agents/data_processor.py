import pandas as pd

class DataProcessorAgent:
    def __init__(self):
        pass

    def process(self, raw_data):
        if not raw_data:
            return "No data to process"
        
        df = pd.DataFrame({'Extracted Text': raw_data})
        df.drop_duplicates(inplace=True)
        return df
