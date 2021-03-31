time = int(input('Введите время в секундах'))

hours = time // 3600
print()
minutes = (time - hours * 3600) // 60
seconds = time - hours * 3600 - minutes * 60

print(f'{hours % 24:02d}:{minutes:02d}:{seconds:02d}')
