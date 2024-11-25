"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:


def get_account() -> int:
    """

    Description: Get the user to input their account number
    Parameter: None
    Return Description: Returns the users valid account number parsed as an integer
    Exceptions: Raises a ValueError if the account number is not a whole number. 
                Raises an Exception is the account number does not exist
    """

    account_number = input("Please enter your account number: ")
    try:
        account_number = int(account_number)
    except Exception:
        raise ValueError("Account number must be a whole number.")
    if account_number not in ACCOUNTS:
        raise Exception("Account number entered does not exist.")
    return account_number
        
def get_amount() -> float:
    """
    Description: Get the user to input their transaction amount
    Parameter: None
    Return Description: Returns the users valid transaction as a float
    Exceptions: Raises a ValueError if the transaction number is not numeric. 
                Raises a ValueError if the transaction number is 0 or less then 0 (negative)
    """
    user_amount = input("Enter the transaction amount: ")
    try:
        user_amount = int(user_amount)
    except Exception:
        raise ValueError("Invalid amount. Amount must be numeric.")
    if user_amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    return user_amount

def get_balance(account: int) -> str:
    """
    Description: Retrieve balance of a specified account
    Parameter: Account number
    Return Description: Returns a string which displays the account number and it's balance
    Exceptions: Raises an Exception if the account number does not exist   
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    balance = ACCOUNTS[account]["balance"]
    return f"Your current balance for account {account} and ${balance:,.2f}."
    
def make_deposit(account: int, amount: float) -> str:
    """
    Description: Make a deposit into the valid account 
    Parameter: Account number, transaction amount
    Return Description: Returns the a string which shows the deposit amount and the account related
    Exceptions: Raises a ValueError if the amount is not a positive 
    """
    
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    balance = ACCOUNTS[account]["balance"]
    ACCOUNTS[account]["balance"] = balance + amount
    
    return f"You have made a deposit of ${balance:,.2f} to account {account}."

def user_selection()->str:
    """
    Description: Ask the user to select a tast
    Parameter: None
    Return Description: Returns the users valid tasks selection
    Exceptions: Raises an Exception if the user inputs an invalid task
    """
    user_input = input("What would you like to do (balance/deposit/exit)? ")
    user_input = user_input.lower()
    if user_input not in VALID_TASKS:
        raise Exception("Invalid task. Please choose balance, deposit, or exit.")
    return user_input

## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION

def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:
            selection = user_selection()
            
            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:
                        account = get_account()

                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULT
                        print(get_balance(account))

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:
                            amount = get_amount()


                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                    ## VARIABLES account AND amount DEFINED ABOVE AND 
                    ## PRINT THE RESULTS:
                    print(make_deposit(account,amount))


            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")

    

if __name__ == "__main__":
    chatbot()
