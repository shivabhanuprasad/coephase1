#Add a nested condition to print "Excellent!" if the grade is A, and "Needs Improvement" if the grade is F.
# A: 85–100 (excllent) B: 70–84(Good) C: 55–69 (Better) D: 40–54 (Need improvement) F: below 40 (Fail)

marks=int(input("Enter your marks : "))
if marks>0:
    if marks <=40 :
        print(" You Failed !")
        print("Work Hard")
    elif marks <=54:
        print("PASS,Need Improvement")
    elif marks<=69:
        print("Better keep it up")
    elif marks<=84:
        print("Good,keep it up")
    else:
        print("EXCLLENT you got good marks")





