from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

if __name__ == "__main__":
    window = Tk()
    window.withdraw()

    poppy_playtime = simpledialog.askstring(title='f', prompt='enter someone from Poppy Playtime')
    rainbow_friends = simpledialog.askstring(title='g', prompt='enter someone from Rainbow Friends')
    creepypasta = simpledialog.askstring(title='h', prompt='enter someone who is a creepypasta character')
    famous_celebrity = simpledialog.askstring(title='n', prompt='enter a famous celebrity, such as an actress, actor, singer, sports player, dancer, etc')
    sus_stuff = simpledialog.askstring(title='asdgh', prompt='enter something sus')
    messagebox.showinfo(title='jg', message="bobby is a chungus who loves " + poppy_playtime + "."
    "He has no friends, so he slapped " + rainbow_friends + ". He had to go go home, so he slapped " + poppy_playtime + "."
    " Soon, he went to a concert and saw " + famous_celebrity + ". He decided to be best friends with " + famous_celebrity + ". Sadly, he saw " + creepypasta +", who scared him to death."
    "He did not know what to do, so he ran away and crashed into " + rainbow_friends +". This was very bad, so he and " + famous_celebrity +" ran inside Bobby's house and went inside the bedroom."
    "He and " + famous_celebrity +" " + sus_stuff + " and  did it for hours and hours and hours. Then, " + creepypasta + " appears out of the shadows and destroys " + famous_celebrity +". Bobby gets super mad."
    "Bobby wanted to destroy everything. he grabs an AK-47 and blasts himself. Bobby was dead and was never seen again")
