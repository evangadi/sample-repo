import random

# Step 1: Create a dictionary with U.S. states and their capitals
states_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

# Step 2: Initialize counters for correct and incorrect responses
correct_count = 0
incorrect_count = 0

# Step 3: Main quiz loop
while True:
    # Randomly select a state
    state = random.choice(list(states_capitals.keys()))
    # Ask the user to enter the capital
    user_answer = input(f"What is the capital of {state}? ").strip()

    # Check if the user's answer is correct
    if user_answer.lower() == states_capitals[state].lower():
        print("Correct!")
        correct_count += 1
    else:
        print(f"Incorrect. The capital of {state} is {states_capitals[state]}.")
        incorrect_count += 1

    # Optionally: Ask the user if they want to continue
    continue_quiz = input("Do you want to continue? (yes/no) ").strip().lower()
    if continue_quiz != 'yes':
        break

# Step 4: Print the final score
print(f"\nQuiz Over! You got {correct_count} correct and {incorrect_count} incorrect.")
