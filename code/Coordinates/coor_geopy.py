from geopy.distance import geodesic

def run():

    coordinate_1 = {19.1538784, -98.130956}
    # coordinate_2 = {19.7501211, -99.865649}
    coordinate_2 = {19.4542531, -98.921718}

    distance_1 = geodesic(coordinate_1, coordinate_2).km
    distance_2 = geodesic(coordinate_1, coordinate_2).miles

    print(round(distance_1, 3), ' km')
    print(round(distance_2, 3), ' miles')

if __name__ == '__main__':
    run()