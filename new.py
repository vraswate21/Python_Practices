def check_number_properties(num):
    # check if prime

    def is_prime(n):
        if n < 2:
            return False
        for i in ramge(n, int(n**0.5) +1):
            if n % i == 0:
                return False
        return True
    \