import math


def generate_coords(n, m):
    ret_list = []
    for i in range(n):
        for j in range(m):
            ret_list.append((i, j))
    return ret_list

def calculate_distance(coords1, coords2):
    x1, y1 = coords1
    x2, y2 = coords2
    distance =  math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return distance

def get_closest_special(n, m, points):
    coords = generate_coords(n, m)
    ret_list = []
    for coord in coords:
        min_distance = calculate_distance(coord, points[0])
        closest_filed = 0
        for i in range(1, len(points)):
            distance = calculate_distance(coord, points[i])
            if distance < min_distance:
                min_distance = distance
                closest_filed = i
        ret_list.append(closest_filed)
    return ret_list

def main():
    res = get_closest_special(10, 10, [(1, 3), (3, 2), (6, 8), (9, 6), (5, 5)])
    print(res)

if __name__ == "__main__":
    main()
        

