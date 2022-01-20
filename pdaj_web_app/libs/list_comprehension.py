import pdaj_project_lib as ppl

def generate_coord_pairs(n, m):
    ret = [(i, j) for i in range(n) for j in range(m)]
    #print(ret)
    return ret

def get_all_distances(coord_pair, points):
    ret = [(ppl.calculate_distance(coord_pair, points[ind]), ind) for ind in range(len(points))]
    return ret


def get_closest_special(n, m, points):
    coord_pairs = generate_coord_pairs(n, m)
    ret = [min(get_all_distances(coord_pair, points))[1] for coord_pair in coord_pairs]
    return ret

def main():
    res = get_closest_special(10, 10, [(1, 3), (3, 2), (6, 8), (9, 6), (5, 5)])
    print(res)

if __name__ == "__main__":
    main()