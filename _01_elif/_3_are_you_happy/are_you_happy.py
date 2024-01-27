from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    w = Tk()
    w.withdraw()
    happy = simpledialog.askstring(title='f', prompt='are you happy?')
    if happy == 'yes':
        messagebox.showinfo(title='l', message='keep doing whatever you are doing')
    elif happy == 'no':
        happy2 = simpledialog.askstring(title='w', prompt='do you want to be happy?')
        if happy2 == 'no':
            messagebox.showinfo(title='q', message='keep doing whatever you are doing')
        elif happy2 == 'yes':
            messagebox.showinfo(title='x', message='change something')
