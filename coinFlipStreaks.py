import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    seq = ['heads', 'tails']
    hot_l = []
    for i in range(101):
        hot_l.append(random.choice(seq))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    h_streak = 0
    t_streak = 0
    yes_streak = 0 
    for j in hot_l:
        if j == 'heads':
            t_streak = 0
            h_streak += 1
            if h_streak == 6:
                yes_streak += 1
        else: # j == 'tails'
            h_streak = 0
            t_streak += 1
            if t_streak == 6:
                yes_streak += 1
    if yes_streak >= 1:
        numberOfStreaks += 1 # If we got 6 heads or 6 tails in a row, we got a streak during our 100 coin flips
    
print('The chance of a streak is: {}'.format(str(round((numberOfStreaks/10000)*100,2)) + '%'))
