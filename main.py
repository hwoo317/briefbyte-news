from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.mock_data import get_news_by_category

app = FastAPI()

# Allow your SwiftUI app to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later you can restrict this to your app's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the News API!"}

@app.get("/api/{category}")
def read_news(category: str):
    news = get_news_by_category(category)
    return {
        "category": category,
        "articles": news
    }
