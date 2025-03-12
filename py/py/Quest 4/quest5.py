li = ['2018-01-01', 'yandex', 'cpc', 100]
last = li[-1]
di = {}

for i in li[-2::-1]:
    di.clear()
    di[i] = last
    last = di.copy()
print(di)