import os
os.chdir("C:/Users/Stéphan Christian/Desktop")

data = []
with open("a_example.in", "r") as données_sujet:
        i = 0
        for line in données_sujet:
            row = []
            for lettre in line:
                row.append(lettre)
            n = len(row)
            del (row[n-1])
            data.append(row)
            i += 1
x=0
while x < i:
    print(data[x])
    x += 1
