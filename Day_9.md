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