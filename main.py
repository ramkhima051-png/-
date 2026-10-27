from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# यूज़र का डाटा (Coins और Ads का रिकॉर्ड)
user_data = {"coins": 0, "ads_watched": 0}

# वीडियो ऐड्स के लिंक (यहाँ आप बाद में अपने YouTube Shorts के लिंक डाल सकते हैं)
video_ads = [
    "https://www.youtube.com/embed/2Vv-BfVoq4g?autoplay=1",
    "https://www.youtube.com/embed/LXb3EKWsInQ?autoplay=1",
    "https://www.youtube.com/embed/9bZkp7q19f0?autoplay=1"
]

@app.get("/", response_class=HTMLResponse)
def home():
    # यह वेबसाइट का असली डिज़ाइन (HTML/CSS) है
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Global Ad Network</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color: #1e1e2f; color: white; margin: 0; padding: 20px; }}
            .container {{ background: #2a2a40; padding: 20px; border-radius: 15px; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); max-width: 400px; margin: auto; border: 1px solid #3a3a50; }}
            h1 {{ color: #00d2ff; font-size: 26px; margin-bottom: 5px; }}
            p {{ color: #aaa; font-size: 14px; margin-bottom: 20px; }}
            .stats {{ display: flex; justify-content: space-around; background: #1e1e2f; padding: 15px; border-radius: 10px; font-weight: bold; margin-bottom: 20px; border: 1px solid #333; }}
            .coin {{ color: #ffd700; font-size: 22px; text-shadow: 0 0 10px #ffd700; }}
            .watch {{ color: #ff4757; font-size: 22px; }}
            iframe {{ width: 100%; height: 220px; border-radius: 10px; border: 2px solid #00d2ff; margin-bottom: 15px; background: #000; }}
            button {{ background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border: none; padding: 15px 20px; font-size: 18px; font-weight: bold; border-radius: 10px; cursor: pointer; width: 100%; transition: 0.3s; box-shadow: 0 5px 15px rgba(0, 210, 255, 0.4); }}
            button:hover {{ transform: scale(1.05); box-shadow: 0 8px 20px rgba(0, 210, 255, 0.6); }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Global Ad Network</h1>
            <p>Watch Ads & Earn Rewards Automatically</p>
            
            <div class="stats">
                <div>💰 Coins<br><span id="coins" class="coin">{user_data['coins']}</span></div>
                <div>📺 Watched<br><span id="watched" class="watch">{user_data['ads_watched']}</span></div>
            </div>
            
            <div id="ad-container">
                <img src="https://media.giphy.com/media/L05HgB2h6qICDs5Sms/giphy.gif" width="100%" style="border-radius:10px; margin-bottom:15px;" alt="Waiting for Ad">
            </div>

            <button onclick="watchAd()">▶ Watch Ad (Auto Earn)</button>
        </div>

        <script>
            // यह ऑटोमैटिक काम करने वाला जावास्क्रिप्ट फंक्शन है
            async function watchAd() {{
                document.getElementById('ad-container').innerHTML = "<h3 style='color:#00d2ff;'>Loading Ad... ⏳</h3>";
                
                const response = await fetch('/watch-ad');
                const data = await response.json();
                
                // बिना पेज रिफ्रेश किए डेटा बदलें
                document.getElementById('coins').innerText = data.coins;
                document.getElementById('watched').innerText = data.ads_watched;
                
                // नया वीडियो लगाएँ
                document.getElementById('ad-container').innerHTML = `<iframe src="${{data.video_url}}" allow="autoplay; encrypted-media" allowfullscreen></iframe>`;
            }}
        </script>
    </body>
    </html>
    """
    return html_content

# यह बैकएंड API है जो सिक्कों का हिसाब रखती है
@app.get("/watch-ad")
def watch_ad():
    user_data["coins"] += 10
    user_data["ads_watched"] += 1
    return {
        "coins": user_data["coins"],
        "ads_watched": user_data["ads_watched"],
        "video_url": random.choice(video_ads)
    }
