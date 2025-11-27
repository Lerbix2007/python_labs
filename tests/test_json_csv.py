import pytest
from pathlib import Path
import json
import csv
from lab_05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [["name", "age", "city"], ["John", "30", "Mocsow"], ["Alice", "25", "SPB"]]
    with dst.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(data)
    csv_to_json(str(dst), str(src))

    with src.open(encoding="utf-8") as f:
        data_result = json.load(f)

    assert len(data_result) == 2
    assert {"name", "age", "city"} == set(data_result[0].keys())


def test_mistake_1(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = []
    with dst.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(data)
    with pytest.raises(ValueError, match="Неверный тип файла или пустой файл"):
        csv_to_json(str(dst), str(src))


def test_mistake_2(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    data = [["name", "age", "city"], ["John", "30", "Mocsow"], ["Alice", "25", "SPB"]]
    with dst.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(data)
    with pytest.raises(ValueError, match="Неверный тип файла или пустой файл"):
        csv_to_json(str(src), str(dst))


def test_mistake_finall(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [["name", "age", "city"], ["John", "30", "Mocsow"], ["Alice", "25", "SPB"]]
    with dst.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(data)
    with pytest.raises(FileNotFoundError, match="Неверный путь к файлу"):
        csv_to_json(str(src), str(dst))
