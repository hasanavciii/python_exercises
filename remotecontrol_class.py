import random
import time

class RemoteControl():
    def __init__(self, tv_status="off", tv_volume=0, channel_list=["trt"], channel="trt"):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel

    def turn_on_tv(self):
        if self.tv_status == "on":
            print("The TV is already on...")
        else:
            print("Turning on the TV")
            self.tv_status = "on"

    def turn_off_tv(self):
        if self.tv_status == "off":
            print("The TV is already off")
        else:
            print("Turning off the TV")
            self.tv_status = "off"

    def adjust_volume(self):
        while True:
            response = input("Decrease volume: '<'\nIncrease volume: '>'\nExit: 'exit'")
            
            if response == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print("TV volume:", self.tv_volume)
            elif response == ">":
                if self.tv_volume != 31:
                    self.tv_volume += 1
                    print("TV volume:", self.tv_volume)
            elif response == "exit":
                print("Volume updated:", self.tv_volume)
                break

    def add_channel(self, new_channel):
        print("Adding a new channel...")
        time.sleep(1)
        self.channel_list.append(new_channel)
        print("New channel added")

    def random_channel(self):
        random_index = random.randint(0, len(self.channel_list)-1)
        self.channel = self.channel_list[random_index]
        print("Current channel:", self.channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "TV status: {}\nTV volume: {}\nChannel list: {}\nCurrent channel: {}".format(
            self.tv_status, self.tv_volume, self.channel_list, self.channel
        )

remote_control = RemoteControl()

print("""

TV Application

1. Turn on TV
2. Turn off TV
3. Adjust volume
4. Add channel
5. Get channel count
6. Switch to a random channel
7. TV information

Press 'q' to exit
""")

while True:
    operation = input("Please select an operation: ")

    if operation == "q":
        print("Program is ending")
        break
    elif operation == "1":
        remote_control.turn_on_tv()
    elif operation == "2":
        remote_control.turn_off_tv()
    elif operation == "3":
        remote_control.adjust_volume()
    elif operation == "4":
        channel_names = input("Enter channel names separated by commas: ")
        channel_list = channel_names.split(",")
        
        for new_channel in channel_list:
            remote_control.add_channel(new_channel)
    elif operation == "5":
        print("Channel count:", len(remote_control))
    elif operation == "6":
        remote_control.random_channel()
    elif operation == "7":
        print(remote_control)
    else:
        print("Invalid operation")

