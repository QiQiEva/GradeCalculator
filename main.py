while True:
    print("Select an option:")
    print("1. Enter a grade")
    print("2. Enter an AP grade")

    gradeArray = []
    # Takes user input for the grade type selection
    choice = int(input())

    if choice == 1:
        numOfGrades = int(input("How many grades do you want to enter?"))

        for i in range(numOfGrades):
            grade = int(input("Enter your number grade ONLY: "))
            gradeArray.append(grade)

        print(gradeArray)

