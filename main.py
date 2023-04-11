from pynput import keyboard

# define a callback function to handle key presses
def on_press(key):
    try:
        print('Key {} pressed.'.format(key))
    except AttributeError:
        print('A special key {0} pressed.'.format(key))

# define a listener object that will wait for keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
