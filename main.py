import random;

while True:
    slots = ["rock", "paper", "scissor"];
    computer = random.choice(slots);
    me = input("You: ");

    if me == "rock" and computer == "paper":
        print("You Failed");

    elif me == "paper" and computer == "scissor":
        print("You Failed");

    elif me == "scissor" and computer == "rock":
        print("You Failed");

    elif me == "paper" and computer == "rock":
        print("You Failed");

    elif me == "scissor" and computer == "paper":
        print("You win!");

    elif me == "rock" and computer == "scissor":
        print("You win!");

    elif me == "paper" and computer == "rock":
        print("You win!");
    
    elif me == computer:
        print("Draw match!!!");

    elif me == "exit":
        break;

    else:
        print("Error: There are this 'rock', 'paper', 'scissor', 'exit'");
