from data_sort import data_sort, data

print(data)
data = data_sort(data)
print('------------------')
print(data)
print('------------------')
for i in data.keys():
    print(i, data[i], '\n' )

