import pytest
from project import read_csv, input_validation, questions, calculate_city_scores

def test_read_csv():
    with pytest.raises(FileNotFoundError):
        read_csv()

def test_input_validation():
    assert input_validation('yes') == True
    assert input_validation('YES') == True
    assert input_validation('y') == True
    assert input_validation('no') == True
    assert input_validation('NO') == True
    assert input_validation('n') == True
    assert input_validation('noo') == False
    assert input_validation('hello') == False
    assert input_validation('this is my answer') == False

def test_questions():
    tests = [
        (["yes", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "yes", "no", "no"], "Rio de Janeiro"),
        (["no", "yes", "no", "yes", "yes", "no", "no", "no", "yes", "no", "yes", "no"], "Nairobi"),
        (["yes", "yes", "yes", "yes", "no", "no", "no", "yes", "no", "yes", "no", "yes"], "Vienna"),
    ]

    for inputs, expected in tests:
        assert questions(inputs) == expected

def test_calculate_city_scores():
    city_highest_scores = {'San Francisco': 75,'London': 74, 'Paris': 77, 'Berlin': 77}
    result = calculate_city_scores(city_highest_scores)
    assert result in ['Paris', 'Berlin']



