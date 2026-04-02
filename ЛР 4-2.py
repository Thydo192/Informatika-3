import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    # Открываем CSV файл для чтения
    # 'r' - режим чтения (read)
    # encoding='utf-8' - кодировка, поддерживающая любые символы (русские буквы, эмодзи и т.д.)
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        # Используем DictReader для автоматического использования первой строки как заголовков
        # Преобразуем итератор в список словарей
        # list() проходит по всем строкам файла и собирает их в список
        # В результате получаем: [словарь_строки1, словарь_строки2, ...]
        csv_reader = csv.DictReader(csv_file)

        # Преобразуем все строки в список словарей
        data = list(csv_reader)

    # Сериализуем в JSON файл с отступами равными 4
    # Открываем JSON файл для записи
    # 'w' - режим записи (write) - создаст новый файл или перезапишет существующий
    # encoding='utf-8' - сохраняем в UTF-8, чтобы корректно записывались любые символы
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")