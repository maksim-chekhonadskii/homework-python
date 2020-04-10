def sal():
    try:
        time = float(input('Выработка (в часах) - '))
        salary = int(input('Ставка (у.е.) - '))
        bonus = int(input('Месячная премия (у.е.) - '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника - {res}')
    except ValueError:
        return print('Not a number')
sal()