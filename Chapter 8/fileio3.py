# to count even numbers from the file containing numbers seperated by comma

count =0
with open("sample2.txt", "r") as f:
    data =f.read()
  
    # numb =""
    # for i in range(len(data)):
    #     if (data[i] == ","):
    #         print(int(numb))
    #         numb =""
    #     else:
    #         numb +=data[i]


    numb = data.split(",")
    for val in numb:
        if(int(val) %2 ==0):
            count +=1

print(count)
