# Prompt for person's name
strName = input("Enter the person's name: ")

# Prompt for 4 test scores
intTest1 = int(input("Enter Test Score 1 (whole number): "))
intTest2 = int(input("Enter Test Score 2 (whole number): "))
intTest3 = int(input("Enter Test Score 3 (whole number): "))
intTest4 = int(input("Enter Test Score 4 (whole number): "))

# Make sure that all test scores are >= 0
if intTest1 < 0:
    print("Test scores must be greater than 0.")
    exit()
if intTest2 < 0:
    print("Test scores must be greater than 0.")
    exit()
if intTest3 < 0:
    print("Test scores must be greater than 0.")
    exit()
if intTest4 < 0:
    print("Test scores must be greater than 0.")
    exit()

# Prompt user to drop lowest grade
strDropLowest = input("Drop the Lowest Grade? (Y or N): ")

# Validate Y or N input
if strDropLowest != "Y":
    if strDropLowest != "N":
        print("Enter Y or N to Drop the Lowest Grade.")
        exit()

# Calculate average manually for each case
if strDropLowest == "Y":
    if intTest1 <= intTest2 and intTest1 <= intTest3 and intTest1 <= intTest4:
        fltAverage = (intTest2 + intTest3 + intTest4) / 3.0
    elif intTest2 <= intTest1 and intTest2 <= intTest3 and intTest2 <= intTest4:
        fltAverage = (intTest1 + intTest3 + intTest4) / 3.0
    elif intTest3 <= intTest1 and intTest3 <= intTest2 and intTest3 <= intTest4:
        fltAverage = (intTest1 + intTest2 + intTest4) / 3.0
    elif intTest4 <= intTest1 and intTest4 <= intTest2 and intTest4 <= intTest3:
        fltAverage = (intTest1 + intTest2 + intTest3) / 3.0
else:
    fltAverage = (intTest1 + intTest2 + intTest3 + intTest4) / float(4)

# Determine letter grade
if fltAverage >= 97.0:
    strGrade = "A+"
if fltAverage >= 94.0 and fltAverage < 97.0:
    strGrade = "A"
if fltAverage >= 90.0 and fltAverage < 94.0:
    strGrade = "A-"
if fltAverage >= 87.0 and fltAverage < 90.0:
    strGrade = "B+"
if fltAverage >= 84.0 and fltAverage < 87.0:
    strGrade = "B"
if fltAverage >= 80.0 and fltAverage < 84.0:
    strGrade = "B-"
if fltAverage >= 77.0 and fltAverage < 80.0:
    strGrade = "C+"
if fltAverage >= 74.0 and fltAverage < 77.0:
    strGrade = "C"
if fltAverage >= 70.0 and fltAverage < 74.0:
    strGrade = "C-"
if fltAverage >= 67.0 and fltAverage < 70.0:
    strGrade = "D+"
if fltAverage >= 64.0 and fltAverage < 67.0:
    strGrade = "D"
if fltAverage >= 60.0 and fltAverage < 64.0:
    strGrade = "D-"
if fltAverage < 60.0:
    strGrade = "F"

# Output results
print("Name: " + strName)
print("Average: " + str(round(fltAverage, 1)))
print("Letter Grade: " + strGrade)
