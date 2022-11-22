import random as r

string:str = input('karakterlánc: ')
rng_num:int = r.randint(0, 9)
print(f'a generált szám: {rng_num}')
if rng_num % 2: print(rng_num * f'{string}\n')
else: print(rng_num * f'{string} ')