from Coordinates import coor_geopy
import geopy_test as gt
import sys 


def run():
    print('.---------------------------------------')
    # # print('Number or params', len(sys.argv))
    # # print('params', sys.argv)
    # print(len(sys.argv))
    # print(sys.argv)
    print('----------------------------------------')
    coor_geopy.run()
    gt.run()

if __name__ == '__main__':
    run()