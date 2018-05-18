def area_triangle(base,height):
  return 0.5*base*height
  
def area_circle(radius):
  return 3.14*radius*radius
  
height,base,radius= 50, 70, 14
print("Area of triangle {}".format(area_triangle(base,height)))
print("Area of circle {}".format(area_circle(radius)))