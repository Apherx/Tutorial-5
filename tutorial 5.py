T1MATH= int(input("What is your term 1 math result? :"))
T1PHY= int(input("What is your term 1 Physics result? :"))
T1AES= int(input("What is your term 1 AES result? :"))
T1CP= int(input("What is your term 1 cp result? :"))
T2MATH= int(input("What is your term 2 math result? :"))
T2PHY= int(input("What is your term 2 Physics result? :"))
T2CP= int(input("What is your term 2 cp result? :"))
T2AES= int(input("What is your term 2 AES result? :"))
T3MATH= int(input("What is your term 3 math result? :"))
T3CP= int(input("What is your term 3 cp result? :"))
T3PHY= int(input("What is your term 3 Physics result? :"))
T3AES= int(input("What is your term 3 AES result? :"))
TOTAL = (T1MATH + T1PHY + T1AES + T1CP + T2MATH + T2PHY + T2AES + T2CP + T3MATH + T3PHY + T3AES + T3CP)
if T1MATH < 0 or T1PHY < 0 or T1AES < 0 or T1CP < 0 or T2MATH<0 or T2AES<0 or T2CP<0 or T2PHY<0 or T3MATH<0 or T3AES<0 or T3CP<0 or T3PHY < 0:
    print("Wrong input")
    quit()
elif  T1MATH >= 40 and T1PHY >= 40 and T1AES >= 40 and T1CP >= 40 and T2MATH>=40 and T2AES>=40 and T2CP>=40 and T2PHY>=40 and T3MATH>=40 and T3AES>=40 and T3CP>=40 and T3PHY >= 40 and TOTAL / 12 >= 60 and (T2MATH + T3MATH)/2 >= 65 and T3AES >= 60:
    print("you have progressed")
elif TOTAL / 12 == 100:
    print("100 in everything, you must be cheating!")
else:
    print("unfortunately, you have not progressed, you must have at least an average of 60%")

quit()




