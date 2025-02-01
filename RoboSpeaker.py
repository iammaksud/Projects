import os

if __name__ == '__main__':
    print("Wlcm to RoboSpeaker")
    while True:
        x = input("Enter Here: ")
        if x =='quit':
            break
        command = f'spd-say "{x}"'
        os.system(command)