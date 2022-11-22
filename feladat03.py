import random as r

score:int = 0
for n in range(8):
    x:int = r.randint(10, 99) if r.randint(0, 1) else r.randint(-99, -10)
    y:int = r.randint(10, 99) if r.randint(0, 1) else r.randint(-99, -10)
    pred_sum = int(input(f'{n+1}.) {x} + {y} = '))
    if pred_sum == x+y: score += 1
print(f'A válaszaid {round(score/8*100, 2)}%-ban voltak helyesek!')