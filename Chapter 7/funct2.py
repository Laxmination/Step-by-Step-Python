# WAF to print the elements of a list in a single line. (list in the parameter)
cities =["Kathmandu", "Pokhara", "Birgunj", "Dhangadi", "Dharan", "Biratnagar"]
heros =["Rajesh Hamal", "Nikhil Upreti", "Biraj Bhatta", "Dayahang Rai"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
