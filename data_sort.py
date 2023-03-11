from data import data

def data_sort(data):
    new_data = {}
    for i in data:
        user, item, count = i.split(',')
        print(user, item, count)
        new_data[user] = {item: count}
        print(new_data)

print(data)
data_sort(data)