def generate_password(n):
    if n < 3 or n > 20:
        return 'Неподходящее число. Число должно быть в диапазоне 3 - 20'
    else:
        result = []
        for i in range(1, 20):
            for j in range(i + 1, 21):
                if n % (i + j) == 0:
                    result.append(f"{i}{j}")
        return ''.join(result)


# Отображение паролей для всех чисел в консоли
for num in range(3, 21):
    print(f"{num} - {generate_password(num)}")