import math

def is_prime(func):
    def wrapper(*args, **kwargs):
      #здесь мы вычисляем рез-т функции sum_three
      result = func(*args, **kwargs)
      if result <= 1:
        print("Составное")
      else:
        # Мы перебираем числа от 2 до квадратного корня
        for i in range(2, int(math.sqrt(result)) + 1):
          if result % i == 0:
            print("Составное")
            return result
        print("Простое")
      return result
    return wrapper

@is_prime
def sum_three(a, b, c):
  return a + b + c

result = sum_three(2, 3, 6)
print(result)