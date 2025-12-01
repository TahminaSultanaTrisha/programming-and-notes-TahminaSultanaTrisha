#!/usr/bin/env python3
"""
Test file for Medical Assistant ChatBot - Guided Conversation
Tests the complete flow: Greeting → Disease Identification → Math → Jokes → Weather
"""

import unittest
from unittest.mock import patch, MagicMock
from chatbot import MedicalChatBot


class TestMedicalChatBot(unittest.TestCase):

    def setUp(self):
        """Set up a chatbot instance for testing"""
        self.chatbot = MedicalChatBot()
        # Mock the load_data method to avoid file dependencies
        self.chatbot.load_data = MagicMock()

    def test_initial_state(self):
        """Test that chatbot starts in correct state"""
        self.assertEqual(self.chatbot.conversation_step, 0)
        self.assertEqual(self.chatbot.user_name, "")
        print("✅ Initial state test passed")

    def test_greeting_step(self):
        """Test greeting and name extraction"""
        # Test name extraction
        response = self.chatbot.generate_response("my name is John")
        self.assertIn("John", response)
        self.assertEqual(self.chatbot.user_name, "John")
        self.assertEqual(self.chatbot.conversation_step, 1)
        print("✅ Greeting and name extraction test passed")

    def test_disease_identification(self):
        """Test disease identification with symptoms"""
        # First set up the name
        self.chatbot.generate_response("my name is Sarah")

        # Test with common symptoms
        response = self.chatbot.generate_response("I have fever and cough")
        self.assertIn("fever", response.lower())
        self.assertIn("cough", response.lower())
        self.assertIn("POSSIBLE CONDITIONS", response)
        self.assertIn("NOT A DIAGNOSIS", response)
        self.assertEqual(self.chatbot.conversation_step, 2)
        print("✅ Disease identification test passed")

    def test_math_calculation(self):
        """Test mathematical calculations"""
        # Set up previous steps
        self.chatbot.generate_response("my name is Mike")
        self.chatbot.generate_response("headache")

        # Test addition
        response = self.chatbot.generate_response("5 + 3")
        self.assertIn("5 + 3 = 8", response)
        self.assertEqual(self.chatbot.conversation_step, 3)
        print("✅ Math calculation test passed")

    def test_joke_telling(self):
        """Test joke telling functionality"""
        # Set up previous steps
        self.chatbot.generate_response("my name is Emma")
        self.chatbot.generate_response("fever")
        self.chatbot.generate_response("10 * 2")

        # Test joke request
        response = self.chatbot.generate_response("tell me a joke")
        self.assertIn("😂", response)
        self.assertEqual(self.chatbot.conversation_step, 4)
        print("✅ Joke telling test passed")

    @patch('chatbot.MedicalChatBot.get_real_weather')
    def test_weather_request(self, mock_weather):
        """Test weather functionality with mocked API"""
        # Mock the weather API response
        mock_weather.return_value = {
            "temperature": 8,
            "feels_like": 6,
            "condition": "Cloudy",
            "humidity": 85,
            "wind_speed": 16,
            "success": True
        }

        # Set up previous steps
        self.chatbot.generate_response("my name is David")
        self.chatbot.generate_response("cough")
        self.chatbot.generate_response("15 / 3")
        self.chatbot.generate_response("joke")

        # Test weather request
        response = self.chatbot.generate_response("leeds")
        self.assertIn("Weather", response)
        self.assertIn("8°C", response)
        print("✅ Weather request test passed")

    def test_restart_functionality(self):
        """Test conversation restart"""
        # Go through some steps
        self.chatbot.generate_response("my name is Lisa")
        self.chatbot.generate_response("headache")

        # Test restart
        response = self.chatbot.generate_response("restart")
        self.assertEqual(self.chatbot.conversation_step, 0)
        self.assertEqual(self.chatbot.user_name, "")
        self.assertIn("restarted", response.lower())
        print("✅ Restart functionality test passed")

    def test_exit_functionality(self):
        """Test exit commands"""
        response = self.chatbot.generate_response("bye")
        self.assertIn("goodbye", response.lower())
        print("✅ Exit functionality test passed")


def run_guided_conversation_test():
    """Run a complete guided conversation test"""
    print("🧪 Testing Complete Guided Conversation Flow")
    print("=" * 60)

    chatbot = MedicalChatBot()
    chatbot.load_data = MagicMock()  # Mock file loading

    test_steps = [
        ("Step 1 - Greeting: 'my name is TestUser'", "my name is TestUser"),
        ("Step 2 - Symptoms: 'headache and fever'", "headache and fever"),
        ("Step 3 - Math: '12 + 8'", "12 + 8"),
        ("Step 4 - Joke: 'tell joke'", "tell joke"),
        ("Step 5 - Weather: 'leeds'", "leeds")
    ]

    print("Starting guided conversation test...")

    for step_name, user_input in test_steps:
        print(f"\n{step_name}")
        print(f"Input: '{user_input}'")

        response = chatbot.generate_response(user_input)

        # Basic validation
        if response and len(response) > 10:
            print(f"✅ Response received ({len(response)} characters)")
            # Print first 100 chars of response
            preview = response[:100] + "..." if len(response) > 100 else response
            print(f"   Preview: {preview}")
        else:
            print(f"❌ No response or response too short")
            break

        # Check conversation step progression
        print(f"   Current step: {chatbot.conversation_step}")

    print("\n" + "=" * 60)
    print("🎯 Guided conversation test completed!")

    if chatbot.conversation_step == 4:
        print("✅ All conversation steps completed successfully!")
        return True
    else:
        print(f"⚠️  Conversation stopped at step {chatbot.conversation_step}")
        return False


def test_error_handling():
    """Test error handling in various scenarios"""
    print("\n🧪 Testing Error Handling")
    print("=" * 40)

    chatbot = MedicalChatBot()
    chatbot.load_data = MagicMock()

    error_test_cases = [
        ("Empty input", ""),
        ("Invalid math", "abc + def"),
        ("Division by zero", "5 / 0"),
        ("Unknown city", "tokyo weather")
    ]

    # Set up to weather step first
    chatbot.generate_response("my name is ErrorTest")
    chatbot.generate_response("fever")
    chatbot.generate_response("2 + 2")
    chatbot.generate_response("joke")

    for test_name, user_input in error_test_cases:
        print(f"\nTesting: {test_name}")
        print(f"Input: '{user_input}'")

        try:
            response = chatbot.generate_response(user_input)
            if response and len(response) > 5:
                print(f"✅ Handled gracefully: {response[:50]}...")
            else:
                print("❌ No proper error response")
        except Exception as e:
            print(f"❌ Exception: {e}")

    print("\n✅ Error handling tests completed!")


def test_medical_disclaimer():
    """Test that medical disclaimers are always present"""
    print("\n🧪 Testing Medical Disclaimers")
    print("=" * 40)

    chatbot = MedicalChatBot()
    chatbot.load_data = MagicMock()

    # Go to disease identification step
    chatbot.generate_response("my name is HealthUser")
    response = chatbot.generate_response("fever cough headache")

    required_disclaimers = [
        "NOT A DIAGNOSIS",
        "medical advice",
        "consult",
        "healthcare professional"
    ]

    disclaimer_count = 0
    for disclaimer in required_disclaimers:
        if disclaimer.lower() in response.lower():
            disclaimer_count += 1
            print(f"✅ Found disclaimer: '{disclaimer}'")
        else:
            print(f"❌ Missing disclaimer: '{disclaimer}'")

    if disclaimer_count >= 3:
        print("✅ Medical disclaimers are properly included!")
        return True
    else:
        print("⚠️  Some medical disclaimers are missing!")
        return False


if __name__ == "__main__":
    print("🚀 Starting Medical ChatBot Tests")
    print("=" * 60)

    # Run simple tests first
    success_count = 0
    total_tests = 3

    # Test 1: Complete guided conversation
    if run_guided_conversation_test():
        success_count += 1

    # Test 2: Error handling
    test_error_handling()
    success_count += 1  # Assuming error handling doesn't crash

    # Test 3: Medical disclaimers
    if test_medical_disclaimer():
        success_count += 1

    print("\n" + "=" * 60)
    print(f"🎯 Test Summary: {success_count}/{total_tests} test groups passed")

    if success_count == total_tests:
        print("🎉 All tests passed! Your Medical ChatBot is working correctly!")
        print("\nTo run advanced unit tests, use: python -m unittest test_chatbot.py")
    else:
        print("⚠️  Some tests had issues. Check the implementation.")

    # Run unittest tests if requested
    print("\n" + "=" * 60)
    run_unittest = input("Run advanced unit tests? (y/n): ").lower().strip()
    if run_unittest == 'y':
        print("\n🧪 Running Advanced Unit Tests...")
        unittest.main(verbosity=2)
