# 🌿 BreatheWise Ultra  

An AI-powered, multilingual **Air Quality Tracker** that combines **real-time AQI data, machine learning insights, and smart activity suggestions** — all wrapped in a vibrant, professional UI.  

---

## 🚀 Features  
- 📊 **Real-time AQI Tracking** – Fetches live air quality data from OpenWeatherMap API.  
- 🤖 **ML-powered Smart Summary** – Generates human-like AQI insights using NLP & ML models.  
- 💡 **Activity Suggestions** – Suggests outdoor/indoor activities based on current AQI.  
- 🌐 **Multilingual Support** – Summaries and insights available in multiple languages.  
- 🎨 **Custom Light Theme** – Vibrant, clean, and professional design.  
- ⚡ **Modular Codebase** – Easy to extend and maintain with separate modules:  
  - `app.py` – Streamlit app & UI  
  - `ml_models.py` – ML/NLP models for smart AQI insights  
  - `theme_config.py` – Centralized theme customization  
  - `utils.py` – Helper functions  

---

## 📂 Project Structure  
breathewise-ultra/
│── app.py # Main Streamlit app
│── ml_models.py # ML/NLP models for AQI analysis
│── theme_config.py # Theme and UI settings
│── utils.py # Helper functions (API calls, formatting, etc.)
│── requirements.txt # Dependencies
│── README.md # Documentation

yaml
Copy
Edit

---

## ⚙️ Installation & Setup  

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/breathewise-ultra.git
cd breathewise-ultra
```
2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. **Install dependencies**

```bash
pip install -r requirements.txt
```
3.**Set up API key**

Get your free API key from OpenWeatherMap.

Add it in a .env file:

```ini

OPENWEATHER_API_KEY=your_api_key_here
```
4.**Run the app**

```bash
streamlit run app.py
```


🔮 Roadmap
✅ Smart activity recommendations

✅ Multilingual AQI summaries

⬜️ Historical AQI trend visualization

⬜️ Health-focused AQI alerts

⬜️ Mobile-friendly version

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch

Commit changes

Push to your branch

Submit a pull request 🚀

📜 License
MIT License © 2025 Dharun S
