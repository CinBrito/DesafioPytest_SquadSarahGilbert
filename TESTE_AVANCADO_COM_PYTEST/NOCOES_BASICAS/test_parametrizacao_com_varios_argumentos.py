@pytest.mark.parametrize("item, attribute", [("", "format"), (list(), "append")])
def test_attributes(item, attribute):
    assert hasattr(item, attribute)

