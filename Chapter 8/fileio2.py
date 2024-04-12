# function to check whether a word is in the file or not
def check_for_word():
    word ="learning"
    with open("file2.txt", "r") as f:
        data =f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Error")


#function to check in which line the first occurence of word exists
def check_for_line():
    word = "learning"
    data =True
    line_no =1
    with open("file2.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no +=1

    return -1

            

f =open("file2.txt", "r")
data =f.read()
new_data =data.replace("Python", "Java")
print(new_data)
    
with open("file2.txt", "w") as f:
    f.write(new_data)

check_for_word()
check_for_line()