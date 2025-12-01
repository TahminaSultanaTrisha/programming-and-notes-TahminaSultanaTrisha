#!/usr/bin/env python3
"""
Medical Assistant ChatBot - Guided Conversation Flow
Follows: Greeting → Disease Identification → Math → Jokes → Weather
"""

import random
import json
import os
import re
import argparse
from datetime import datetime
import requests


class MedicalChatBot:
    def __init__(self, intents_file="intents.json", knowledge_file="knowledge_base.txt"):
        self.intents_file = intents_file
        self.knowledge_file = knowledge_file
        self.intents = {}
        self.knowledge_base = {}
        self.conversation_step = 0  # 0: greeting, 1: disease, 2: math, 3: jokes, 4: weather
        self.user_name = ""

        print("🔄 Loading chatbot data...")
        self.load_data()
        print("✅ Medical Assistant ChatBot ready!")

    def load_data(self):
        """Load intents and knowledge base from files"""
        # Load intents from JSON file
        try:
            if os.path.exists(self.intents_file):
                with open(self.intents_file, 'r', encoding='utf-8') as f:
                    self.intents = json.load(f)
                print(f"✅ Loaded {len(self.intents)} intents from {self.intents_file}")
            else:
                print(f"⚠️  Intents file {self.intents_file} not found")
                self.intents = {}
        except Exception as e:
            print(f"❌ Error loading intents: {e}")
            self.intents = {}

        # Load knowledge base from text file
        try:
            if os.path.exists(self.knowledge_file):
                with open(self.knowledge_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and ':' in line:
                            topic, info = line.split(':', 1)
                            self.knowledge_base[topic.strip().lower()] = info.strip()
                print(f"✅ Loaded {len(self.knowledge_base)} topics from {self.knowledge_file}")
            else:
                print(f"⚠️  Knowledge file {self.knowledge_file} not found")
        except Exception as e:
            print(f"❌ Error loading knowledge base: {e}")

    def get_greeting_response(self, user_input):
        """Handle greeting and get user's name"""
        if self.conversation_step == 0:
            # Extract name from input
            name_patterns = [
                r"my name is (\w+)",
                r"i am (\w+)",
                r"call me (\w+)",
                r"you can call me (\w+)",
                r"this is (\w+)"
            ]

            for pattern in name_patterns:
                match = re.search(pattern, user_input.lower())
                if match:
                    self.user_name = match.group(1).title()
                    self.conversation_step = 1
                    return (f"Nice to meet you, {self.user_name}! 👋\n"
                            f"Now, let me help you identify potential health concerns.\n"
                            f"Please tell me about any symptoms you're experiencing.\n"
                            f"For example: 'I have headache and fever' or 'I feel tired with cough'")

            # If no name found, ask for it
            return ("Hello! I'm your Medical Assistant ChatBot. 🤖\n"
                    "What's your name?")

        return None

    def identify_disease(self, user_input):
        """Simple disease identification based on symptoms"""
        if self.conversation_step == 1:
            symptoms = user_input.lower()

            # Common symptoms and possible conditions
            conditions = {
                "fever": ["Common Cold", "Flu", "COVID-19", "Infection"],
                "cough": ["Common Cold", "Flu", "COVID-19", "Bronchitis"],
                "headache": ["Migraine", "Tension Headache", "Dehydration", "Sinusitis"],
                "fatigue": ["Anemia", "Sleep Disorders", "Thyroid Issues", "Chronic Fatigue"],
                "sore throat": ["Strep Throat", "Common Cold", "Flu", "Tonsillitis"],
                "nausea": ["Food Poisoning", "Migraine", "Gastroenteritis", "Pregnancy"],
                "chest pain": ["Seek IMMEDIATE medical attention!", "Angina", "Heart Issues", "Anxiety"],
                "shortness of breath": ["Seek IMMEDIATE medical attention!", "Asthma", "Anxiety", "COVID-19"]
            }

            # Find matching symptoms
            found_symptoms = []
            possible_conditions = set()

            for symptom, diseases in conditions.items():
                if symptom in symptoms:
                    found_symptoms.append(symptom)
                    possible_conditions.update(diseases)

            if found_symptoms:
                response = (f"Based on your symptoms: {', '.join(found_symptoms)}\n"
                            f"⚠️  POSSIBLE CONDITIONS (NOT A DIAGNOSIS):\n")

                for condition in list(possible_conditions)[:5]:  # Show max 5 conditions
                    response += f"   • {condition}\n"

                response += ("\n🔴 IMPORTANT MEDICAL DISCLAIMER:\n"
                             "   This is NOT medical advice. I'm an AI assistant.\n"
                             "   Please consult a healthcare professional for proper diagnosis.\n"
                             "   For emergencies, call emergency services immediately.\n\n"
                             "Now, let's move to some math calculations! 🧮\n"
                             "Give me a math problem like '5 + 3' or '10 * 2':")

                self.conversation_step = 2
                return response
            else:
                return ("I didn't recognize specific symptoms. Please describe how you're feeling.\n"
                        "Examples: headache, fever, cough, tiredness, etc.")

        return None

    def handle_calculation(self, user_input):
        """Handle mathematical calculations"""
        if self.conversation_step == 2:
            calculation_pattern = r'(\d+)\s*([+\-*/])\s*(\d+)'
            match = re.search(calculation_pattern, user_input)

            if match:
                try:
                    num1 = int(match.group(1))
                    operator = match.group(2)
                    num2 = int(match.group(3))

                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        if num2 == 0:
                            result = "undefined (cannot divide by zero)"
                        else:
                            result = num1 / num2
                    else:
                        return "I don't recognize that operation. Try +, -, *, or /"

                    self.conversation_step = 3
                    return (f"🧮 Math Result: {num1} {operator} {num2} = {result}\n\n"
                            "Great! Now let me tell you a joke to lighten the mood! 😄\n"
                            "Type 'tell me a joke' or just press Enter:")

                except Exception as e:
                    return f"Sorry, I couldn't calculate that: {e}"
            else:
                return "Please give me a math problem like '5 + 3' or '10 * 2'"

        return None

    def handle_joke_request(self, user_input):
        """Tell a joke if requested or at this step"""
        if self.conversation_step == 3:
            joke_words = ['joke', 'funny', 'laugh', 'humor', '']

            if any(word in user_input.lower() for word in joke_words) or user_input.strip() == "":
                jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Why did the scarecrow win an award? He was outstanding in his field!",
                    "Why don't eggs tell jokes? They'd crack each other up!",
                    "What do you call a fake noodle? An impasta!",
                    "Why did the math book look so sad? Because it had too many problems!",
                    "What do you call a sleeping bull? A bulldozer!",
                    "Why don't skeletons fight each other? They don't have the guts!",
                    "What do you call a bear with no teeth? A gummy bear!"
                ]

                self.conversation_step = 4
                return (f"😂 {random.choice(jokes)}\n\n"
                        "Now, let's check the weather! 🌤️\n"
                        "Which city's weather would you like to know?\n"
                        "Options: Leeds, London, Manchester or type 'current location':")

        return None

    def get_real_weather(self, city_name):
        """Get REAL current weather from OpenWeatherMap API"""
        try:
            # Free API key for OpenWeatherMap
            api_key = "b6907d289e10d714a6e88b30761fae22"  # Free demo key

            # City coordinates for more accurate results
            city_coordinates = {
                "leeds": {"lat": 53.8008, "lon": -1.5491},
                "london": {"lat": 51.5074, "lon": -0.1278},
                "manchester": {"lat": 53.4808, "lon": -2.2426},
                "current location": {"lat": 53.8008, "lon": -1.5491}  # Default to Leeds
            }

            if city_name.lower() in city_coordinates:
                coords = city_coordinates[city_name.lower()]
                url = f"https://api.openweathermap.org/data/2.5/weather?lat={coords['lat']}&lon={coords['lon']}&appid={api_key}&units=metric"
            else:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                weather_data = response.json()

                temperature = round(weather_data['main']['temp'])
                feels_like = round(weather_data['main']['feels_like'])
                humidity = weather_data['main']['humidity']
                wind_speed = round(weather_data['wind']['speed'] * 3.6)
                condition = weather_data['weather'][0]['description'].title()

                return {
                    "temperature": temperature,
                    "feels_like": feels_like,
                    "condition": condition,
                    "humidity": humidity,
                    "wind_speed": wind_speed,
                    "success": True
                }
            else:
                return {"success": False, "error": "Weather service unavailable"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def handle_weather_request(self, user_input):
        """Handle weather queries"""
        if self.conversation_step == 4:
            cities = ["leeds", "london", "manchester", "current location"]
            mentioned_cities = [city for city in cities if city in user_input.lower()]

            if not mentioned_cities:
                return "Please choose: Leeds, London, Manchester or type 'current location'"

            city = mentioned_cities[0]
            display_city = "Leeds" if city == "current location" else city.title()

            print(f"🌤️ Getting real weather data for {display_city}...")
            real_weather = self.get_real_weather(city)

            if real_weather["success"]:
                return (f"🌤️ REAL Current Weather in {display_city}:\n"
                        f"   Temperature: {real_weather['temperature']}°C\n"
                        f"   Feels like: {real_weather['feels_like']}°C\n"
                        f"   Condition: {real_weather['condition']}\n"
                        f"   Humidity: {real_weather['humidity']}%\n"
                        f"   Wind: {real_weather['wind_speed']} km/h\n"
                        f"   Updated: {datetime.now().strftime('%H:%M')}\n\n"
                        f"🎉 Thank you for chatting with me, {self.user_name if self.user_name else 'friend'}!\n"
                        f"This completes our guided conversation. Stay healthy! 💙\n"
                        f"Type 'restart' to start over or 'bye' to exit.")
            else:
                # Fallback to simulated weather
                simulated_weather = {
                    "leeds": {"temp": random.randint(5, 12), "condition": "Cloudy"},
                    "london": {"temp": random.randint(8, 15), "condition": "Partly Cloudy"},
                    "manchester": {"temp": random.randint(6, 13), "condition": "Light Rain"},
                    "current location": {"temp": random.randint(5, 12), "condition": "Cloudy"}
                }

                weather = simulated_weather[city]
                return (f"🌤️ Weather in {display_city} (API unavailable):\n"
                        f"   Temperature: {weather['temp']}°C\n"
                        f"   Condition: {weather['condition']}\n\n"
                        f"🎉 Thank you for chatting with me, {self.user_name if self.user_name else 'friend'}!\n"
                        f"This completes our guided conversation. Stay healthy! 💙\n"
                        f"Type 'restart' to start over or 'bye' to exit.")

        return None

    def generate_response(self, user_input):
        """Generate response based on conversation flow"""
        user_input = user_input.lower().strip()

        # Check for restart or exit commands
        if user_input == 'restart':
            self.conversation_step = 0
            self.user_name = ""
            return "🔄 Conversation restarted! What's your name?"

        if user_input in ['bye', 'exit', 'quit', 'goodbye']:
            return f"👋 Goodbye, {self.user_name if self.user_name else 'friend'}! Take care and stay healthy!"

        # Follow the conversation flow
        if self.conversation_step == 0:
            return self.get_greeting_response(user_input)
        elif self.conversation_step == 1:
            return self.identify_disease(user_input)
        elif self.conversation_step == 2:
            return self.handle_calculation(user_input)
        elif self.conversation_step == 3:
            return self.handle_joke_request(user_input)
        elif self.conversation_step == 4:
            return self.handle_weather_request(user_input)
        else:
            return "I'm not sure what to do next. Type 'restart' to start over."


def main():
    """Main function to run the guided conversation chatbot"""
    parser = argparse.ArgumentParser(description='Medical Assistant ChatBot - Guided Conversation')
    parser.add_argument('--intents', '-i', default='intents.json',
                        help='Path to intents JSON file')
    parser.add_argument('--knowledge', '-k', default='knowledge_base.txt',
                        help='Path to knowledge base text file')

    try:
        args = parser.parse_args()
    except SystemExit:
        args = argparse.Namespace(intents='intents.json', knowledge='knowledge_base.txt')

    print("=" * 70)
    print("🤖 Welcome to Medical Assistant ChatBot!")
    print("I'll guide you through: Hello → Health Check → Math → Jokes → Weather")
    print("=" * 70)

    chatbot = MedicalChatBot(args.intents, args.knowledge)

    # Start the guided conversation
    print("\nChatBot: Hello! I'm your Medical Assistant ChatBot. 🤖")
    print("ChatBot: What's your name?")

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            response = chatbot.generate_response(user_input)
            print(f"ChatBot: {response}")

            if "goodbye" in response.lower():
                break

        except KeyboardInterrupt:
            print("\n\nChatBot: Oops! Goodbye! 👋")
            break
        except Exception as e:
            print(f"ChatBot: Sorry, I encountered an error: {e}")


if __name__ == "__main__":
    main()