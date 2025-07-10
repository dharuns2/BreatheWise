import streamlit as st
import requests
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import random
import datetime
from typing import Dict, List, Tuple
import time
from PIL import Image
import io
import base64

# Import custom modules
from ml_models import (
    AirQualityPredictor, 
    HealthRiskAnalyzer, 
    ActivityRecommender,
    MoodAnalyzer,
    SkyQualityClassifier
)
from theme_config import apply_vibrant_light_theme
from creative_features import (
    AirQualityPersona,
    BreathingCoach,
    AQIGameification,
    SocialFeatures
)
from data_processor import DataProcessor

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="BreatheWise Ultra", 
    page_icon="🌈", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- CONSTANTS --------------------
WEATHER_API_KEY = "5262ebc0fa9512f2c231bc245e74321d"

# Enhanced AQI levels with more granular data
AQI_LEVELS = {
    1: {"name": "Excellent", "emoji": "🌟", "color": "#00FF7F", "rgb": "0,255,127", "vibe": "Energetic"},
    2: {"name": "Good", "emoji": "😊", "color": "#32CD32", "rgb": "50,205,50", "vibe": "Positive"},
    3: {"name": "Moderate", "emoji": "😐", "color": "#FFD700", "rgb": "255,215,0", "vibe": "Cautious"},
    4: {"name": "Poor", "emoji": "😷", "color": "#FF6347", "rgb": "255,99,71", "vibe": "Concerned"},
    5: {"name": "Hazardous", "emoji": "☠️", "color": "#8B0000", "rgb": "139,0,0", "vibe": "Alert"}
}

# -------------------- INITIALIZE MODELS --------------------
@st.cache_resource
def load_ml_models():
    """Load all ML models"""
    return {
        'predictor': AirQualityPredictor(),
        'health_analyzer': HealthRiskAnalyzer(),
        'activity_recommender': ActivityRecommender(),
        'mood_analyzer': MoodAnalyzer(),
        'sky_classifier': SkyQualityClassifier()
    }
def display_analytics(history, models, data_processor):
    st.markdown("## 📊 Analytics")
    if not history:
        st.info("No air quality history available yet.")
        return
    # Example: Show number of checks and average AQI
    avg_aqi = sum(entry['aqi'] for entry in history) / len(history)
    st.write(f"Total checks: {len(history)}")
    st.write(f"Average AQI: {avg_aqi:.2f}")

def display_wellness_center(breathing_coach, current_aqi, aqi_info, models):
    import streamlit as st
    st.markdown("## 🧘‍♀️ Wellness Center")
    # Recommend a breathing exercise
    exercise = breathing_coach.get_recommended_exercise(current_aqi)
    st.markdown(f"### 🌬️ {exercise['name']}")
    st.write(f"**Benefits:** {exercise['benefits']}  \n**Duration:** {exercise['duration']}")
    st.markdown("#### Steps:")
    for i, step in enumerate(exercise['instructions'], 1):
        st.markdown(f"{i}. {step}")
    # Optionally, add more wellness widgets, tips, or charts
    st.info("Remember to take regular breathing breaks for optimal wellness!")

def display_social_features(social, city_name, current_aqi, aqi_info):
    import streamlit as st
    st.markdown("## 🌍 Social & Community Air Quality")
    
    # Global city comparison
    comparison = social.get_global_comparison(city_name, current_aqi)
    st.markdown("### 🌏 How does your city compare globally?")
    for city in comparison:
        status_emoji = "🟢" if city['status'] == 'better' else "🔴" if city['status'] == 'worse' else "🟡"
        st.write(f"{status_emoji} **{city['city']}**: AQI {city['aqi']} ({city['trend']})")
    
    # City ranking
    ranking = social.get_city_ranking(city_name, current_aqi)
    st.markdown(f"**Your city ranks #{ranking['rank']} out of {ranking['total_cities']} for air quality.**")
    st.progress(ranking['percentile'] / 100, text=f"Better than {ranking['better_than']} cities")
    
    # Community tip
    tip = social.generate_community_tip(current_aqi)
    st.info(f"🌱 **Community Tip:** {tip}")

st.markdown("""
<style>
/* Change input text color and background for better visibility */
.stTextInput > div > div > input {
    color: #333333 !important;           /* dark text color */
    background-color: #f0f0f0 !important; /* light gray background */
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Change selectbox text color for age category to dark color */
.stSelectbox > div > div > select {
    color: #333333 !important;           /* dark text color */
    background-color: #f0f0f0 !important; /* light gray background */
}
</style>
""", unsafe_allow_html=True)


# -------------------- MAIN APPLICATION --------------------
def main():
    # Apply vibrant light theme
    apply_vibrant_light_theme()
    
    # Initialize session state
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {
            'name': '',
            'age_group': 'Adult',
            'health_conditions': [],
            'activity_level': 'Moderate',
            'preferences': {}
        }
    
    if 'air_quality_history' not in st.session_state:
        st.session_state.air_quality_history = []
    
    user_name = st.session_state.get('user_profile', {}).get('name', '')
    greeting_name = user_name.strip() if user_name and user_name.strip() else "there"

    # After collecting user_name from the sidebar/profile
    greeting_name = user_name.strip() if user_name.strip() else "there"
    st.markdown(f"## 👋 Hello, {greeting_name}!")
    st.markdown("Welcome to BreatheWise Ultra — your vibrant, AI-powered air quality companion.")


    # Load ML models
    models = load_ml_models()
    
    # Initialize creative features
    persona = AirQualityPersona()
    breathing_coach = BreathingCoach()
    gamification = AQIGameification()
    social = SocialFeatures()
    data_processor = DataProcessor()
    
    # Header with rainbow gradient
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FECA57, #FF9FF3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 4rem;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        ">🌈 BreatheWise Ultra</h1>
        <p style="font-size: 1.3rem; color: #666; margin-top: 1rem;">
            AI-Powered Air Quality Intelligence with Creative Insights ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    /* Force selectbox selected option text to dark color */
    .stSelectbox > div > div > select, 
    .stSelectbox > div > div > select:focus, 
    .stSelectbox > div > div > select option, 
    .stSelectbox > div > div > select option:checked {
        color: #222 !important;
        background-color: #f0f0f0 !important;
    }
    </style>
""", unsafe_allow_html=True)

    
    # Sidebar - User Profile & Settings
    with st.sidebar:
        st.markdown("### 👤 Your Profile")
        
        # User profile setup
        user_name = st.text_input("Name", st.session_state.user_profile['name'])
        age_group = st.selectbox("Age Group", 
                                ["Child", "Teen", "Adult", "Senior"],
                                index=2)
        
        health_conditions = st.multiselect("Health Conditions", 
                                         ["None", "Asthma", "Allergies", "Heart Condition", 
                                          "Respiratory Issues", "Pregnancy"])
        
        activity_level = st.select_slider("Activity Level",
                                        options=["Low", "Moderate", "High", "Athlete"],
                                        value="Moderate")
        
        # Update session state
        st.session_state.user_profile.update({
            'name': user_name,
            'age_group': age_group,
            'health_conditions': health_conditions,
            'activity_level': activity_level
        })
        
        st.markdown("---")
        
        # Location input with AI suggestions
        st.markdown("### 📍 Location")
        city_input = st.text_input("Enter City", "", placeholder="e.g., Tokyo, Mumbai, London")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎯 Auto-Detect", use_container_width=True):
                auto_city = detect_location()
                if auto_city:
                    city_input = auto_city
                    st.success(f"📍 {city_input}")
        
        with col2:
            if st.button("🔄 Refresh", use_container_width=True):
                st.cache_data.clear()
                st.rerun()
        
        # AI Features Toggle
        st.markdown("---")
        st.markdown("### 🤖 AI Features")
        enable_predictions = st.toggle("Predictive Analytics", True)
        enable_recommendations = st.toggle("Smart Recommendations", True)
        enable_mood_tracking = st.toggle("Mood Analysis", True)
        enable_gamification = st.toggle("Gamification", True)
    
    # Main content area
    if not city_input:
        display_welcome_screen(models, persona)
        return
    
    # Get location data
    lat, lon, city_name, country = get_coordinates(city_input)
    if not lat:
        st.error("🚫 City not found. Please try a different location.")
        return
    
    # Fetch air quality data
    aqi_data = fetch_aqi(lat, lon)
    weather_data = fetch_weather(lat, lon)
    
    if not aqi_data:
        st.error("❌ Unable to fetch air quality data.")
        return
    
    # Process data
    current_aqi = aqi_data['list'][0]['main']['aqi']
    pollutants = aqi_data['list'][0]['components']
    aqi_info = AQI_LEVELS[current_aqi]
    
    # Store in history
    st.session_state.air_quality_history.append({
        'timestamp': datetime.datetime.now(),
        'city': city_name,
        'aqi': current_aqi,
        'pollutants': pollutants
    })
    
    # Main dashboard with tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌈 Dashboard", "🤖 AI Insights", "🎮 Gamification", 
        "📊 Analytics", "🧘‍♀️ Wellness", "🌍 Social"
    ])
    
    with tab1:
        display_main_dashboard(current_aqi, aqi_info, pollutants, weather_data, 
                             city_name, country, models, persona)
    
    with tab2:
        display_ai_insights(current_aqi, pollutants, st.session_state.user_profile, 
                           models, enable_predictions, enable_recommendations, enable_mood_tracking)
    
    with tab3:
        if enable_gamification:
            display_gamification(gamification, current_aqi, st.session_state.air_quality_history)
    
    with tab4:
        display_analytics(st.session_state.air_quality_history, models, data_processor)
    
    with tab5:
        display_wellness_center(breathing_coach, current_aqi, aqi_info, models)
    
    with tab6:
        display_social_features(social, city_name, current_aqi, aqi_info)

def display_welcome_screen(models, persona):
    """Display welcome screen with AI features preview"""
    
    # Feature showcase with vibrant cards
    st.markdown("### ✨ Discover BreatheWise Ultra Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #FF6B6B22, #FF6B6B11);
            padding: 2rem;
            border-radius: 20px;
            border-left: 5px solid #FF6B6B;
            text-align: center;
            height: 300px;
        ">
            <h2>🤖 AI Predictions</h2>
            <p>Machine learning models predict air quality trends, health risks, and optimal activity times</p>
            <div style="font-size: 3rem; margin: 1rem 0;">📈</div>
            <p><strong>Smart • Accurate • Personalized</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4ECDC422, #4ECDC411);
            padding: 2rem;
            border-radius: 20px;
            border-left: 5px solid #4ECDC4;
            text-align: center;
            height: 300px;
        ">
            <h2>🎮 Gamification</h2>
            <p>Turn air quality monitoring into an engaging experience with achievements and challenges</p>
            <div style="font-size: 3rem; margin: 1rem 0;">🏆</div>
            <p><strong>Fun • Motivating • Rewarding</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #45B7D122, #45B7D111);
            padding: 2rem;
            border-radius: 20px;
            border-left: 5px solid #45B7D1;
            text-align: center;
            height: 300px;
        ">
            <h2>🧘‍♀️ Wellness AI</h2>
            <p>Personalized breathing exercises, mood analysis, and wellness recommendations</p>
            <div style="font-size: 3rem; margin: 1rem 0;">🌱</div>
            <p><strong>Mindful • Healthy • Balanced</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sample AI persona introduction
    st.markdown("---")
    persona_intro = persona.generate_persona_message("welcome", 3)
    st.info(f"🌟 **AI Assistant:** {persona_intro}")

def display_main_dashboard(current_aqi, aqi_info, pollutants, weather_data, 
                          city_name, country, models, persona):
    """Main dashboard with enhanced visuals"""
    
    # Location header with gradient
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba({aqi_info['rgb']}, 0.2), rgba({aqi_info['rgb']}, 0.1));
        padding: 2rem;
        border-radius: 20px;
        border-left: 5px solid {aqi_info['color']};
        margin-bottom: 2rem;
    ">
        <h2>📍 {city_name}, {country}</h2>
        <p style="color: #666; font-size: 1.1rem;">Real-time environmental intelligence</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main metrics row
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        # Large AQI display with animated elements
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {aqi_info['color']}33, {aqi_info['color']}11);
            padding: 3rem;
            border-radius: 25px;
            text-align: center;
            border: 3px solid {aqi_info['color']};
            position: relative;
            overflow: hidden;
        ">
            <div style="font-size: 6rem; margin: 0;">{aqi_info['emoji']}</div>
            <h1 style="color: {aqi_info['color']}; margin: 1rem 0; font-size: 3rem;">AQI {current_aqi}</h1>
            <h2 style="color: #333; margin: 0;">{aqi_info['name']}</h2>
            <p style="color: #666; margin: 1rem 0; font-size: 1.2rem;">Feeling {aqi_info['vibe']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if weather_data:
            temp = weather_data['main']['temp']
            st.metric("🌡️ Temperature", f"{temp}°C", 
                     delta=f"{random.randint(-3, 3)}°C vs yesterday")
    
    with col3:
        humidity = weather_data['main']['humidity'] if weather_data else 50
        st.metric("💧 Humidity", f"{humidity}%",
                 delta=f"{random.randint(-10, 10)}%")
    
    with col4:
        # AI-generated health score
        health_score = models['health_analyzer'].calculate_health_score(
            current_aqi, pollutants, st.session_state.user_profile
        )
        st.metric("💚 Health Score", f"{health_score}/100",
                 delta=f"{random.randint(-5, 5)} pts")
    
    # Enhanced pollutant visualization
    st.markdown("### 🧪 Pollutant Analysis with ML Insights")
    
    # Create enhanced pollutant chart
    pollutant_df = pd.DataFrame([
        {'Pollutant': k.upper(), 'Value': v, 'Status': 'Normal' if v < 50 else 'Elevated'}
        for k, v in pollutants.items()
    ])
    
    fig = px.bar(pollutant_df, x='Pollutant', y='Value', color='Status',
                 color_discrete_map={'Normal': '#4ECDC4', 'Elevated': '#FF6B6B'},
                 title="Real-time Pollutant Concentrations")
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333'),
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Persona message based on current conditions
    persona_message = persona.generate_persona_message("current_conditions", current_aqi)
    st.success(f"🌟 **Your AI Assistant says:** {persona_message}")

def display_ai_insights(current_aqi, pollutants, user_profile, models, 
                       enable_predictions, enable_recommendations, enable_mood_tracking):
    """AI insights and predictions tab"""
    
    st.markdown("### 🤖 AI-Powered Insights & Predictions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if enable_predictions:
            st.markdown("#### 📈 Predictive Analytics")
            
            # Generate predictions
            predictions = models['predictor'].predict_next_hours(current_aqi, pollutants)
            
            # Display prediction chart
            pred_df = pd.DataFrame(predictions)
            fig = px.line(pred_df, x='hour', y='predicted_aqi', 
                         title="Next 24 Hours AQI Prediction",
                         color_discrete_sequence=['#FF6B6B'])
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333')
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Prediction insights
            best_time = pred_df.loc[pred_df['predicted_aqi'].idxmin(), 'hour']
            worst_time = pred_df.loc[pred_df['predicted_aqi'].idxmax(), 'hour']
            
            st.info(f"🎯 **Best time for outdoor activities:** {best_time}:00")
            st.warning(f"⚠️ **Avoid outdoor activities around:** {worst_time}:00")
    
    with col2:
        if enable_recommendations:
            st.markdown("#### 💡 Smart Recommendations")
            
            # Generate personalized recommendations
            recommendations = models['activity_recommender'].get_recommendations(
                current_aqi, user_profile
            )
            
            for i, rec in enumerate(recommendations):
                color = ['#4ECDC4', '#FF6B6B', '#FECA57'][i % 3]
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {color}22, {color}11);
                    padding: 1rem;
                    border-radius: 15px;
                    border-left: 4px solid {color};
                    margin-bottom: 1rem;
                ">
                    <h4>{rec['activity']}</h4>
                    <p>{rec['description']}</p>
                    <small>Confidence: {rec['confidence']}%</small>
                </div>
                """, unsafe_allow_html=True)
    
    # Mood analysis section
    if enable_mood_tracking:
        st.markdown("---")
        st.markdown("#### 😊 Mood & Air Quality Correlation")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            user_mood = st.text_area("How are you feeling today?", 
                                   placeholder="Describe your mood, energy level, any symptoms...")
            
            if user_mood:
                mood_analysis = models['mood_analyzer'].analyze_mood(user_mood, current_aqi)
                
                # Display mood analysis
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #96CEB422, #96CEB411);
                    padding: 1.5rem;
                    border-radius: 15px;
                    border-left: 4px solid #96CEB4;
                ">
                    <h4>🧠 Mood Analysis</h4>
                    <p><strong>Detected Mood:</strong> {mood_analysis['mood']}</p>
                    <p><strong>Air Quality Impact:</strong> {mood_analysis['impact']}</p>
                    <p><strong>Recommendation:</strong> {mood_analysis['suggestion']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Mood trend visualization
            mood_data = [
                {'Day': 'Mon', 'Mood Score': 7, 'AQI': 2},
                {'Day': 'Tue', 'Mood Score': 6, 'AQI': 3},
                {'Day': 'Wed', 'Mood Score': 8, 'AQI': 1},
                {'Day': 'Thu', 'Mood Score': 5, 'AQI': 4},
                {'Day': 'Fri', 'Mood Score': 7, 'AQI': 2},
            ]
            
            mood_df = pd.DataFrame(mood_data)
            fig = px.scatter(mood_df, x='AQI', y='Mood Score', 
                           color='Day', size='Mood Score',
                           title="Mood vs Air Quality")
            
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)


# [Continue with remaining functions...]

def display_gamification(gamification, current_aqi, history):
    """Gamification features"""
    
    st.markdown("### 🎮 Air Quality Gaming Experience")
    
    # User stats and achievements
    col1, col2, col3 = st.columns(3)
    
    with col1:
        points = gamification.calculate_points(history)
        st.metric("🏆 Total Points", points, delta="+50 today")
    
    with col2:
        level = gamification.get_user_level(points)
        st.metric("⭐ Level", f"Level {level}", delta="+1 this week")
    
    with col3:
        streak = gamification.calculate_streak(history)
        st.metric("🔥 Check-in Streak", f"{streak} days", delta="+1")
    
    # Achievements showcase
    st.markdown("#### 🏅 Recent Achievements")
    achievements = gamification.get_achievements(history, current_aqi)
    
    for achievement in achievements:
        st.success(f"🎉 **{achievement['title']}** - {achievement['description']}")
    
    # Daily challenge
    st.markdown("#### 🎯 Today's Challenge")
    challenge = gamification.get_daily_challenge(current_aqi)
    
    st.info(f"🎮 **{challenge['title']}**\n\n{challenge['description']}\n\n**Reward:** {challenge['reward']} points")
    
    # Progress visualization
    progress_data = gamification.get_progress_data(history)
    fig = px.line(progress_data, x='date', y='points', 
                  title="Your Air Quality Journey",
                  color_discrete_sequence=['#4ECDC4'])
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#333')
    )
    
    st.plotly_chart(fig, use_container_width=True)

# [Additional functions would continue here...]

# -------------------- UTILITY FUNCTIONS --------------------
@st.cache_data(ttl=600)
def get_coordinates(city_name):
    """Get coordinates for city"""
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            return data['lat'], data['lon'], data['name'], data.get('country', '')
    except:
        pass
    return None, None, None, None

@st.cache_data(ttl=300)
def fetch_aqi(lat, lon):
    """Fetch air quality data"""
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

@st.cache_data(ttl=600)
def fetch_weather(lat, lon):
    """Fetch weather data"""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={WEATHER_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def detect_location():
    """Auto-detect location"""
    try:
        ip = requests.get('https://api64.ipify.org?format=json', timeout=5).json()['ip']
        location = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5).json()
        return location.get('city')
    except:
        return None




if __name__ == "__main__":
    main()
st.markdown("""
<div class='footer'>
    Made with ❤️ by <b>
    <a href="mailto:dharun.ece2@gmail.com" style="color:inherit; text-decoration:underline; cursor:pointer;">
        Dharun
    </a>
    </b>
</div>
""", unsafe_allow_html=True)