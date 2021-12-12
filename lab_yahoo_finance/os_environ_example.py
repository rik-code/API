import os

for key in os.environ:
    print(f'Переменная: {key}\nЗначение: {os.environ[key]}\n')