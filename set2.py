#Figure out a way to store 9 & 9.0 as separate values in the set.

# set1 ={"9", "9.0"}
# print(set1)

set1 ={
    ("Float", 9.0),
    ("int", 9)
}
print(set1)