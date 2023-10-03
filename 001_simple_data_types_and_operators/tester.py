side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))

half_perimeter = (side_a + side_b + side_c) / 2

my_triangle_area = (half_perimeter * (half_perimeter - side_a) *
                    (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5

print('Area of triangle is: ' + str(my_triangle_area))
