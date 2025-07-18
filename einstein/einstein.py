c = 300000000            #speed of light

def energy(m):
    return m * c ** 2

def main():
    m = int(input("m: "))
    e = energy(m)
    print("e: " + str(e))

main()
