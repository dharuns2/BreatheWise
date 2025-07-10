import numpy as np
import pandas as pd
from typing import Dict, List
import random
from datetime import datetime, timedelta

class AirQualityPredictor:
    """ML model for predicting air quality trends"""
    
    def __init__(self):
        self.model_accuracy = 0.85
    
    def predict_next_hours(self, current_aqi: int, pollutants: Dict, hours: int = 24) -> List[Dict]:
        """Predict AQI for next N hours using ML simulation"""
        predictions = []
        base_aqi = current_aqi
        
        for hour in range(1, hours + 1):
            # Simulate ML prediction with realistic patterns
            time_factor = np.sin(hour * np.pi / 12)  # Daily pattern
            pollution_trend = -0.1 if hour > 12 else 0.1  # Evening improvement
            noise = random.uniform(-0.3, 0.3)
            
            predicted_aqi = max(1, min(5, base_aqi + time_factor * 0.5 + pollution_trend + noise))
            
            predictions.append({
                'hour': hour,
                'predicted_aqi': round(predicted_aqi, 1),
                'confidence': random.uniform(0.7, 0.95)
            })
        
        return predictions
    
    def predict_weekly_trend(self, current_aqi: int) -> List[Dict]:
        """Predict weekly AQI trend"""
        weekly_data = []
        base_date = datetime.now()
        
        for day in range(7):
            # Simulate weekly patterns
            weekend_factor = 0.3 if day in [5, 6] else 0  # Better on weekends
            weather_factor = random.uniform(-0.5, 0.5)
            
            predicted_aqi = max(1, min(5, current_aqi + weekend_factor + weather_factor))
            
            weekly_data.append({
                'date': (base_date + timedelta(days=day)).strftime('%Y-%m-%d'),
                'day': (base_date + timedelta(days=day)).strftime('%a'),
                'predicted_aqi': round(predicted_aqi, 1)
            })
        
        return weekly_data

class HealthRiskAnalyzer:
    """Analyze health risks based on air quality and user profile"""
    
    def calculate_health_score(self, aqi: int, pollutants: Dict, user_profile: Dict) -> int:
        """Calculate personalized health score"""
        base_score = max(0, 100 - (aqi - 1) * 20)
        
        # Adjust for user profile
        age_adjustment = {
            'Child': -10, 'Teen': -5, 'Adult': 0, 'Senior': -15
        }.get(user_profile['age_group'], 0)
        
        health_adjustment = -5 * len([c for c in user_profile['health_conditions'] if c != 'None'])
        
        # Pollutant-specific adjustments
        pm25_penalty = -pollutants.get('pm2_5', 0) / 10
        
        final_score = max(0, min(100, base_score + age_adjustment + health_adjustment + pm25_penalty))
        return round(final_score)
    
    def get_risk_assessment(self, aqi: int, user_profile: Dict) -> Dict:
        """Comprehensive risk assessment"""
        base_risk = ["Very Low", "Low", "Moderate", "High", "Very High"][aqi - 1]
        
        # Adjust risk based on profile
        sensitive_conditions = ['Asthma', 'Allergies', 'Respiratory Issues', 'Heart Condition', 'Pregnancy']
        is_sensitive = any(condition in user_profile['health_conditions'] for condition in sensitive_conditions)
        
        if is_sensitive and aqi >= 3:
            risk_levels = ["Low", "Moderate", "High", "Very High", "Extreme"]
            adjusted_risk = risk_levels[min(4, aqi - 1)]
        else:
            adjusted_risk = base_risk
        
        return {
            'risk_level': adjusted_risk,
            'is_sensitive_group': is_sensitive,
            'recommendations': self._get_risk_recommendations(adjusted_risk, is_sensitive)
        }
    
    def _get_risk_recommendations(self, risk_level: str, is_sensitive: bool) -> List[str]:
        """Get recommendations based on risk level"""
        recommendations = {
            'Very Low': ["Enjoy outdoor activities", "Perfect time for exercise", "Open windows for fresh air"],
            'Low': ["Good for most outdoor activities", "Monitor if sensitive", "Stay hydrated"],
            'Moderate': ["Limit prolonged outdoor exercise", "Consider indoor alternatives", "Wear mask if sensitive"],
            'High': ["Avoid outdoor exercise", "Stay indoors when possible", "Use air purifier"],
            'Very High': ["Mandatory indoor stay", "Seal windows", "Seek medical advice if symptomatic"],
            'Extreme': ["Emergency protocols", "Immediate shelter", "Contact healthcare provider"]
        }
        
        base_recs = recommendations.get(risk_level, [])
        
        if is_sensitive:
            base_recs.append("Extra precautions for sensitive individuals")
        
        return base_recs

class ActivityRecommender:
    """AI-powered activity recommendations"""
    
    def __init__(self):
        self.activities = {
            1: [  # Excellent air quality
                {"activity": "🏃‍♂️ Outdoor Running", "description": "Perfect conditions for a morning jog", "confidence": 95},
                {"activity": "🚴‍♀️ Cycling", "description": "Great day for bike rides", "confidence": 90},
                {"activity": "🧘‍♀️ Outdoor Yoga", "description": "Practice yoga in the fresh air", "confidence": 85}
            ],
            2: [  # Good air quality
                {"activity": "🚶‍♂️ Walking", "description": "Nice day for a pleasant walk", "confidence": 85},
                {"activity": "⚽ Sports", "description": "Good for outdoor sports", "confidence": 80},
                {"activity": "🌳 Nature Photography", "description": "Clear skies for photography", "confidence": 75}
            ],
            3: [  # Moderate air quality
                {"activity": "🏠 Indoor Exercise", "description": "Consider gym workouts", "confidence": 80},
                {"activity": "🛍️ Shopping", "description": "Indoor shopping activities", "confidence": 75},
                {"activity": "📚 Reading", "description": "Great time for indoor reading", "confidence": 70}
            ],
            4: [  # Poor air quality
                {"activity": "🏠 Stay Indoors", "description": "Indoor activities recommended", "confidence": 90},
                {"activity": "🎬 Movie Time", "description": "Perfect for watching movies", "confidence": 85},
                {"activity": "🍳 Cooking", "description": "Try new indoor recipes", "confidence": 80}
            ],
            5: [  # Very poor air quality
                {"activity": "🔒 Stay Inside", "description": "Mandatory indoor stay", "confidence": 95},
                {"activity": "🧘‍♀️ Meditation", "description": "Practice indoor meditation", "confidence": 90},
                {"activity": "🎨 Creative Arts", "description": "Indoor creative activities", "confidence": 85}
            ]
        }
    
    def get_recommendations(self, aqi: int, user_profile: Dict) -> List[Dict]:
        """Get personalized activity recommendations"""
        base_activities = self.activities.get(aqi, [])
        
        # Personalize based on user profile
        personalized = []
        for activity in base_activities:
            personalized_activity = activity.copy()
            
            # Adjust confidence based on user profile
            if user_profile['activity_level'] == 'High' and aqi <= 2:
                personalized_activity['confidence'] += 5
            elif user_profile['activity_level'] == 'Low' and aqi >= 3:
                personalized_activity['confidence'] += 5
            
            # Health condition adjustments
            if any(condition in user_profile['health_conditions'] for condition in ['Asthma', 'Respiratory Issues']):
                if 'Outdoor' in activity['activity'] and aqi >= 3:
                    personalized_activity['confidence'] -= 20
            
            personalized.append(personalized_activity)
        
        return personalized[:3]  # Return top 3 recommendations

class MoodAnalyzer:
    """Analyze mood correlation with air quality"""
    
    def __init__(self):
        self.mood_keywords = {
            'positive': ['happy', 'energetic', 'great', 'wonderful', 'fantastic', 'good', 'positive'],
            'neutral': ['okay', 'fine', 'normal', 'average', 'decent'],
            'negative': ['tired', 'sluggish', 'headache', 'irritated', 'sad', 'low', 'exhausted']
        }
    
    def analyze_mood(self, mood_text: str, current_aqi: int) -> Dict:
        """Analyze mood and correlate with air quality"""
        mood_text_lower = mood_text.lower()
        
        # Simple sentiment analysis
        positive_count = sum(1 for word in self.mood_keywords['positive'] if word in mood_text_lower)
        negative_count = sum(1 for word in self.mood_keywords['negative'] if word in mood_text_lower)
        
        if positive_count > negative_count:
            detected_mood = "Positive"
            mood_score = 7 + positive_count
        elif negative_count > positive_count:
            detected_mood = "Negative"
            mood_score = 4 - negative_count
        else:
            detected_mood = "Neutral"
            mood_score = 5
        
        # Correlate with air quality
        impact = self._assess_air_quality_impact(mood_score, current_aqi)
        suggestion = self._get_mood_suggestion(detected_mood, current_aqi)
        
        return {
            'mood': detected_mood,
            'score': max(1, min(10, mood_score)),
            'impact': impact,
            'suggestion': suggestion
        }
    
    def _assess_air_quality_impact(self, mood_score: int, aqi: int) -> str:
        """Assess how air quality might be affecting mood"""
        if aqi >= 4 and mood_score <= 5:
            return "Poor air quality may be contributing to low mood"
        elif aqi <= 2 and mood_score >= 7:
            return "Good air quality supporting positive mood"
        elif aqi >= 3 and mood_score <= 6:
            return "Air quality might be affecting your energy levels"
        else:
            return "Air quality appears to have minimal mood impact"
    
    def _get_mood_suggestion(self, mood: str, aqi: int) -> str:
        """Get mood-based suggestions"""
        if mood == "Negative" and aqi >= 3:
            return "Consider indoor relaxation activities and ensure good ventilation"
        elif mood == "Positive" and aqi <= 2:
            return "Great time to enjoy outdoor activities and soak up fresh air"
        elif mood == "Negative":
            return "Try breathing exercises or indoor plants to improve air quality"
        else:
            return "Maintain current activities and monitor how air quality affects you"

class SkyQualityClassifier:
    """Classify sky/air quality from images (simulated)"""
    
    def __init__(self):
        self.quality_indicators = {
            'clear': {'aqi_range': (1, 2), 'visibility': 'excellent', 'color': 'blue'},
            'hazy': {'aqi_range': (2, 3), 'visibility': 'good', 'color': 'light_blue'},
            'smoggy': {'aqi_range': (3, 4), 'visibility': 'poor', 'color': 'gray'},
            'polluted': {'aqi_range': (4, 5), 'visibility': 'very_poor', 'color': 'brown'}
        }
    
    def classify_sky_image(self, image_data=None) -> Dict:
        """Simulate sky quality classification"""
        # In a real implementation, this would use computer vision
        # For demo purposes, we'll simulate the analysis
        
        sky_types = list(self.quality_indicators.keys())
        detected_type = random.choice(sky_types)
        
        quality_info = self.quality_indicators[detected_type]
        
        return {
            'sky_type': detected_type,
            'estimated_aqi_range': quality_info['aqi_range'],
            'visibility': quality_info['visibility'],
            'dominant_color': quality_info['color'],
            'confidence': random.uniform(0.7, 0.95),
            'analysis': f"Sky appears {detected_type} with {quality_info['visibility']} visibility"
        }
