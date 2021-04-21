"""
Get from input: 23:30:31
Get from input: 23:31:31

find difference between the 2 inputs in seconds
"""
text1 = input("Get time1: ")
text2 = input("Get time2: ")

h1 = int(text1[0:2])
h2 = int(text2[0:2])
min1 = int(text1[3:5])
sec1 = int(text1[6:8])
min2 = int(text2[3:5])
sec2 = int(text2[6:8])

t1 = 3600*h1+60*min1+sec1
t2 = 3600*h2+60*min2+sec2
print(t2-t1)


