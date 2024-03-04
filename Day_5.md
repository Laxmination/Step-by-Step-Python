# Conditional Statements
if-elif-else (SYNTAX)
<br><br>
if(condition):
<br>
Statement1
<br>
elif(condition):
<br>
Statement2
<br>
else:
<br>
statementN
<br><br>
<b>Single line If/ Ternary Operator</b><br>
var =val1 if  condition  else val2 <br>
Eg:<br>
food = input("Food: ")<br>
eat = "Yes" if food == "Cake" else "No"<br>
print(Eat)

# Strings
 String is data type that stores a sequence of characters.<br>
 1. <b>concatenation:</b> "Hello" + "World" -> "HelloWorld"<br>
 2. <b>Lengt of string:</b> len(str)
 3. <b>Indexing:</b><br>str ="Laxmi_Kathayat" <br> str[0] is 'L', str[1] is 'a'....<br>
 str[0] = 'B'
 4. <b>Slicing:</b> Accessing parts of a string.<br>
 str[starting_idx:ending_idx]<br>
 str ="LaxmiKathayat" <br>
 str[1:4] is "axm" <br>
 str[ :4] is same as str[0:4] <br>
 str[1: ] is same as str[1: len(str)]<br>
 str[-3:-1] is "ya"<br>