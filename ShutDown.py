from pynput.mouse import Button, Controller
import time

mouse = Controller()
mouse.position = (403, 837)
mouse.click(Button.left, 1)
time.sleep(1)
mouse.position = (1018, 770)
time.sleep(1)
mouse.click(Button.left, 1)
mouse.position = (1017, 701)
time.sleep(1)
mouse.click(Button.left, 1)
time.sleep(1)
mouse.click(Button.left, 1)
while True:
    print(mouse.position)