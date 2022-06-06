import Pong.pong as pong

print("Hello friends.")
input("Let's play a few games!")

player1 = input("\nPlayer1, what's your name? > ")
print(f"Nice to meet you {player1}!")

player2 = input("\nPlayer2, what's your name? > ")
print("Nice to meet you too!")

print("\nI'll boot up pong for you and a friend.")
input("Booting... Press ENTER to commence!")

pong.game_loop()