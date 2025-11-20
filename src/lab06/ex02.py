import sys, argparse
from pathlib import Path
import os
import contextlib
import io

from src.lab05.ex01 import json_to_csv, csv_to_json
from src.lab05.ex02 import csv_to_xlsx
from src.lab06.ex01 import check_file

def silent_check_file(file_path: str) -> bool:
    """Проверка файла без вывода на экран"""
    return os.path.exists(file_path) and os.path.isfile(file_path)

def run_silently(func, *args, **kwargs):
    """Запускает функцию без вывода на экран"""
    with contextlib.redirect_stdout(io.StringIO()):
        with contextlib.redirect_stderr(io.StringIO()):
            return func(*args, **kwargs)

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертатор из JSON в CSV")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help="Конвертатор из CSV в JSON")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help="Конвертатор из CSV в Excel")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            if not silent_check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)

            run_silently(json_to_csv, args.input, args.output)
            print(f"Успешно: JSON -> CSV")

        elif args.cmd == "csv2json":
            if not silent_check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)

            run_silently(csv_to_json, args.input, args.output)
            print(f"Успешно: CSV -> JSON")

        elif args.cmd == "csv2xlsx":
            if not silent_check_file(args.input):
                print(f"Ошибка: Файл {args.input} не существует или недоступен")
                sys.exit(1)

            run_silently(csv_to_xlsx, args.input, args.output)
            print(f"Успешно: CSV -> XLSX")

        else:
            print("Ошибка: Неизвестная команда")
            sys.exit(1)

        return 0

    except Exception as e:
        print(f"Ошибка при конвертации: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()



"   python3 -m src.lab06.ex02 json2csv --in data/samples/people.json --out data/samples/out/people_from_json.csv   "
"   python3 -m src.lab06.ex02 csv2json --in data/samples/people.csv --out data/samples/out/people_from_csv.json   "
"   python3 -m src.lab06.ex02 csv2xlsx --in data/samples/people.csv --out data/samples/out/people_from_csv.xlsx   "
"   python3 -m src.lab06.ex02 --help   "