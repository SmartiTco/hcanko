import os
os.chdir("C:/Users/Stéphan Christian/Desktop")

with open("a_example.in", "r") as data:
    for line in range(1):
        int_number = data.readline()
        list_int_nbr = int_number.split()

        R = int(list_int_nbr[0])
        C = int(list_int_nbr[1])
        F = int(list_int_nbr[2])
        N = int(list_int_nbr[3])
        B = int(list_int_nbr[4])
        T = int(list_int_nbr[5])

    data_set = []
    données = data.readlines()
    for line in données:
        entier = line.split()
        data_set.append(entier)
    print (data_set)
