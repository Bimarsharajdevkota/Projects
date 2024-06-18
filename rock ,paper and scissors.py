#It's a game of Rock,Paper and Scissors. (First player to score 3 points win.)

from getpass import getpass as input

def print_winner(player1, player2, winner):
    if winner == 'draw':
        print("It's a draw! Both {} and {} chose {}.".format(player1, player2, player1_choice))
    else:
        print("🎉 {} wins the round! 🎉 {} chose {}, and {} chose {}.".format(winner.capitalize(), player1, player1_choice, player2, player2_choice))

def get_player_choice(player_name):
    while True:
        choice = input("Enter your choice {}: ".format(player_name)).upper()
        if choice in ['R', 'P', 'S']:
            return choice
        else:
            print("Invalid choice! Please enter R for Rock, P for Paper, or S for Scissors.")

def play_round(player1, player2):
    player1_choice = get_player_choice(player1)
    player2_choice = get_player_choice(player2)

    if player1_choice == player2_choice:
        return 'draw', player1_choice, player2_choice

    if (player1_choice == 'R' and player2_choice == 'S') or \
       (player1_choice == 'P' and player2_choice == 'R') or \
       (player1_choice == 'S' and player2_choice == 'P'):
        return player1, player1_choice, player2_choice
    else:
        return player2, player1_choice, player2_choice

print("Welcome to the epic game of Rock✊, Paper✋, and Scissors✌️! First to 3 points wins.")
print()
player1 = input("Enter name of Player 1: ").capitalize()
player2 = input("Enter name of Player 2: ").capitalize()
print()

player1_points = 0
player2_points = 0

while True:
    winner, player1_choice, player2_choice = play_round(player1, player2)
    print_winner(player1, player2, winner)
    print()
    if winner != 'draw':
        if winner == player1:
            player1_points += 1
        else:
            player2_points += 1
        
        print("Score: {} - {} :{}".format(player1, player1_points, player2_points))
        print()
        
        if player1_points == 3:
            print("🎉 Congratulations, {} wins the game! 🎉".format(player1))
            break
        elif player2_points == 3:
            print("🎉 Congratulations, {} wins the game! 🎉".format(player2))
            break

    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")