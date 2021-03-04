import shelve

# with shelve.open('data') as shelf:
# 	shelf['key'] = {'int': 9, 'name': 'Вирусный конъюнктивит', 'type': 'патология', 'change': 'не изменяется', 'w|w/o': 'без рубцов', 'type_2': 'инфекция'}
# 	shelf['key1'] = {'int': 10, 'name': 'Трахома', 'type': 'патология', 'change': 'не изменяется', 'w|w/o': 'с рубцами', 'type_2': 'инфекция'}

with shelve.open('data') as shelf:
	print(shelf['key1'])