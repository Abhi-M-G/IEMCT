def is_prime(num):
   if num > 1:
       for i in range(2, int(num**0.5) + 1):
           if (num % i) == 0:
               return False
       return True
   return False

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
print("Prime numbers between", start, "and", end, "are:", prime_numbers)
