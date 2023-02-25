def volume_of_a_cylinder(pi=22/7):
    volume=pi*r*r*h
    v=volume*0.000001
    print("volume of the cylinder=",format(volume,".2f"),"cm^3")
    print("volume of the cylinder=",format(v,".8f"),"m^3")
r=float(input("Enter the radius of the cylinder in cm: "))
h=float(input("Enter the height of the cylinder in cm: "))
volume_of_a_cylinder()