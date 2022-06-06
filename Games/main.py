# -*- coding: utf-8 -*-
import Pong.pong as pong

print("Hello friends.")
input("Let's play a few games!")

player_a_too_long = True

while player_a_too_long:

    playerA = input("\nPlayerA, what's your name? > ")
    if len(playerA) > 12:
        print("Unfortunately, that's too long to display...can you choose another name?")
    
    else:
        print(f"Nice to meet you {playerA}!")
        player_a_too_long = False


player_b_too_long = True

while player_b_too_long:
    playerB = input("\nPlayerB, what's your name? > ")
    if len(playerB) > 12:
        print("Unfortunately, that's too long to display...can you choose another name?")

    else:
        print(f"Nice to meet you {playerA}!")
        player_b_too_long = False
    

print("\nI'll boot up pong for you and a friend.")
input("Booting... Press ENTER to commence!")

pong.game_loop(playerA, playerB)