"""
Description:
Author:
Date:
Usage:
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account
from src.chatbot import VALID_TASKS, ACCOUNTS

class ChatbotTests(unittest.TestCase):
    def test_valid_account(self):
        #Arrange
        expected_output = 123456
        #Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["123456"]    
        #Assert
        self.assertEqual(int(mock_input()),expected_output)
    
    def test_non_numeric_data(self):
        #Arrange
        expected_output = "Account number must be a whole number."
        #Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]
        #Assert
        with self.assertRaises(Exception) as context:
            get_account()
            
        self.assertEqual(str(context.exception), expected_output)
    
    def test_account_nonexist(self):
        #Arrange
        expected_output = "Account number entered does not exist."
        #Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["112233"]
        result = mock_input()
        # Assert
        with self.assertRaises(Exception) as context:
            get_account()
            
        self.assertEqual(str(context.exception), expected_output) 
    