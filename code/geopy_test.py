from geopy.distance import geodesic

def run():

    coordinate_1 = {19.1538784, -98.130956} #Ubicación 1
    coordinate_2 = {19.7501211, -99.865649} #Ubicación 2
    coordinate_3 = {19.4542531, -98.921718} #Ubicación 3

    distance_1 = round(geodesic(coordinate_1, coordinate_2).km, 3)
    distance_2 = round(geodesic(coordinate_1, coordinate_3).km, 3)

    print(distance_1, ' km')
    print(distance_2, ' km')



    dT = [distance_1, distance_2]
    dT = min(dT)

    if dT == distance_1:
        print('La distancia menor corresponde del punto A al B')
    else:
        print('La distancia menor corresponde del punto A al C')


if __name__ == '__main__':
    run()