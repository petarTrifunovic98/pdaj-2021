import pdaj_project_lib as ppl

def generate_coord_pairs(n, m):
    for i in range(n):
        for j in range(m):
            yield (i, j)

def get_all_distances(coord_pair, points):
    for ind in range(len(points)):
        yield (ppl.calculate_distance(coord_pair, points[ind]), ind)

def _get_closest_special_gen(coord_pairs, points):
    for coord_pair in coord_pairs:
        yield min(get_all_distances(coord_pair, points))[1]

def get_closest_special(n, m, points):
    coord_pairs = generate_coord_pairs(n, m)
    res = _get_closest_special_gen(coord_pairs, points)
    return res
    

def main():
    res = get_closest_special(10, 10, [(1, 3), (3, 2), (6, 8), (9, 6), (5, 5)])
    print(res)

if __name__ == "__main__":
    main()