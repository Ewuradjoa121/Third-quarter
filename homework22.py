from math import pi,sqrt
def SHM(length, gravity=9.81):
    return 2*pi*sqrt(length/gravity)
def gravity( M,m,R,G=6.67*10**-11):
    return(G*M*m/R**2)
def energy(mass,speed=3.0*10**8):
    return (mass*speed**2)
def main():
    print("1.SHM/n 2.gravity /n 3. Energy")
choice=input("enter choice:")
if choice =="1":
    length= float(input("enter length:"))
    print( "time=",SHM(length))
elif choice =="2":
    print("gravity=", gravity())
elif choice=="3":
    mass=float(input("enter  mass:"))
    print("energy")
else:
    print("invaild choice")

main()
