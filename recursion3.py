def print_list(list, idx =0):
    if(idx ==len(list)):
        return None
    print(list[idx])
    print_list(list, idx +1)

fruits =["Mango", "banana", "litchi", "orange", "Apple"]

print_list(fruits)