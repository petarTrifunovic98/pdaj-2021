import tracemalloc


def number_generator(N):
    ret = [i for i in range(0, N)]
    return ret


def double_loop_addition(l):
    ret = []
    for i in l:
        for j in l:
            ret.append(i + j)
    return ret

def double_loop_addition_gen(l):
    for i in l:
        for j in l:
            yield i + j

def main():
    l = number_generator(3000)

    tracemalloc.start()
    double_loop_addition(l)
    current, peak = tracemalloc.get_traced_memory()
    print(f"NO_YIELD: Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

    tracemalloc.start()
    gen = double_loop_addition_gen(l)
    for res in gen:
        pass
    current, peak = tracemalloc.get_traced_memory()
    print(f"YIELD: Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

if __name__ == "__main__":
    main()