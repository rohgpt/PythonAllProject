import string
import random
import tkinter as tk


def gen():
    s1 = string.ascii_uppercase  # generate all upper case letter
    s2 = string.ascii_lowercase
    l1 = list(s1)
    l2 = list(s2)
    l3 = list(string.digits + string.punctuation)
    l1.extend(l2 + l3)
    e.delete(0, tk.END)
    random.shuffle(l1)

    print("".join(l1[:9]))
    e.insert(tk.INSERT, "".join(l1[:9]))


root = tk.Tk()
root.title("Password Generator Created by Rohitgupta")
root.geometry("1000x800")
p1 = tk.PhotoImage(file="screenshotphoto/1594588415381.png")
root.iconphoto(False, "screenshotphoto/1594588415381.png")
frame = tk.Frame(root)
frame.pack()
Run = tk.Button(
    root, text="Run", bg="black", fg="yellow", width=15, height=2, command=gen
)
e = tk.Entry(root)

e.pack(side=tk.TOP)
Run.pack(side=tk.TOP)

root.mainloop()
