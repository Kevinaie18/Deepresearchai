from transformers import pipeline

class AnalysisAgent:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def analyze(self, data):
        if data.empty:
            return "No data to analyze"
        
        text = " ".join(data["Extracted Text"].tolist())
        summary = self.summarizer(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]['summary_text']
