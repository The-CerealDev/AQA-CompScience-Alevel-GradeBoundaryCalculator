import math
def courseworkToTest(b):
    courseworkMark = -2
    while courseworkMark == -2:
        try:
            courseworkMark = int(input("Enter the mark you got in the coursework (or give an estimation)\n"))
            if courseworkMark < 0 or courseworkMark > 75:
                courseworkMark = -2
                print("must input a valid mark")
        except Exception as e:
            courseworkMark = -2
    weightedMark = courseworkMark *1
    for index in b:
        calc = math.ceil((index[1] - weightedMark)/1.5)
        if calc <= 0:
            print(f"You are automatically guarenteed at least a grade {index[0]}")
        elif calc > 200:
            print(f"You cannot achieve a grade of {index[0]}, you would need a mark of {calc} out of 200")
        else:
            print(f"In order to achieve a grade {index[0]} you need to achieve a score of {calc} out of 200 in the exam ({(calc/200)*100}%)")
def testToCoursework(b):
    testMark = -2
    while testMark == -2:
        try:
            testMark = int(input("Enter the combined mark you got in the test (or give an estimation)\n"))
            if testMark < 0 or testMark > 200:
                courseworkMark = -2
                print("must input a valid mark")
        except Exception as e:
            testMark = -2
    weightedMark = testMark *1.5
    for index in b:
        calc = math.ceil((index[1] - weightedMark))
        if calc <= 0:
            print(f"You are automatically guarenteed at least a grade {index[0]}")
        elif calc > 75:
            print(f"You cannot achieve a grade of {index[0]}, you would need a mark of {calc} out of 75")
        else:
            print(f"In order to achieve a grade {index[0]} you need to achieve a score of {calc} out of 75 in the coursework ({round((calc/75)*100,2)}%)")
def menu(b):
    choice = input("1. Know coursework mark, find test mark\n2. Know test mark, find coursework mark\n3. Quit\n")
    while choice not in ["1","2","3"]:
        print("you must enter a number between 1 and 3")
        choice = input("1. Know coursework mark, find test mark\n2. Know test mark, find coursework mark\n3. Quit\n")
    if choice == "1":
        courseworkToTest(b)
    elif choice == "2":
        testToCoursework(b)
    else:
        return 0
    return 1
boundaries = [["A*", 309], ["A",261], ["B",214], ["C",167], ["D",120], ["E",74]]
print("Computer Science A-level grade calculator")
print("This is based on the June 2019 Grade boundaries")
print("The combined boundaries for marks are as follows:\nA*:309\nA:261\nB:214\nC:167\nD:120\nE:74")
print("Exam is out of 375, the two exams are each out of 100 for a combined total of 200 marks. The coursework is worth 75 marks. The exams are scaled by 1.5 to increase the total of marks from 200 to 300")    
while menu(boundaries):
    pass
print("Thanks for using me, I hope I was helpful!\nProgram created by GMG0241")
