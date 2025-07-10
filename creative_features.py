import random
from typing import Dict, List
from datetime import datetime, timedelta

class AirQualityPersona:
    """AI personality that provides contextual, creative responses"""
    
    def __init__(self):
        self.personality_traits = {
            'cheerful': ['excited', 'optimistic', 'energetic'],
            'caring': ['concerned', 'supportive', 'nurturing'],
            'wise': ['knowledgeable', 'thoughtful', 'analytical'],
            'playful': ['fun', 'creative', 'engaging']
        }
        
        self.response_templates = {
            'welcome': [
                "🌟 Welcome to your personal air quality journey! I'm here to help you breathe smarter and live healthier!",
                "✨ Ready to discover what the air around you is telling you? Let's explore together!",
                "🌈 Your intelligent air quality companion is here! Let's make breathing an adventure!"
            ],
            'excellent': [
                "🎉 Fantastic! The air is absolutely pristine today - perfect for all your outdoor dreams!",
                "🌟 This is air quality gold! Time to step outside and embrace nature's gift!",
                "✨ The atmosphere is singing with purity today - what outdoor adventure calls to you?"
            ],
            'good': [
                "😊 The air quality is looking great! A wonderful day to be active outside.",
                "🌱 Good vibes in the air today! Perfect timing for that outdoor activity you've been planning.",
                "🌤️ The air is welcoming you outside - enjoy the fresh atmosphere!"
            ],
            'moderate': [
                "🤔 The air has some personality today. Maybe balance indoor and outdoor activities?",
                "⚖️ It's an interesting air day - perfect for mindful choices about your activities.",
                "🌟 The air quality is moderate - a great time to be aware and make smart decisions!"
            ],
            'poor': [
                "😷 The air needs some love today. Let's focus on indoor wellness and protection!",
                "🏠 Time for some cozy indoor activities while the air takes a breather outside.",
                "💙 Your health comes first - let's make today about indoor comfort and care."
            ],
            'hazardous': [
                "🚨 The air needs serious attention today. Your safety is my top priority - stay protected indoors!",
                "🛡️ This is a day for maximum protection and indoor sanctuary. Let's keep you safe and healthy!",
                "⚠️ Emergency air quality mode activated - time for complete indoor protection!"
            ]
        }
    
    def generate_persona_message(self, situation: str, aqi_level: int = None) -> str:
        """Generate contextual personality-driven messages"""
        if situation == 'welcome':
            return random.choice(self.response_templates['welcome'])
        
        if situation == 'current_conditions' and aqi_level:
            level_map = {1: 'excellent', 2: 'good', 3: 'moderate', 4: 'poor', 5: 'hazardous'}
            level_key = level_map.get(aqi_level, 'moderate')
            return random.choice(self.response_templates[level_key])
        
        return "🌈 I'm here to help you navigate your air quality journey with wisdom and care!"
    
    def generate_creative_tip(self, aqi_level: int, time_of_day: str) -> str:
        """Generate creative, time-aware tips"""
        creative_tips = {
            (1, 'morning'): "🌅 Start your day with a sunrise meditation outside - the air is pristine!",
            (1, 'afternoon'): "☀️ Perfect lunch break for a park picnic or outdoor meeting!",
            (1, 'evening'): "🌆 Golden hour + clean air = perfect evening stroll magic!",
            (2, 'morning'): "🌱 Great morning for window yoga or balcony stretching!",
            (2, 'afternoon'): "🚶‍♀️ Ideal time for a mindful walk around the neighborhood!",
            (2, 'evening'): "🌙 Lovely evening for stargazing or outdoor dinner!",
            (3, 'morning'): "🏠 Start indoors with energizing breathing exercises!",
            (3, 'afternoon'): "🌿 Time for indoor plants appreciation and air purification rituals!",
            (3, 'evening'): "🕯️ Create a cozy indoor atmosphere with natural scents!",
            (4, 'morning'): "🧘‍♀️ Begin with indoor meditation and air quality mindfulness!",
            (4, 'afternoon'): "📚 Perfect reading weather with air purifier ambiance!",
            (4, 'evening'): "🛁 Relaxing bath time with aromatherapy for respiratory wellness!",
            (5, 'morning'): "🏠 Indoor sanctuary mode - create your healthy haven!",
            (5, 'afternoon'): "🎨 Creative indoor time - art, music, or gentle movement!",
            (5, 'evening'): "💤 Early rest and recovery - your body deserves protection!"
        }
        
        # Determine time of day
        current_hour = datetime.now().hour
        if current_hour < 12:
            time_key = 'morning'
        elif current_hour < 18:
            time_key = 'afternoon'
        else:
            time_key = 'evening'
        
        return creative_tips.get((aqi_level, time_key), 
                               "🌈 Make every moment count with mindful air quality awareness!")

class BreathingCoach:
    """Interactive breathing exercise coach"""
    
    def __init__(self):
        self.exercises = {
            'stress_relief': {
                'name': '4-7-8 Relaxation',
                'instructions': [
                    "Find a comfortable seated position",
                    "Inhale through nose for 4 counts",
                    "Hold breath for 7 counts", 
                    "Exhale through mouth for 8 counts",
                    "Repeat 3-4 cycles"
                ],
                'benefits': 'Reduces stress and anxiety, promotes relaxation',
                'duration': '2-3 minutes'
            },
            'energy_boost': {
                'name': 'Energizing Breath',
                'instructions': [
                    "Sit or stand with spine straight",
                    "Rapid belly breathing for 30 seconds",
                    "Hold breath for 15 seconds",
                    "Long, slow exhale for 30 seconds",
                    "Repeat 2-3 times"
                ],
                'benefits': 'Increases energy and mental clarity',
                'duration': '3-4 minutes'
            },
            'purification': {
                'name': 'Air Purification Breath',
                'instructions': [
                    "Visualize clean, pure air entering your lungs",
                    "Inhale slowly for 6 counts",
                    "Pause and feel the clean air in your body",
                    "Exhale slowly for 8 counts, releasing toxins",
                    "Repeat with intention for 5-7 cycles"
                ],
                'benefits': 'Mental air purification and mindfulness',
                'duration': '5-7 minutes'
            }
        }
    
    def get_recommended_exercise(self, aqi_level: int, user_mood: str = 'neutral') -> Dict:
        """Recommend breathing exercise based on air quality and mood"""
        if aqi_level >= 4:
            return self.exercises['purification']
        elif user_mood in ['stressed', 'anxious', 'negative']:
            return self.exercises['stress_relief']
        else:
            return self.exercises['energy_boost']
    
    def generate_guided_session(self, exercise_name: str) -> List[Dict]:
        """Generate a guided breathing session"""
        exercise = self.exercises.get(exercise_name, self.exercises['stress_relief'])
        
        session_steps = []
        for i, instruction in enumerate(exercise['instructions']):
            session_steps.append({
                'step': i + 1,
                'instruction': instruction,
                'duration': random.randint(15, 60),  # seconds
                'visual_cue': self._get_visual_cue(instruction)
            })
        
        return session_steps
    
    def _get_visual_cue(self, instruction: str) -> str:
        """Generate visual cues for instructions"""
        if 'inhale' in instruction.lower():
            return "🌬️⬆️"
        elif 'exhale' in instruction.lower():
            return "💨⬇️"
        elif 'hold' in instruction.lower():
            return "⏸️"
        else:
            return "🧘‍♀️"

class AQIGameification:
    """Gamification system for air quality monitoring"""
    
    def __init__(self):
        self.achievements = {
            'first_check': {'title': 'Air Quality Explorer', 'description': 'First air quality check!', 'points': 10},
            'week_streak': {'title': 'Consistency Champion', 'description': '7 days of checking air quality', 'points': 50},
            'health_conscious': {'title': 'Health Guardian', 'description': 'Avoided outdoor activity during poor air quality', 'points': 25},
            'fresh_air_lover': {'title': 'Fresh Air Enthusiast', 'description': 'Enjoyed 5 excellent air quality days', 'points': 40},
            'weather_wizard': {'title': 'Weather Wisdom', 'description': 'Predicted air quality improvement', 'points': 30}
        }
        
        self.challenges = {
            'daily_monitor': {
                'title': 'Daily Air Quality Detective',
                'description': 'Check air quality at least once today',
                'reward': 15,
                'type': 'daily'
            },
            'week_planner': {
                'title': 'Weekly Wellness Planner', 
                'description': 'Plan 3 activities based on air quality forecasts',
                'reward': 100,
                'type': 'weekly'
            },
            'indoor_master': {
                'title': 'Indoor Wellness Master',
                'description': 'Complete 3 indoor activities during poor air quality',
                'reward': 75,
                'type': 'situational'
            }
        }
    
    def calculate_points(self, history: List[Dict]) -> int:
        """Calculate total points from user history"""
        base_points = len(history) * 5  # 5 points per check-in
        
        # Bonus points for consistency
        if len(history) >= 7:
            base_points += 50  # Week streak bonus
        
        # Quality bonus
        excellent_days = sum(1 for entry in history if entry['aqi'] == 1)
        base_points += excellent_days * 10
        
        return base_points
    
    def get_user_level(self, points: int) -> int:
        """Calculate user level based on points"""
        if points < 50:
            return 1
        elif points < 150:
            return 2
        elif points < 300:
            return 3
        elif points < 500:
            return 4
        else:
            return 5
    
    def calculate_streak(self, history: List[Dict]) -> int:
        """Calculate consecutive days streak"""
        if not history:
            return 0
        
        # Sort by timestamp
        sorted_history = sorted(history, key=lambda x: x['timestamp'], reverse=True)
        
        streak = 1
        current_date = sorted_history[0]['timestamp'].date()
        
        for entry in sorted_history[1:]:
            entry_date = entry['timestamp'].date()
            if (current_date - entry_date).days == 1:
                streak += 1
                current_date = entry_date
            else:
                break
        
        return streak
    
    def get_achievements(self, history: List[Dict], current_aqi: int) -> List[Dict]:
        """Get unlocked achievements"""
        unlocked = []
        
        if len(history) >= 1:
            unlocked.append(self.achievements['first_check'])
        
        if self.calculate_streak(history) >= 7:
            unlocked.append(self.achievements['week_streak'])
        
        excellent_count = sum(1 for entry in history if entry['aqi'] == 1)
        if excellent_count >= 5:
            unlocked.append(self.achievements['fresh_air_lover'])
        
        return unlocked[-3:]  # Return last 3 achievements
    
    def get_daily_challenge(self, current_aqi: int) -> Dict:
        """Get today's challenge based on conditions"""
        if current_aqi >= 4:
            return self.challenges['indoor_master']
        else:
            return self.challenges['daily_monitor']
    
    def get_progress_data(self, history: List[Dict]) -> List[Dict]:
        """Generate progress data for visualization"""
        if not history:
            return []
        
        progress = []
        cumulative_points = 0
        
        for i, entry in enumerate(sorted(history, key=lambda x: x['timestamp'])):
            cumulative_points += 5  # Base points per check-in
            
            # Bonus points
            if entry['aqi'] == 1:
                cumulative_points += 10
            
            progress.append({
                'date': entry['timestamp'].strftime('%Y-%m-%d'),
                'points': cumulative_points,
                'level': self.get_user_level(cumulative_points)
            })
        
        return progress

class SocialFeatures:
    """Social and community features"""
    
    def __init__(self):
        self.global_cities = [
            {'city': 'Tokyo', 'aqi': 2, 'trend': 'improving'},
            {'city': 'London', 'aqi': 3, 'trend': 'stable'},
            {'city': 'Paris', 'aqi': 2, 'trend': 'improving'},
            {'city': 'New York', 'aqi': 3, 'trend': 'declining'},
            {'city': 'Mumbai', 'aqi': 4, 'trend': 'stable'},
            {'city': 'Sydney', 'aqi': 1, 'trend': 'stable'},
            {'city': 'Berlin', 'aqi': 2, 'trend': 'improving'},
            {'city': 'Singapore', 'aqi': 2, 'trend': 'stable'}
        ]
    
    def get_global_comparison(self, current_city: str, current_aqi: int) -> List[Dict]:
        """Compare current city with global cities"""
        comparison = []
        
        for city_data in self.global_cities:
            if city_data['city'].lower() != current_city.lower():
                comparison.append({
                    'city': city_data['city'],
                    'aqi': city_data['aqi'],
                    'difference': current_aqi - city_data['aqi'],
                    'trend': city_data['trend'],
                    'status': 'better' if current_aqi > city_data['aqi'] else 'worse' if current_aqi < city_data['aqi'] else 'same'
                })
        
        return sorted(comparison, key=lambda x: x['aqi'])[:5]
    
    def generate_community_tip(self, aqi_level: int) -> str:
        """Generate community-sourced tips"""
        community_tips = {
            1: [
                "🌟 Community tip: Perfect day for outdoor photography! Share your clear sky photos!",
                "🏃‍♀️ Runners in your area recommend early morning jogs today!",
                "🌱 Garden enthusiasts say it's ideal for planting and outdoor garden work!"
            ],
            2: [
                "😊 Local cyclists suggest scenic route rides today!",
                "🧘‍♀️ Yoga groups are meeting in parks - great air for outdoor practice!",
                "🚶‍♂️ Walking groups report excellent conditions for nature walks!"
            ],
            3: [
                "⚖️ Community suggests limiting outdoor workout duration to 30-45 minutes",
                "🏠 Indoor fitness enthusiasts recommend trying new workout videos!",
                "🌿 Plant lovers suggest checking on indoor air-purifying plants today"
            ],
            4: [
                "😷 Community recommends N95 masks for essential outdoor activities",
                "🏠 Indoor cooking enthusiasts share healthy immune-boosting recipes!",
                "💨 Air purifier users suggest running them on high today"
            ],
            5: [
                "🚨 Community emergency tip: Stay indoors and seal windows with tape if needed",
                "🏥 Health groups recommend monitoring symptoms and seeking help if needed",
                "🔒 Essential workers in your area recommend maximum protection gear"
            ]
        }
        
        tips = community_tips.get(aqi_level, community_tips[3])
        return random.choice(tips)
    
    def get_city_ranking(self, current_city: str, current_aqi: int) -> Dict:
        """Get city ranking in air quality"""
        all_cities = self.global_cities + [{'city': current_city, 'aqi': current_aqi, 'trend': 'current'}]
        
        sorted_cities = sorted(all_cities, key=lambda x: x['aqi'])
        
        for i, city in enumerate(sorted_cities):
            if city['city'].lower() == current_city.lower():
                return {
                    'rank': i + 1,
                    'total_cities': len(all_cities),
                    'percentile': round((i + 1) / len(all_cities) * 100, 1),
                    'better_than': len(all_cities) - i - 1
                }
        
        return {'rank': len(all_cities), 'total_cities': len(all_cities), 'percentile': 100, 'better_than': 0}
