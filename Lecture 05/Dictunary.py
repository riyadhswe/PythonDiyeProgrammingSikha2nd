lines = ["A","B","C","D"]

with open("file.txt","w") as fb:
    for line in lines:
        fb.write(line+"\n")