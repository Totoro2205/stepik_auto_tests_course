def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'


def main():
    try:
        test_input_text(8, 11)
    except Exception as ex:
        print(repr(ex))
    try:
        test_input_text(11, 11)
    except Exception as ex:
        print(repr(ex))
    try:
        test_input_text(11, 15)
    except Exception as ex:
        print(repr(ex))

if __name__ == "__main__":
    main()
