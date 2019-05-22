a = int(input('Input number from 100 to 999: '))
print('Sum:', a // 100 + (a // 10) % 10 + a % 10, \
      '\nMultiplication:', (a // 100) * ((a // 10) % 10) * (a % 10))
