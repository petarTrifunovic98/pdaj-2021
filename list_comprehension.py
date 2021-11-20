import math


def number_generator(N):
    ret = [i for i in range(1, N)]
    return ret

def find_squares(list):
    squares_l = [num for num in list if math.sqrt(num).is_integer()]
    return squares_l

def main():
    list = number_generator(70)
    # print(list)
    squares_l = find_squares(list)
    print(squares_l)

if __name__ == "__main__":
    main()