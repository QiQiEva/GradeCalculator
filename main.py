gradeArray = []
gradeWeights = []

while True:
    print("Select an option:")
    print("1. Enter a grade")
    print("2. Enter an AP grade")
    print("3. Calculate Average")

    # Takes user input for the grade type selection
    choice = int(input())

    if choice == 1:
        numOfGrades = int(input("How many grades do you want to enter?"))

        for i in range(numOfGrades):
            grade = int(input("Enter your number grade ONLY: "))
            gradeArray.append(grade)
            gradeWeights.append(1)

        print("Grades Entered:", gradeArray)

    elif choice == 2:
        numOfGrades = int(input("How many grades do you want to enter?"))

        for i in range(numOfGrades):
            grade = int(input("Enter your number grade ONLY: "))

            # Multiply the AP weight to grade before appending to array of grades
            gradeArray.append(grade * 1.1)
            gradeWeights.append(1.1)
      
        print("Grades Entered:", gradeArray)
    
    elif choice == 3:
        if not gradeArray or not gradeWeights:
            print("No grades entered yet.")
            continue

        # Fetch values from arrays
        total_sum = sum(gradeArray)
        total_weights = sum(gradeWeights)

        gradeAvg = round(total_sum / total_weights)


        print("Weighted Average:", gradeAvg)
        break

    

