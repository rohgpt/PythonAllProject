import time
import pyautogui
import tkinter as tk


def screen():

    time.sleep(5)
    name = int(
        time.time() * 1000
    )  # generate random imagename to avoid overwrite of image
    name = "./screenshotphoto/{}.png".format(name)
    print("ScreenShot Is in Your screenshotphoto folder with name = {}".format(name))
    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
root.title("screenshot Created by Rohitgupta")
root.geometry("1000x800")
frame = tk.Frame(root)
frame.pack()
buttom = tk.Button(frame, text="Click To take Screenshot", command=screen)
buttom.pack(side=tk.LEFT)
close = tk.Button(frame, text="Close", command=quit)
close.pack(side=tk.LEFT)
root.mainloop()
