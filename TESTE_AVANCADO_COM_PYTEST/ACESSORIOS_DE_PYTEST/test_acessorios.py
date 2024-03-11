import pytest
import tempfile
import os

# @pytest.fixture
# def tmp_file():
#     def create():
#         temp = tempfile.NamedTemporaryFile(delete=False)
#         return temp.name
#     return create

# INTRODUZINDO ESCOPO
@pytest.fixture(scope="module")
def tmp_file():
    def create(contents):
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    # ADICIONANDO LIMPEZA
    def cleanup():
        os.remove(temp.name)

    request.addfinalizer(cleanup) # não 
    return create

# def test_file(tmp_file):
#     path = tmp_file()
#     assert os.path.exists(path)

# USANDO MONKEYPATCH
def test_os(monkeypatch):
    monkeypatch.setattr('os.path.exists', lambda x: False)
    assert os.path.exists('/') is False

# USANDO MONKEYPATCH COM CADEIA DE CARACTERES
def test_os(monkeypatch):
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    assert os.path.exists('/') is False