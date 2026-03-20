# Name: Ariana Fafach
# Date: 3/19/2026
# Title: Program #3: Capital Quiz


# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).



import random

# Make dictionary of US states and Capitals:
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Initialize total scores:
Correct_Answers = 0
Incorrect_Answers = 0

# Quiz function chooses a random state from the dictionary and finds its capital:
def quiz():
    # Choose random state:
    state = random.choice(list(capitals.keys()))
    # Find that state's capital
    capital = capitals.get(state, None)
    
    return capital, state

# Check_answer function checks if the user's answer was correct and keeps track of a correct or incorrect answer:
def check_answer(capital):

    # Initialize scores for current run:
    correct_answers = 0
    incorrect_answers = 0

    # Check if user's answer is correct. If it is, tell the user and set the correct_answers variable to 1
    if answer == capital:
        print("Your answer is correct!")
        correct_answers += 1
    # Check if user's answer is incorrect. If it is, tell the user the correct answer and set the incorrect_answers variable to 1
    elif answer != capital:
        print(f"Your answer is incorrect. The correct answer is {capital}.")
        incorrect_answers += 1

    return correct_answers, incorrect_answers

# Start program
again = 'yes'
# Program runs as long as the user keeps typing 'yes'.
while again == 'yes':
    # Call quiz function
    capital, state = quiz()
    # Get the user's answer:
    answer = input(f"Enter the capital of {state}:  ")
    # Call check_answer function:
    correct_answers, incorrect_answers = check_answer(capital)
    # Ask the user if they want to try again:
    again = input("Would you like to try again? Enter y for 'yes' and n for 'no':  ")

    # Keep track of the total score:
    if correct_answers == 1:
        Correct_Answers += 1
    
    elif incorrect_answers == 1:
        Incorrect_Answers += 1

# Print results:
print (f"{Correct_Answers} of your answers were correct.")
print (f"{Incorrect_Answers} of your answers were incorrect.")
