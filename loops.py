def is_prime(n):
    if n <= 1:
        return False # 0 and 1 are not prime number 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return false 
        return True
    
    num = int(input("enter a number"))
    if is_prime(num):
        print(f"{num}is a prime number")
    else:
        print(f"{num}is not a prime number.")