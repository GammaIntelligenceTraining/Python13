def area(w, h):
    return w * h

def perimeter(w, h):
    return (w + h) * 2

def count_materials(order_list):
    result = {}
    for carpet_type in order_list:
        result[carpet_type['size']] = {
                'area': area(carpet_type['width'], carpet_type['height']) * carpet_type['qty'],
                'perimeter': perimeter(carpet_type['width'], carpet_type['height']) * carpet_type['qty']
            }
    return result


def count_total_material(order_counts):
    total_a = 0
    total_p = 0
    for value in order_counts.values():
        total_a += value['area']
        total_p += value['perimeter']
    return {
        'total_area': total_a,
        'total_perimeter': total_p
    }


# count_total_material(count_materials(order))




order = [
    {'size': 'small', 'qty': 35, 'width': 60, 'height': 40},
    {'size': 'medium', 'qty': 20, 'width': 80, 'height': 60},
    {'size': 'large', 'qty': 15, 'width': 90, 'height': 90},
]


#
# x = count_materials(order)
# count_total_material(x)

print(count_materials(order))
print(count_total_material(count_materials(order)))

# x = {'one': 1,}