from Cloud_Platforms.app import get_next_day
import random

def index_day() :
    i = random.randint(0, 9)
    if i >= 0 and i <= 6: get_next_day(i)
    else: print('Index is out of range: expected indexes in range 0...6')
