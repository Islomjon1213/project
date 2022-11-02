a = 5
b = 2

try:
    print("Open resource")
    k = int(input("Enter number: "))
    print(k)
    print(a/b)
except ZeroDivisionError as a:
    print("ERROR ", a)

except ValueError as e:
    print("Bugs: ", e)

except Exception as b:
    print("Something is wrong: ", b)

finally:
    print("Close resource")   
