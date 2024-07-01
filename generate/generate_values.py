import random


def two_options_value(percentage):
    if random.random() < (percentage / 100):
        return 1
    else:
        return 0


def three_option_value(percentage_1, percentage_2, percentage_3):
    if (percentage_1 + percentage_2 + percentage_3) == 100:
        index = random.random()
        
        if index < (percentage_1 / 100):
            return 0 
        elif (percentage_1 / 100) <= index <= ((percentage_1 + percentage_2) / 100):
            return 1 
        else:
            return 2 


def generate_ranged_value(min_value, max_value, limit_value, percentage):
    index = random.random()
    
    if index < (percentage / 100):
        return random.randint(limit_value, max_value)
    else:
        return random.randint(min_value, limit_value - 1)


















