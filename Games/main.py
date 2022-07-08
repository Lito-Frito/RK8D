# -*- coding: utf-8 -*-

# Import games
import Pong.pong as pong

# Greet players
print("Hello friends.")
welcome = input("Let's play a few games!")

# Ensure that players can't pick too long a name
player_a_too_long = True

while player_a_too_long:

    playerA = input("\nPlayerA, what's your name? > ")
    if len(playerA) > 12:
        print("Unfortunately, that's too long for me to display...can you choose another name?")
    
    else:
        greeting_a = input(f"Nice to meet you {playerA}!")
        player_a_too_long = False


player_b_too_long = True

while player_b_too_long:
    playerB = input("\nPlayerB, what's your name? > ")
    if len(playerB) > 12:
        print("Unfortunately, that's too long for me to display...can you choose another name?")

    else:
        greeting_b = input(f"Nice to meet you {playerB}!")
        player_b_too_long = False
    

# Start the game
boot = input("\nI'll boot up pong for you both.")

instructions = input(f"\n{playerA}, you use W & S to move your paddle."
                     f"\n{playerB}, use the UP and DOWN arrows to move your paddle."
                      "\nFirst to 5 points wins!")

start_game = input("\nBooting... Press ENTER to commence!")

pong.game_loop(playerA, playerB)