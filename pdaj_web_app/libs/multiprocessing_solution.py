import multiprocessing as mp
from . import pdaj_project_lib as ppl


def generate_coord_pairs(n, m):
    for i in range(n):
        for j in range(m):
            yield (i, j)

def get_all_distances(coord_pair, points):
    for ind in range(len(points)):
        yield (ppl.calculate_distance(coord_pair, points[ind]), ind)

def prepare_args(coord_pairs, points):
    for coord_pair in coord_pairs:
        yield coord_pair, points

def get_chunksize(coord_pairs_num):
    return coord_pairs_num // 10
    
def _worker(args):
    coord_pair, points = args
    return min(get_all_distances(coord_pair, points))[1]

def get_closest_special(n, m, points):
    coord_pairs = generate_coord_pairs(n, m)
    with mp.Pool() as pool:
        res = pool.imap(
            _worker,
            prepare_args(coord_pairs, points),
            chunksize=get_chunksize(n*m)
        )
        return [r for r in res]


def main():
    res = get_closest_special(10, 10, [(1, 3), (3, 2), (6, 8), (9, 6), (5, 5)])
    print(res)
    # for i in range(100):
    #     print(next(res))
    #print([r for r in res])

if __name__ == "__main__":
    main()
