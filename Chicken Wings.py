def getFloatInput(sPrompt):
    # Prompt for a positive float with validation
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Error: Enter a positive, non-zero number.")
                continue
            return fValue
        except ValueError:
            print("Error: Invalid input. Enter a numeric value.")


def getMedian(lSales):
    # Calculate median without using statistics module
    lSales.sort()
    iCount = len(lSales)
    if iCount % 2 == 1:
        return lSales[iCount // 2]
    else:
        return (lSales[iCount // 2 - 1] + lSales[iCount // 2]) / 2


def main():
    lSales = []

    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        lSales.append(fSalesPrice)

        while True:
            sContinue = input("Enter another value Y or N: ").strip().lower()
            if sContinue in ("y", "n"):
                break
            print("Invalid input. Please enter Y or N.")

        if sContinue == "n":
            break

    lSales.sort()

    print("\nSorted Sales Entries:")
    for fValue in lSales:
        print(f"${fValue:,.2f}")

    fMin = min(lSales)
    fMax = max(lSales)
    fTotal = sum(lSales)
    fAverage = fTotal / len(lSales)
    fMedian = getMedian(lSales)
    fCommission = fTotal * 0.03

    print(f"\nMinimum: ${fMin:,.2f}")
    print(f"Maximum: ${fMax:,.2f}")
    print(f"Total: ${fTotal:,.2f}")
    print(f"Average: ${fAverage:,.2f}")
    print(f"Median: ${fMedian:,.2f}")
    print(f"Commission (3%): ${fCommission:,.2f}")


if __name__ == "__main__":
    main()
