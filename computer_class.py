import time
import math

class Computer():
    def __init__(self, computer_status="on", files=["cv", "documents", "papers"], games=["pokemon"]):
        self.computer_status = computer_status
        self.files = files
        self.games = games

    def turn_on(self):
        if self.computer_status == "on":
            print("The computer is already on.")
        else:
            self.computer_status = "on"
            print("Turning on the computer.")

    def turn_off(self):
        if self.computer_status == "off":
            print("The computer is already off.")
        else:
            self.computer_status = "off"
            print("Turning off the computer.")

    def add_file(self, file_name):
        print("Adding file...")
        time.sleep(1)
        self.files.append(file_name)

    def add_game(self, game_name):
        print("Adding game...")
        time.sleep(1)
        self.games.append(game_name)

    def __str__(self):
        return "Computer Status: {}\nFiles: {}\nGames: {}".format(self.computer_status, self.files, self.games)

computer = Computer()

print("""
    
1. Turn on the computer
2. Turn off the computer
3. Add a file
4. Add a game
5. Show information
    
Press 'q' to quit.
    
""")

while True:
    choice = input("Please select an action: ")

    if choice == "q":
        print("Exiting...")
        break
    elif choice == "1":
        computer.turn_on()
    elif choice == "2":
        computer.turn_off()
    elif choice == "3":
        file_names = input("Please enter file names separated by commas: ")
        files = file_names.split(",")

        for file in files:
            computer.add_file(file)
    elif choice == "4":
        game_names = input("Please enter game names separated by commas: ")
        games = game_names.split(",")

        for game in games:
            computer.add_game(game)
    elif choice == "5":
        print(computer)
