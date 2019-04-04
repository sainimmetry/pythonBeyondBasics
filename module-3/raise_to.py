def raise_to(exp):
    def raise_to_exp(x):
        return pow(x,exp)
    return raise_to_exp


sqaure = raise_to(2)

print(sqaure.__closure__)

print(sqaure)

print(sqaure(5))

print(sqaure(9))

cube = raise_to(3)
print(cube(3))