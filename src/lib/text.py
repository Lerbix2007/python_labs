import re

def normalize(text, casefold=True, yo2e=True):
    if not text:
        return ""
    
    result = text
    
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    
    if casefold:
        result = result.casefold()
    
    result = result.strip()
    result = re.sub(r'\s+', ' ', result)
    
    return result

def tokenize(text):
    if not text:
        return []
    
    return re.findall(r'[\w\-]+', text)

def count_freq(tokens):
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq, n=5):
    if not freq:
        return []
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

def test_functions():
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ")
    print("=" * 50)
    
    # Тесты для normalize
    print("\n1. normalize():")
    test_cases = [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ]
    
    for input_text, expected in test_cases:
        result = normalize(input_text)
        print(f"  '{input_text}' → '{result}'")
    
    # Тесты для tokenize
    print("\n2. tokenize():")
    test_cases = [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ]
    
    for input_text, expected in test_cases:
        result = tokenize(input_text)
        print(f"  '{input_text}' → {result}")
    
    # Тесты для count_freq + top_n
    print("\n3. count_freq() + top_n():")
    
    tokens1 = ["a", "b", "a", "c", "b", "a"]
    freq1 = count_freq(tokens1)
    top1 = top_n(freq1, 2)
    print(f"  {tokens1} → {top1}")
    
    tokens2 = ["bb", "aa", "bb", "aa", "cc"]
    freq2 = count_freq(tokens2)
    top2 = top_n(freq2, 2)
    print(f"  {tokens2} → {top2}")
def demo_text_analysis():
    """Демонстрационный текст для анализа во 2 задании"""
    demo_text = "Привет Мир!!! Привет!.."

if __name__ == "__main__":
    test_functions()