# data/mock_data.py

def get_news_by_category(category: str):
    sample_data = {
        "politics": [
            {
                "title": "New Policy Debate Heats Up",
                "summary": "Lawmakers are split over the latest reforms.",
                "image": "https://example.com/politics1.jpg"
            },
            {
                "title": "Election Watch 2025",
                "summary": "Key races are gaining traction.",
                "image": "https://example.com/politics2.jpg"
            }
        ],
        "economics": [
            {
                "title": "Stock Markets Rebound",
                "summary": "Markets recovered after a turbulent week.",
                "image": "https://example.com/economics1.jpg"
            }
        ],
        "entertainment": [
            {
                "title": "Award Show Surprises",
                "summary": "Unexpected wins in the latest awards.",
                "image": "https://example.com/entertainment1.jpg"
            }
        ],
        "sports": [
            {
                "title": "Championship Final This Weekend",
                "summary": "Two top teams are ready to clash in the finals.",
                "image": "https://example.com/sports1.jpg"
            },
            {
                "title": "Star Player Breaks Record",
                "summary": "A historic performance in yesterday’s game.",
                "image": "https://example.com/sports2.jpg"
            }
        ],
        "others": [
            {
                "title": "Technology Trends 2025",
                "summary": "What’s coming next in AI, robotics, and beyond.",
                "image": "https://example.com/others1.jpg"
            },
            {
                "title": "World's Tallest Building Planned",
                "summary": "An architectural marvel in the works.",
                "image": "https://example.com/others2.jpg"
            }
        ]
    }

    return sample_data.get(category.lower(), [])
