# input coordinates
def manhattan_distance(cd1:list, cd2:list):
    distance = 0
    for n in range(len(cd1)):
        # sum distances
        distance = distance + abs(cd1[n]-cd2[n])
    return distance

# example
# print(manhattan_distance([1,5], [4,9]))
# print(manhattan_distance([2,3,6], [7,2,4]))