# Dictionary in Python

1. Dictionaries are used to store data values in  <b>key: value</b> pairs
2. They are unordered, mutable(changable) and don't allow duplicate keys<br>
 Eg:<br>
 dict = {<br>
    "name" : "Laxmi", <br>
    "cgpa" : 3.0, <br>
    "marks" : [60, 70, 80], <br>
 }<br><br>

 dict["name"], dict["cgpa"], dict["marks"]<br>
dict["key"] = "value" :- It assigns or adds new <br><br>
<b>Nested Dictionaries</b><br>
Eg:-<br>
student = {<br>
    "name" : "Shasi",<br>
    "score" {<br>
        "chem": 80,<br>
        "phy": 84,<br>
        "math": 95<br>
    }<br>
}<br><br>

student["score"]["math"]

# Dictionary Methods

1. myDict.key() :- it returns all keys.
2. myDict.values() :- It returns all values.
3. myDict.items() :- It returns all (key, value) pairs as tuple.
4. myDict.get("key") :-It returns the dkey according to value
5. myDict.update(newDict) :-It inserts the specified items to the dictionary

# Set in Python
<b>Set is the collection of the unordered items.</b><br>
<b>Each element in the set must be unique and immutable.</b><br>
Eg:<br>
nums ={1, 2, 3, 4}<br><br>
set2 ={1, 2, 2, 2} :-Repeated elements stored only once, so it resolved to {1, 2}<br>
null_set =set() :-Empty set syntax.<br>

# Set Methods

1. set.add(elementName):- It adds an element.
2. set.remove(elementName):- It removes the element form set
3. set.clear():- It empties the set
4. set.pop():- It removes a random value
5. set.union(set2):- It combines both set values and returns new.
6. Set.intersection(set2):- It combines common values in sets and returns new.
