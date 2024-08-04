def is_prime(num):
    # initial checks
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# print prime numbers from 2 to 100 and appending it in a list. 
list1 = []
for i in range(2, 100):
    if is_prime(i):
        list1.append(i)
print(list1)