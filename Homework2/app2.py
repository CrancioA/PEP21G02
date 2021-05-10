# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print the difference between them in the
# received format dd:hh:mm:ss
# dd is number of days
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)

# datele introduse trebuie sa contina doua zecimale altfel va da eroare
text1 = input("Get time1: ")
text2 = input("Get time2: ")

dd1 = int(text1[0:2])
dd2 = int(text2[0:2])
hh1 = int(text1[3:5])
hh2 = int(text2[3:5])
mm1 = int(text1[6:8])
mm2 = int(text2[6:8])
ss1 = int(text1[9:11])
ss2 = int(text2[9:11])

#am pus conditia ca ziua sa fie intre 1 si 31 asemenea zilelor dintr-o luna normala
if dd1 >= dd2 and (((dd1 >= 1) and (dd1 <= 31)) and ((dd2 >= 1) and (dd2 <= 31))): #am pus conditia ca dd1 > dd2 ca sa nu dea ziua cu minus. Se poate scoate aceasta conditie
    if ((hh1 >= 0) and (hh1 <= 23)) and ((hh2 >= 0) and (hh2 <= 23)):
        if ((mm1 >= 0) and (mm1 <= 59)) and ((mm2 >= 0) and (mm2 <= 59)):
            if ((ss1 >= 0) and (ss1 <= 59)) and ((ss2 >= 0) and (ss2 <= 59)):
                dif_d = dd1 - dd2
                dif_h = abs(hh1 - hh2)
                dif_min = abs(mm1 - mm2)
                dif_sec = abs(ss1 - ss2)
                print("The time difference is: ", dif_d, ':', dif_h, ':', dif_min, ':', dif_sec, sep='')
            else:
                print("Wrong seconds format entered!")
        else:
            print("Wrong minutes format entered!")
    else:
        print("Wrong hours format entered!")
else:
    print("Wrong days format entered!")



