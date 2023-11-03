"""
Description:
Author:
Date:
Usage:
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account,get_amount, get_balance, make_deposit
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
        # Assert
            with self.assertRaises(Exception) as context:
             get_account()
            
            self.assertEqual(str(context.exception), expected_output) 
        
    ""
    def test_valid_amount(self):
        # Arrange
        expected_output = "500.1"
        #Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["500.1"]    
        #Assert
        result = mock_input()
       
        self.assertEqual(result,expected_output)
    
    def test_non_numeric_amount(self):
        #Arrange
        expected_output = "Invalid amount. Amount must be numeric."
        #Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]
        #Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            
            self.assertEqual(str(context.exception), expected_output)

    def test_zero_or_negative(self):
        #Arrange
        expected_output = "Invalid amount. Please enter a positive number."
        #Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["0"]
        #Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            
            self.assertEqual(str(context.exception), expected_output)

    def test_correct_balance(self):
        #Arrange
        account = 123456
        expected_output = f"Your current balance for account {account} and $1,000.00."
        #Act
        ACCOUNTS[account]["balance"] = 1000.0
        actual_output = get_balance(account)
        #Assert
        assert actual_output == expected_output
        

    def test_balance_exception(self):
        #Arrange
        expected_output = "Account number does not exist."
        #Act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["112233"]
        #Assert
        with self.assertRaises(Exception) as context:
            get_balance(mock_input)
        self.assertEqual(str(context.exception), expected_output)
        
    def test_deposit_correctly_updated(self):
        #Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        #Act
        make_deposit(account_number,1500.01)
        #Assert
        assert ACCOUNTS[account_number]["balance"] == 2500.01 
        
    def test_deposit_correctly_returned(self):
        #Arrange
        account_number = 123456
        amount = 1500.01
        ACCOUNTS[account_number]["balance"] = 1000.0
        expected_output = f"You have made a deposit of $2,500.01 to account {account_number}."
        #Act
        make_deposit(account_number,amount)
        #Assert
        assert make_deposit(account_number, amount) == expected_output
        
    def test_deposit_exception_account_does_not_exist(self):
        #Arrange
        account_number = 112233
        amount = 1500.01
        expected_output = "Account number does not exist."
        #Act
        with self.assertRaises(Exception) as context:
            get_amount(make_deposit(account_number,amount))
        #Assert
        self.assertEqual(str(context.exception), expected_output)
        
    def test_deposit_exception_less_than_zero(self):
        #Arrange
        account_number= 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        expected_output = "Invalid Amount. Amount must be positive."
        #Act
        with self.assertRaises(ValueError) as context:
            get_amount(make_deposit(account_number,-50.01))
        #Assert
        self.assertEqual(str(context.exception), expected_output)
        
    
        

        

    