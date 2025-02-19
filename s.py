def extract_number_from_string(text):
    numbers = []
    for t in text.split(" "):
        for e in t.split(","):
            try:
                numbers.append(float(e))
            except ValueError:
                pass
    return numbers

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1

def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1

def sqrt(a):
    return a ** 0.5

def end():
    print("Thank you for using the smart calculator")
    input("Press Enter key to exit")
    exit()

def sorry():
    print("This instruction is beyond my ability")

operations0 = {'CLOSE': end, 'END': end, 'TERMINATE': end, 'EXIT': end, 'QUIT': end}
operations1 = {'SQUARE': sqrt}
operations2 = {
    'PLUS': add, 'SUM': add, 'ADDITION': add, 'ADD': add, 'SUBTRACTION': sub,
    'SUBTRACT': sub, 'MINUS': sub, 'DIFFERENCE': sub, 'PRODUCT': multi,
    'MULTIPLICATION': multi, 'MULTIPLY': multi, 'DIVIDE': div, 'DIVISION': div,
    'LCM': lcm, 'HCF': hcf
}

def main():
    print("WELCOME TO THE SMART CALCULATOR")
    while True:
        print()
        text = input("Enter any text:\n")
        for word in text.split(" "):
            if word.upper() in operations2:
                try:
                    numbers = extract_number_from_string(text)
                    if len(numbers) >= 2:
                        result = operations2[word.upper()](numbers[0], numbers[1])
                        print("Result is:", result)
                    else:
                        print("Please provide two numbers for this operation.")
                except Exception as e:
                    print(f"Something went wrong: {e}")
                finally:
                    break
            elif word.upper() in operations0:
                operations0[word.upper()]()
                break
            elif word.upper() in operations1:
                try:
                    numbers = extract_number_from_string(text)
                    if len(numbers) >= 1:
                        result = operations1[word.upper()](numbers[0])
                        print("Result is:", result)
                    else:
                        print("Please provide one number for this operation.")
                except Exception as e:
                    print(f"Something went wrong: {e}")
                finally:
                    break
        else:
            sorry()

if __name__ == "__main__":
    main()
