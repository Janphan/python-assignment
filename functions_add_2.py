def add(float1: float, float2: float):
    return int(float1 + float2 + 0.5)
def main():
    float1 = float(input("Enter a float: "))
    float2 = float(input("Enter a float: "))
    result = add(float1, float2)
    print(result)
if __name__ == "__main__":
    main()