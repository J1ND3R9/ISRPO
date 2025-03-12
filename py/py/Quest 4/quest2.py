ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
unique_ids = []
for item in ids.items():
    for i in item[1]:
        if i not in unique_ids:
            unique_ids.append(i)
print(unique_ids)