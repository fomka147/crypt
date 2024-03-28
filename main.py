import random

def generate_unique_codes(num_codes, code_length):
    generated_codes = set()  # Создаем множество для хранения уникальных кодов
    while len(generated_codes) < num_codes:
        code = ''.join(random.choices(['0', '1'], k=code_length))  # Генерируем случайный код
        generated_codes.add(code)  # Добавляем его во множество
    return list(generated_codes)  # Возвращаем список уникальных кодов

# Генерируем 150 индивидуальных кодов, каждый длиной 10 символов
codes = generate_unique_codes(250, 10)

# Печатаем сгенерированные коды
for code in codes:
    print(code)
