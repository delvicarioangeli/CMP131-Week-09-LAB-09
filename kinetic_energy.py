
#Angelina Del Vicario
#CMP131
#Lab 09
#Week 09
#Kinetic energy
#11/04/26
def kineticEnergy(mass,velocity):
    return 0.5 * mass * (velocity **2)

def main():
    print("Kinetic energy calculator")

    mass = float(input("Enter mass in kilograms:"))
    velocity = float(input("Enter Velocity in meters per second:"))

    result = kineticEnergy(mass,velocity)

    print("Kinetic Energy", result)


main()