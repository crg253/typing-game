import string
import random
import time
from functools import wraps

'''
Typing Game gives you three random characters, numbers, or symbols, and asks you
to type the same thing. User gets one point for each correctly typed set.
'''

class Score:
    score = 0
    start_time = time.time()
    ave_time = None
    def update_score(self):
        self.score += 1
        self.ave_time = round((time.time() - self.start_time)/self.score, 2)

def get_new_score(Score):
    Score.update_score(Score)
    return Score.score, Score.ave_time

def type_line(new_line):
    user_input=''
    while user_input != new_line:
        user_input = input(new_line+"\n")

def get_new_line():
    chars = string.ascii_letters+string.digits+string.punctuation
    return "".join(random.sample(chars, 3))

def until_quit(game):
    @wraps(game)
    def wrapper():
        try:
            game()
        except KeyboardInterrupt:
            pass
    return wrapper

@until_quit
def play_typing_game():
    while True:
        new_line = get_new_line()
        type_line(new_line)
        scores = get_new_score(Score)
        print(f"Good Job! Score is {scores[0]}. Average Time is {scores[1]}.")

if __name__ == "__main__":
    play_typing_game()
