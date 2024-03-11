# def test_string_is_digit():
#     items = ["1", "10", "33"]
#     for item in items:
#         assert item.isdigit()

# MODIFICAÇÃO PARA CRIAR FALHA
# def test_string_is_digit():
#     items = ["No", "1", "10", "33", "Yes"]
#     for item in items:
#         assert item.isdigit()

# # GRUPO DE TESTE DE MESMO COMPORTAMENTO
# def test_is_digit_1():
#     assert "1".isdigit()

# def test_is_digit_10():
#     assert "10".isdigit()

# def test_is_digit_33():
#     assert "33".isdigit()

# USANDO PARAMETRIZAÇÃO
import pytest

# @pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])
# def test_string_is_digit(item):
    # assert item.isdigit()

# ATUALIZAÇÃO COM CORREÇÃO DE FALHAS APONTADAS
@pytest.mark.parametrize("item", ["0", "1", "10", "33", "9"])
def test_string_is_digit(item):
    assert item.isdigit()