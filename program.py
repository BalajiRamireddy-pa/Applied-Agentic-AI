# 1.RockPaper Scissor Game

import random

def rock_paper_scissors():

    choices = ["rock", "paper", "scissors"]

    win = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    while True:
        total_games = int(input("Enter number of games to play (1-3): "))
        if 1 <= total_games <= 3:
            break
        print("Please enter a number between 1 and 3.")

    player_score = 0
    computer_score = 0

    for game in range(1, total_games + 1):
        print(f"\n----- Game {game} -----")

        player = input("Enter your choice (rock, paper, scissors): ").lower()

        if player not in choices:
            print("Invalid Choice!")
            continue

        computer = random.choice(choices)

        print("Player 1:", player)
        print("Player 2:", computer)

        if player == computer:
            print("Result: Tie")

        elif win[player] == computer:
            print("Result: Player 1 Won")
            player_score += 1

        else:
            print("Result: Player 2 Won")
            computer_score += 1

        print(f"Score -> Player 1: {player_score} | Player 2: {computer_score}")

        if total_games == 3:
            if player_score == 2:
                print("\nPlayer 1 Wins the Series!")
                break
            elif computer_score == 2:
                print("\nPlayer 2 Wins the Series!")
                break

    print("\n===== Final Result =====")
    print("Player 1 Score:", player_score)
    print("Player 2 Score:", computer_score)

    if player_score > computer_score:
        print("Final Winner: Player 1")
    elif computer_score > player_score:
        print("Final Winner: Player 2")
    elif player_score == computer_score:
        print("Series Draw")
    else:
        print("Invalid Game")




# 2.Story Generator 

def story():

    when = [
        "Yesterday",
        "Last week",
        "One morning",
        "Last Sunday",
        "A few days ago"
    ]

    who = [
        "a scientist",
        "a teacher",
        "a little boy",
        "a police officer",
        "an astronaut"
    ]

    where = [
        "in a forest",
        "at the beach",
        "in a school",
        "on Mars",
        "in a village"
    ]

    what = [
        "found a treasure",
        "rescued a puppy",
        "invented a robot",
        "discovered a secret cave",
        "won a competition"
    ]

    how = [
        "using intelligence",
        "with the help of friends",
        "by working hard",
        "with great courage",
        "by never giving up"
    ]

    print("=" * 40)
    print("     RANDOM STORY GENERATOR")
    print("=" * 40)

    n = int(input("Enter number of stories: "))

    if n < 0:
        print("Please enter a positive number.")

    elif n == 0:
        print("Please enter a number greater than zero.")

    else:
        print("\nGenerated Stories:\n")

        for i in range(1, n + 1):
            print("Story", i)
            print(
                random.choice(when),
                random.choice(who),
                random.choice(what),
                random.choice(where),
                random.choice(how) + "."
            )
            print()

        print("Thank You for Using Story Generator!")



# 3. Email Sender

'''
Step-1 : Setting up Gmail App Password
'''

import smtplib

def send_email():

    # Create SMTP server connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print(server)

    # Start TLS security
    server.starttls()

    # Login to Gmail
    server.login("jagadeeshboyalla3384@gmail.com", "YOUR_APP_PASSWORD")
    print("Login Successful")

    # Email message
    message = "Welcome to my World. This is an automated email."

    # Send email
    server.sendmail(
        "jagadeeshboyalla3384@gmail.com",
        "jagadeeshsrkr3384@gmail.com",
        message
    )

    print("Email Sent Successfully")

    # Close the server connection
    server.quit()

# Function Call



# bmi cal


def bmi_calculator():

    while True:
        try:
            print("\n========== BMI CALCULATOR ==========")

            sno = int(input("Enter S.No: "))
            name = input("Enter Name: ")
            weight = float(input("Enter Weight (kg): "))
            height = float(input("Enter Height (m): "))

            if height <= 0 or weight <= 0:
                print("Weight and Height must be greater than zero.")
                continue

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            print("\n========== BMI REPORT ==========")
            print("S.No      :", sno)
            print("Name      :", name)
            print("Weight    :", weight, "kg")
            print("Height    :", height, "m")
            print("BMI       :", round(bmi, 2))
            print("Category  :", category)
            print("=" * 32)

            break

        except ValueError:
            print("Invalid Input! Please enter valid numbers.")

        except ZeroDivisionError:
            print("Height cannot be zero.")