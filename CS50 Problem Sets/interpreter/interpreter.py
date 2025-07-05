exp = input("Expression: ")
x , y , z = exp.split()
xs = int(x)
zs= int(z)

if y == "+":
    result = float(xs+zs)
elif y == "-":
    result = float(xs-zs)
elif y == "*":
    result = float(xs*zs)
elif y == "/":
    result = float(xs/zs)
print(f"{result:.1f}")
