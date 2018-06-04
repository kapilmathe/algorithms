def find_prime_factor(n):
    pass



def ugly_number(n):
    ugly_number_map = {1:1, 2:2, 3:3, 4:5}
    ugly_counter = 0
    if ugly_number_map.get(n):
        return ugly_number_map.get(n)

if __name__ == '__main__':
    n = long(raw_input().strip())

