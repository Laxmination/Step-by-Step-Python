# Lists in Python
A built-in data type that stores set of values.<br> It can store elements of different types (integer, float, string, etc.)
<br>
Eg:<br>
marks = [87, 64, 33, 95, 76]<br>

student = [”Karan”, 85,“Delhi”]<br>

student[0] ="Karan"<br>


len(student) :- It returns length

# List Slicing
Accessing parts of a List.<br>
list_name[starting_idx:ending_idx] <br>
Eg: <br>
marks=[87, 64, 48, 11, 36, 88]<br>
marks[1:4] is [64, 48, 11]<br>
marks[ :4] is same as marks[0:4]<br>
marks[1: ] is same as marks[1:len(marks)]<br>
marks[-3:-1] is [11, 36]

# List Methods

list = [2, 1, 3]<br>
1. list.append(4) :- It adds one element at the end [2, 1, 3, 4]<br>
2. list.sort() :- It sorts in ascending order [1, 2, 3]<br>
3. list.sort(reverse =True) :- It sorts in descending order [3, 2, 1]<br>
4. list.reverse() :- It reverses list [3, 1, 2]<br>
5. list.insert(idx, element) :- It inserts element at index<br>
list1 = [2, 1,3, 1]<br>
6. list.remove(1) :- It removes first occurrence of element [2, 3, 1]<br>
7. list.pop(idx) :- It removes element at index

# Tuples in Python
<b>A built-in datatype that lets us create immutable (not changeble) sequences of valuse.</b><br><br>

tup = (87, 64, 33, 95,76) :-tup[1], tup[2] etc.<br> 
tup[0] = 43 is not allowed i.e. We cannot change the value of tuple.<br>
1. tup1 =() is valid tuple<br>
2. tup2 =(1,) is valid tuple but tup2 =(1) is invalid tuple because when we give such type of data the python understands it as an integer only.<br>
3. tup3 =(1, 2, 3) is valid tuple.

# Tuple Methods

tup =(2, 1, 3, 1)<br>
1. tup.index(element) :- It returns index of first occurence. i.e. tup.index(1) is 1 <br>
2. tup.count(element) :- It counts total occurences i.e. tup.count(1) is 2