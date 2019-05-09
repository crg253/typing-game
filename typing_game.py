import string
import random
import time
from functools import wraps

'''
Typing Game gives you three random characters, numbers, or symbols, and asks you
to type the same thing. User gets one point for each correctly typed set.
'''

class ScoreBoard:
    def __init__(self):
        self.total_score = 0
        self.start_time = time.time()
    def increase_score(self):
        self.total_score += 1
    def calculate_speed(self):
        return round((time.time() - self.start_time)/self.total_score, 2)

def encouraging_message(user_scoreboard:object):
    print(f"Good Job! Score is {user_scoreboard.total_score}.",\
        f"Average Speed is {user_scoreboard.calculate_speed()} seconds per line.")
    return None

def update_score(user_scoreboard:object):
    user_scoreboard.increase_score()
    if user_scoreboard.total_score % 3 ==0:
        encouraging_message(user_scoreboard)
    return None

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
    my_score_board = ScoreBoard()
    while True:
        new_line = get_new_line()
        type_line(new_line)
        update_score(my_score_board)

if __name__ == "__main__":
    play_typing_game()
