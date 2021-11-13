import math


def number_generator(n):
    ret_list = []
    for i in range(1, n):
        ret_list.append(i)
    return ret_list

def find_prime_numbers(list):
    max_num = list[len(list)-1]
    ret_list = []
    for i in range(2, max_num):
        is_prime = True
        for j in range(2, int(math.sqrt(float(i))) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ret_list.append(i)
    return ret_list


def main():
    generated_list = number_generator(27)
    print(generated_list)
    prime_numbers_list = find_prime_numbers(generated_list)
    print(prime_numbers_list)

if __name__ == "__main__":
    main()