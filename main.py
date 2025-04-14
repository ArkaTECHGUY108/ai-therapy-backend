from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from ml_model.emotion_detector import EmotionDetector

app = FastAPI()
detector = EmotionDetector()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Therapy Chatbot API is Live"}

@app.post("/analyze/")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text", "")
    result = detector.analyze(text)
    return {"input": text, "emotions": result}
