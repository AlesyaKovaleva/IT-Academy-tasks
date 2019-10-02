import time
import operator

date = '01/06/1986'
try:
    valid_date = time.strptime(date, '%d/%m/%Y')
    print(valid_date)
    print(f'{valid_date[2]}.{valid_date[1]}.{valid_date[0]}')
except ValueError:
    print('Invalid date!')

