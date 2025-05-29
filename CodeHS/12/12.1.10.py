import math
def distance(first_point, second_point):
    return math.sqrt(math.pow((second_point[1]-first_point[1]),2) + math.pow((second_point[0]-first_point[0]),2))
