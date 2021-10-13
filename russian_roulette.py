import random
import time
import webbrowser


random.seed(time.time())
dies = [True] + [False] * 5
random.shuffle(dies)


if dies.pop() is True:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
