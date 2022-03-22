import pandas as pd
import json
d = []

xl = pd.read_excel('data2.xlsx')

def color(color):
    if color == 'Офисный центр':
        return 'pin_cooper'
    elif color == 'Гостиница':
        return 'pin_grey'
    elif color == 'Здания госучреждений и госкомпаний':
        return 'pin_gold'
    elif color == 'Религиозные учреждения':
        return 'pin_blue'
    elif color == 'Культурные и досуговые учреждения':
        return 'pin_blue'
    elif color == 'Медицинские учреждения':
        return 'pin_blue'
    elif color == 'ВУЗ':
        return 'pin_blue'
    elif color == 'Автобус':
        return 'pin_bus'
    elif color == 'Трамвай':
        return 'pin_tram'

def type_point(point):
    if point in ['Автобус','Трамвай']:
        return 'metro'
    else:
        return 'environment'

for i in range(66):
    d.append({'type': 'Feature',
     'properties':{'type': type_point(xl.iloc[i][1]),'icon': color(xl.iloc[i][1]),'title': xl.iloc[i][3]},
     'geometry':{'type': 'Point','coordinates': [xl.iloc[i][6], xl.iloc[i][5]]},
})

jsonstr = json.dumps(d)

print(jsonstr)
