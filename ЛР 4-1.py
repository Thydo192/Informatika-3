import json
# Читаем файл
data = json.load(open('input.json'))
# Суммируем произведения score * weight и округляем до 3 знаковпосле запятой
result = round(sum(d['score'] * d['weight'] for d in data), 3)
# Выводим результат
print(f"{result:.3f}")