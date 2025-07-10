import pandas as pd
import numpy as np
from typing import Dict, List
from datetime import datetime, timedelta
import json

class DataProcessor:
    """Advanced data processing and analytics"""
    
    def __init__(self):
        self.pollutant_weights = {
            'pm2_5': 0.3,
            'pm10': 0.25, 
            'o3': 0.2,
            'no2': 0.15,
            'so2': 0.05,
            'co': 0.05
        }
    
    def calculate_composite_score(self, pollutants: Dict) -> float:
        """Calculate weighted composite air quality score"""
        score = 0
        total_weight = 0
        
        for pollutant, concentration in pollutants.items():
            if pollutant in self.pollutant_weights:
                # Normalize concentration (simple linear normalization)
                normalized = min(concentration / 100, 1.0)  # Assuming 100 as max threshold
                score += normalized * self.pollutant_weights[pollutant]
                total_weight += self.pollutant_weights[pollutant]
        
        return (score / total_weight) * 100 if total_weight > 0 else 0
    
    def analyze_trends(self, history: List[Dict]) -> Dict:
        """Analyze air quality trends from historical data"""
        if len(history) < 3:
            return {'trend': 'insufficient_data', 'change': 0, 'forecast': 'unknown'}
        
        # Convert to DataFrame for easier analysis
        df = pd.DataFrame(history)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        
        # Calculate trend
        recent_avg = df.tail(3)['aqi'].mean()
        older_avg = df.head(3)['aqi'].mean()
        
        change = recent_avg - older_avg
        
        if change > 0.5:
            trend = 'worsening'
        elif change < -0.5:
            trend = 'improving'
        else:
            trend = 'stable'
        
        # Simple forecast
        if trend == 'improving':
            forecast = 'likely_to_improve'
        elif trend == 'worsening':
            forecast = 'may_worsen'
        else:
            forecast = 'stable_conditions'
        
        return {
            'trend': trend,
            'change': round(change, 2),
            'forecast': forecast,
            'confidence': min(len(history) / 10, 1.0)  # More data = higher confidence
        }
    
    def generate_health_insights(self, current_aqi: int, pollutants: Dict, 
                               user_profile: Dict, history: List[Dict]) -> Dict:
        """Generate comprehensive health insights"""
        
        # Risk assessment
        base_risk = current_aqi
        
        # Adjust for user vulnerabilities
        age_factor = {
            'Child': 1.2, 'Teen': 1.0, 'Adult': 1.0, 'Senior': 1.3
        }.get(user_profile.get('age_group', 'Adult'), 1.0)
        
        health_factor = 1.0
        sensitive_conditions = ['Asthma', 'Allergies', 'Respiratory Issues', 'Heart Condition', 'Pregnancy']
        if any(condition in user_profile.get('health_conditions', []) for condition in sensitive_conditions):
            health_factor = 1.4
        
        adjusted_risk = min(5, base_risk * age_factor * health_factor)
        
        # Historical exposure analysis
        if history:
            avg_exposure = np.mean([entry['aqi'] for entry in history])
            exposure_trend = 'high' if avg_exposure > 3 else 'moderate' if avg_exposure > 2 else 'low'
        else:
            exposure_trend = 'unknown'
        
        # Specific pollutant concerns
        concerning_pollutants = []
        if pollutants.get('pm2_5', 0) > 35:
            concerning_pollutants.append('PM2.5 (fine particles)')
        if pollutants.get('o3', 0) > 100:
            concerning_pollutants.append('Ozone')
        if pollutants.get('no2', 0) > 40:
            concerning_pollutants.append('Nitrogen Dioxide')
        
        return {
            'adjusted_risk_score': round(adjusted_risk, 1),
            'exposure_history': exposure_trend,
            'concerning_pollutants': concerning_pollutants,
            'personalized_advice': self._generate_personalized_advice(adjusted_risk, user_profile),
            'protection_level': self._get_protection_level(adjusted_risk)
        }
    
    def _generate_personalized_advice(self, risk_score: float, user_profile: Dict) -> List[str]:
        """Generate personalized health advice"""
        advice = []
        
        # Base advice by risk level
        if risk_score >= 4:
            advice.extend([
                "Stay indoors as much as possible",
                "Use air purifiers if available",
                "Avoid all outdoor exercise"
            ])
        elif risk_score >= 3:
            advice.extend([
                "Limit outdoor activities",
                "Wear N95 mask when outside",
                "Consider indoor alternatives for exercise"
            ])
        else:
            advice.extend([
                "Normal activities are generally safe",
                "Stay hydrated",
                "Monitor air quality regularly"
            ])
        
        # Age-specific advice
        if user_profile.get('age_group') in ['Child', 'Senior']:
            advice.append("Extra caution recommended due to age sensitivity")
        
        # Health condition specific advice
        conditions = user_profile.get('health_conditions', [])
        if 'Asthma' in conditions:
            advice.append("Keep rescue inhaler readily available")
        if 'Allergies' in conditions:
            advice.append("Consider antihistamines as directed by healthcare provider")
        if 'Heart Condition' in conditions:
            advice.append("Monitor for chest discomfort or unusual fatigue")
        
        return advice
    
    def _get_protection_level(self, risk_score: float) -> str:
        """Determine required protection level"""
        if risk_score >= 4.5:
            return "Maximum Protection"
        elif risk_score >= 3.5:
            return "High Protection"
        elif risk_score >= 2.5:
            return "Moderate Protection"
        else:
            return "Basic Awareness"
    
    def export_user_data(self, history: List[Dict], user_profile: Dict) -> str:
        """Export user data as JSON for download"""
        export_data = {
            'user_profile': user_profile,
            'air_quality_history': [
                {
                    'timestamp': entry['timestamp'].isoformat(),
                    'city': entry['city'],
                    'aqi': entry['aqi'],
                    'pollutants': entry['pollutants']
                }
                for entry in history
            ],
            'export_timestamp': datetime.now().isoformat(),
            'summary': {
                'total_checks': len(history),
                'average_aqi': np.mean([entry['aqi'] for entry in history]) if history else 0,
                'cities_monitored': len(set(entry['city'] for entry in history)) if history else 0
            }
        }
        
        return json.dumps(export_data, indent=2)
