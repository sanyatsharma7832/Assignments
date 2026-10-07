x=int(input("Length of side 1:"))
y=int(input("Length of side 2:"))
z=int(input("Length of side 3:"))

if x>=y and x>=z:
    hypotenuse=x
    base=y
    perpendicular=z
elif y>=x and y>=z:
    hypotenuse=y
    base=x
    perpendicular=z
else:
    hypotenuse=z
    base=x
    perpendicular=y

if base**2 + perpendicular**2 == hypotenuse**2:
    print("Triangle is right angled")
else:
    print("Triangle is right not angled")
