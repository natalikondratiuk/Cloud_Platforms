from app import get_next_day
import random

def index_day() :
    i = random.randint(0, 9)
    try :
        get_next_day(i)
    except IndexError:
        print('Index is out of range: expected indexes in range 0...6')
