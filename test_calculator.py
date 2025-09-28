import pytest
from calculator import MetricCalculator

def test_calculate_mean_basic():
    calculator = MetricCalculator()
    data = [1, 2, 3, 4, 5]
    result = calculator.calculate_mean(data)
    assert result == 3.0

def test_calculate_mean_empty_list():
    calculator = MetricCalculator()
    data = []
    result = calculator.calculate_mean(data)

def test_calculate_accuracy_basic():
    calculator = MetricCalculator()
    y_true = [1, 0, 1, 0]
    y_pred = [1, 0, 0, 0]
    result = calculator.calculate_accuracy(y_true, y_pred)
    assert result == 0.75

def test_calculate_accuracy_empty():
    calculator = MetricCalculator()
    y_true = []
    y_pred = []
    result = calculator.calculate_accuracy(y_true, y_pred)

def test_calculate_accuracy_different_lengths():
    calculator = MetricCalculator()
    y_true = [1, 0, 1]
    y_pred = [1, 0]
    result = calculator.calculate_accuracy(y_true, y_pred)

def test_add_metric():
    calculator = MetricCalculator()
    calculator.add_metric("test_metric", 0.85)
    results = calculator.get_results()
    assert ("test_metric", 0.85) in results
