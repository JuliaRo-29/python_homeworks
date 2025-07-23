import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для метода capitalize
@pytest.mark.positive

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),  # Обычная строка
    ("hello world", "Hello world"),  # Строка с пробелом
    ("python", "Python"),  # Одинарное слово
    ("a", "A"),  # Один символ
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected, f"Expected {expected}, but got {string_utils.capitalize(input_str)}"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),  # Строка начинается с цифры
    ("", ""),  # Пустая строка
    ("   ", "   "),  # Строка из пробелов
    ("SKYPRO", "SKYPRO"),  # Строка уже в верхнем регистре
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected, f"Expected {expected}, but got {string_utils.capitalize(input_str)}"


# Тесты для метода trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),  # Пробелы в начале
    (" sky pro ", "sky pro "),  # Пробелы только в начале, строка с пробелами внутри и в конце
    ("\t  hello", "hello"),  # Табуляция и пробелы в начале
])
def test_trim_positive(input_str, expected):

    assert string_utils.trim(input_str) == expected, f"Expected {expected}, but got {string_utils.trim(input_str)}"

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),  # Строка без пробелов
    ("", ""),  # Пустая строка
    ("skypro   ", "skypro   "),  # Пробелы только в конце
])
def test_trim_negative(input_str, expected):

    assert string_utils.trim(input_str) == expected, f"Expected {expected}, but got {string_utils.trim(input_str)}"

# Тесты для метода contains
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),  # Одинарный символ присутствует
    ("SkyPro", "Pro", True),  # Подстрока присутствует
    ("Hello123", "123", True),  # Числовая подстрока
])
def test_contains_positive(input_str, symbol, expected): 

    assert string_utils.contains(input_str, symbol) == expected, f"Expected {expected}, but got {string_utils.contains(input_str, symbol)}"


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),  # Символ отсутствует
    ("", "a", False),  # Пустая строка
    ("SkyPro", "", False),  # Пустой искомый символ
])

def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected, f"Expected {expected}, but got {string_utils.contains(input_str, symbol)}"

# Тесты для метода delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # Удаление одиночного символа
    ("SkyPro", "Pro", "Sky"),  # Удаление подстроки
    ("Hello!!!", "!", "Hello"),  # Удаление повторяющегося символа
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected, f"Expected {expected}, but got {string_utils.delete_symbol(input_str, symbol)}"

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "Z", "SkyPro"),  # Символ отсутствует
    ("", "a", ""),  # Пустая строка
    ("SkyPro", "", "SkyPro"),  # Пустой искомый символ
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected, f"Expected {expected}, but got {string_utils.delete_symbol(input_str, symbol)}"

if __name__ == '__main__':
    pytest.main()
