import math


# Function to get validated float input
def getFloatInput(strPrompt):
    while True:
        try:
            fltValue = float(input(strPrompt))
            if fltValue <= 0:
                print("ERROR: Value must be greater than 0.")
            else:
                return fltValue
        except ValueError:
            print("ERROR: Enter a valid number.")


# Function to calculate gallons of paint (rounded up)
def getGallonsOfPaint(fltWallSqFt, fltFeetPerGallon):
    return math.ceil(fltWallSqFt / fltFeetPerGallon)


# Function to calculate labor hours
def getLaborHours(fltLaborHoursPerGallon, intGallons):
    return fltLaborHoursPerGallon * intGallons


# Function to calculate labor cost
def getLaborCost(fltLaborHours, fltLaborChargePerHour):
    return fltLaborHours * fltLaborChargePerHour


# Function to calculate paint cost
def getPaintCost(intGallons, fltPaintPrice):
    return intGallons * fltPaintPrice


# Function to get sales tax rate based on state
def getSalesTax(strState):
    strState = strState.upper()
    if strState == "CT":
        return 0.06
    elif strState == "MA":
        return 0.0625
    elif strState == "ME":
        return 0.085
    elif strState == "NH":
        return 0.0
    elif strState == "RI":
        return 0.07
    elif strState == "VT":
        return 0.06
    else:
        return 0.0


# Function to display and write cost estimate
def showCostEstimate(strLastName, intGallons, fltLaborHours, fltPaintCost, fltLaborCost, fltTaxRate, fltSubtotal,
                     fltTaxAmount, fltTotal):
    strFileName = strLastName + "_PaintJobOutput.txt"
    with open(strFileName, "w") as file:
        file.write(f"Gallons of Paint Required: {intGallons}\n")
        file.write(f"Labor Hours Required: {fltLaborHours:.2f}\n")
        file.write(f"Paint Cost: ${fltPaintCost:.2f}\n")
        file.write(f"Labor Cost: ${fltLaborCost:.2f}\n")
        file.write(f"Subtotal: ${fltSubtotal:.2f}\n")
        file.write(f"Sales Tax: ${fltTaxAmount:.2f}\n")
        file.write(f"Total Cost: ${fltTotal:.2f}\n")

    # Output to screen
    print(f"\nGallons of Paint Required: {intGallons}")
    print(f"Labor Hours Required: {fltLaborHours:.2f}")
    print(f"Paint Cost: ${fltPaintCost:.2f}")
    print(f"Labor Cost: ${fltLaborCost:.2f}")
    print(f"Subtotal: ${fltSubtotal:.2f}")
    print(f"Sales Tax: ${fltTaxAmount:.2f}")
    print(f"Total Cost: ${fltTotal:.2f}")
    print(f"\nOutput file created: {strFileName}")


# Main function
def main():
    # Get user inputs
    fltWallSqFt = getFloatInput("Enter Square Feet of Wall: ")
    fltPaintPrice = getFloatInput("Enter Paint Price: ")
    fltFeetPerGallon = getFloatInput("Enter Feet per Gallon of Paint: ")
    fltLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
    fltLaborChargePerHour = getFloatInput("Enter Painting Labor Charge per Hour: ")

    strState = input("Enter the State abbreviation (CT, MA, ME, NH, RI, VT): ")
    strLastName = input("Enter the Customer's Last Name: ")

    # Calculations
    intGallons = getGallonsOfPaint(fltWallSqFt, fltFeetPerGallon)
    fltLaborHours = getLaborHours(fltLaborHoursPerGallon, intGallons)
    fltPaintCost = getPaintCost(intGallons, fltPaintPrice)
    fltLaborCost = getLaborCost(fltLaborHours, fltLaborChargePerHour)

    fltSubtotal = fltPaintCost + fltLaborCost
    fltTaxRate = getSalesTax(strState)
    fltTaxAmount = fltSubtotal * fltTaxRate
    fltTotal = fltSubtotal + fltTaxAmount

    # Output
    showCostEstimate(strLastName, intGallons, fltLaborHours, fltPaintCost, fltLaborCost, fltTaxRate, fltSubtotal,
                     fltTaxAmount, fltTotal)


# Run the program
main()
