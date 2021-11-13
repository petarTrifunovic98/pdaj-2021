def number_generator(n):
    ret_list = []
    for i in range(1, n):
        ret_list.append(i)
    return ret_list

def main():
    print(number_generator(12))

if __name__ == "__main__":
    main()