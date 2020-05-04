# Change the code inside this function to enter the expression that equals y'
# For instance, here y' = (1/x)(y^2 + y)


def f(x, y):
    return (1/x)*(y**2 + y)


N = int(input("Enter a value for N: "))
h = float(input("Enter a value for h: "))
x = float(input("Enter a value for x0: "))
y = float(input("Enter a value for y0: "))
print()

for i in range(0, N):
    print("x" + str(i) + " = " + str(round(x, 2)) + ", y" + str(i) + " = " + str(round(y, 2)))
    y = y + (h/2)*(f(x, y) + f(x + h, y + h*f(x, y)))
    x += h

print("xn = " + str(round(x, 2)) + ", yn = " + str(round(y, 2)))
