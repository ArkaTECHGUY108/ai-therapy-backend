from transformers import pipeline

class EmotionDetector:
    def __init__(self):
        self.classifier = pipeline("text-classification", 
                                   model="j-hartmann/emotion-english-distilroberta-base",
                                   return_all_scores=True)

    def analyze(self, text):
        results = self.classifier(text)[0]
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        return sorted_results
