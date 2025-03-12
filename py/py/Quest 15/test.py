# python -m pytest test.py

import main
import pytest

@pytest.fixture()
def words():
  return ['Я', 'Хочу', 'Очень жоска', 'Пиццы', 'Ононосыми', 'Кря']

def test_calculate():
  assert main.calculate_sum(5) == 15
  
def test_calculate_sum():
  assert main.calculate_sum(-3) == 0
  
def test_calculate_neg():
  assert main.calculate_sum(0) == 0

def test_only_Three(words):
  li = words
  assert main.only_three(li) == ['Кря']
  
def test_sort(words):
  li = words
  assert main.sort_by_len(li) == ['Очень жоска', 'Ононосыми', 'Пиццы', 'Хочу', 'Кря', 'Я']
  
def test_count_letters(words):
  li = words
  assert main.count_letters(li) == {'я': 2, 'х': 1, 'о': 6, 'ч': 2, 'у': 1, 'е': 1, 'н': 3, 'ь': 1, ' ': 1, 'ж': 1, 'с': 2, 'к': 2, 'а': 1, 'п': 1, 'и': 2, 'ц': 2, 'ы': 2, 'м': 1, 'р': 1}

@pytest.mark.parametrize('n, expected',
                         [(7, 5040),
                          (3, 6),
                          (12, 479001600),
                          (-5, -120),
                          (0, 1)])
def test_factorial(n, expected):
  assert main.factorial(n) == expected