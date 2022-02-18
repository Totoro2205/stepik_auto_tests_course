def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


def main():
    try:
        test_substring('fulltext', 'some_value')
    except Exception as ex:
        print(repr(ex))
    try:
        test_substring('1', '1')
    except Exception as ex:
        print(repr(ex))
    try:
        test_substring('some_text', 'some')
    except Exception as ex:
        print(repr(ex))

if __name__ == "__main__":
    main()
