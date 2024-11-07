def get_string_length(s: str) -> int:
    return len(s)

def test_empty_string():
    assert get_string_length("") == 0

def test_single_line_string():
    assert get_string_length("hello") == 5

def test_multiline_string():
    assert get_string_length("hello\nworld") == 11

def test_string_with_spaces():
    assert get_string_length("   ") == 3