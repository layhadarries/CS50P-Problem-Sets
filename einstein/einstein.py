"""
energy = mass * 300000000 **2
"""

mass = int(input("m: "))
light = 300000000


def main(mass):
    return mass * light ** 2


print("e: " + str(main(mass)))
