print("Введите три целых числа через пробел:")
numbers = input().split()
n1 = int(numbers[0])
n2 = int(numbers[1])
n3 = int(numbers[2])
print(f"Введенные числа: {n1}, {n2}, {n3}")
m1 = n1 * n2 
m2 = n2 * n3  
m3 = n3 * n1 
power4 = n1 ** 4          
remainder = n2 % n3      
int_division = m3 // n1 
results_p5 = [power4, remainder, int_division]
print("\nРезультаты пункта 2 (умножения):")
print(f"{n1} * {n2} = {m1}")
print(f"{n2} * {n3} = {m2}")
print(f"{n3} * {n1} = {m3}")
print("\nРезультаты пункта 4:")
print(f"{n1} в 4 степени = {power4}")
print(f"Остаток от деления {n2} на {n3} = {remainder}")
print(f"Целочисленное деление {m3} на {n1} = {int_division}")
print("\nСумма переменных из пункта 5:")
sum_p5 = sum(results_p5)
print(f"{power4} + {remainder} + {int_division} = {sum_p5}")