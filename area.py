def area_of_a_circle(pi=22/7):
    area=pi*r*r
    a=area*0.0001
    print("Area of the circle=",format(area,".2f"),"cm^2")
    print("Area of the circle=",format(a,".5f"),"m^2")
r=float(input("Enter the radius of the circle: "))
area_of_a_circle()