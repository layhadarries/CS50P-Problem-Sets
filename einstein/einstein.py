"""
energy = mass * 300000000 **2
"""

mass = int(input("m: "))
light = 300000000


def main(mass):
    energy = mass * light ** 2
    return energy


print("e: " + str(main(mass)))
