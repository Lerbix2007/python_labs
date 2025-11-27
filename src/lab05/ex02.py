import csv, json
from pathlib import Path
from openpyxl import Workbook


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    print(f" Ищем файл: {json_path}")
    if not json_file.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")

    if json_file.suffix.lower() != ".json":
        raise ValueError("Неверный тип файла. Ожидается .json")

    try:
        with json_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка чтения JSON: {e}")

    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    if data:
        first_item_keys = list(data[0].keys())
        remaining_keys = sorted(all_keys - set(first_item_keys))
        fieldnames = first_item_keys + remaining_keys
    else:
        fieldnames = sorted(all_keys)

    try:
        with csv_file.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                complete_row = {key: row.get(key, "") for key in fieldnames}
                writer.writerow(complete_row)
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")

    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный тип файла. Ожидается .csv")

    try:
        with csv_file.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")

            data = list(reader)

    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    if not data:
        raise ValueError("Пустой CSV файл")

    try:
        with json_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использует openpyxl. Автоматическая ширина колонок.
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный формат входного файла: ожидается .csv")
    if xlsx_file.suffix.lower() != ".xlsx":
        raise ValueError("Неверный формат выходного файла: ожидается .xlsx")
    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")

    with csv_file.open(encoding="utf-8") as f:
        reader = list(csv.reader(f, delimiter="\t"))
        if not reader:
            raise ValueError("Пустой файл")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in reader:
        ws.append(row)

    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            value = str(cell.value) if cell.value is not None else ""
            if len(value) > max_length:
                max_length = len(value)
        adjusted_width = max(max_length + 2, 8)
        ws.column_dimensions[column].width = adjusted_width

    wb.save(xlsx_file)


# Вызовы функций с АБСОЛЮТНЫМИ путями
json_to_csv(
    r"C:\Users\Librix\Desktop\labs\python_labs\data\samples\people.json",
    r"C:\Users\Librix\Desktop\labs\python_labs\data\samples\out\people_from_json.csv",
)
csv_to_json(
    r"C:\Users\Librix\Desktop\labs\python_labs\data\samples\people.csv",
    r"C:\Users\Librix\Desktop\labs\python_labs\data\samples\out\people_from_csv.json",
)
csv_to_xlsx(
    r"C:\Users\Librix\Desktop\labs\python_labs\data\samples\people.csv",
    r"C:\Users\Librix\Desktop\labs\python_labs\data\samples\out\people_from_csv.xlsx",
)
