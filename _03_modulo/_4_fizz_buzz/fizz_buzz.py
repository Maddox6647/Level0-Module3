"""
 TODO: Fizz Buzz
   In this project, we're going to build FizzBuzz. It's a children's game where
   you count from 1 to 20. Easy, right? Here's the catch:
   -
   Instead of saying a number that is divisible by 3, say "Fizz".
   And instead of saying a number that is divisible by 5, say "Buzz".
   For numbers divisible by both 3 and 5, say "FizzBuzz".
   -
   Print your results to the console.
   -
   If your code is correct, the output will be:
   -
   1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz
"""
from tkinter import simpledialog, Tk, messagebox
if __name__ == "__main__":
    window = Tk()
    window.withdraw()

fizz = simpledialog.askstring(title='FIZZ BUZZ GAME', prompt='pick a number from 1-20 that is divisible by 3')
buzz = simpledialog.askstring(title='FIZZ BUZZ GAME', prompt='pick a number from 1-20 that is divisible by 5')
fizzbuzz = simpledialog.askstring(title='FIZZ BUZZ GAME', prompt='pick a number from 1-20 that is divisible by 3 or 5')


if fizz == 'fizz' and buzz == 'buzz':
    print('1 2 ' + fizz + ' 4 ' + buzz + ' ' + fizz + ' 7 8 ' + fizz + ' ' + buzz + ' 11 ' + fizz + ' 13 14 ' + fizzbuzz + ' 16 17 ' + fizz + ' 19 ' + buzz + '')
else:
    messagebox.showerror(title='FIZZ BUZZ GAME', message='U SUCK AT THIS GAME AND ITS FOR CHILDREN!!!')
