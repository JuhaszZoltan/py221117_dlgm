spd_lmt:int = int(input('maximálisan megengedett sebesség (kmph): '))
if spd_lmt > 50 or spd_lmt < 5:
    print(f'HIBA: ez a program csak [5;50] kmph limit között tudja meghatározni a bírságot!')
else:
    act_spd:int = int(input('tényleges sebesség (kmph): '))
    if act_spd < 0: print('HIBA: a negatív haladási sebesség nem lehetséges!')
    elif act_spd <= spd_lmt: print('Nem haladtad meg a sebességkorlátozást, nincs büntetés.')
    else:
        exceed:int = act_spd - spd_lmt
        if exceed <= 15:
            print('A sebességtúllépés még tűréshatáron belül van, nincs bírság, de légy óvatosabb!')
        else:
            if   exceed <= 25: fine:int =  30000
            elif exceed <= 35: fine:int =  45000
            elif exceed <= 45: fine:int =  60000
            elif exceed <= 55: fine:int =  90000
            elif exceed <= 65: fine:int = 130000
            elif exceed <= 75: fine:int = 200000
            else:              fine:int = 300000
            print(f'A megengedett sebességet {exceed} kmph-val haladtad meg,', end=' ')
            print(f'a kiszabott bírság összege: {fine} HUF')