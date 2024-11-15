# clipboard: https://note.nkmk.me/en/python-pyperclip-usage/
import pyperclip
import sys


def camel_to_words_with_should(s: str) -> str:
    function, description = s.split("Should")
    res = ""
    for c in description:
        if c.isupper():
            res += " " + c.lower()
        else:
            res += c
    return function + "() should" + res


def generate_display_name_and_copy_to_clipboard(s: str) -> None:
    pyperclip.copy(f'@DisplayName("{s}")')


def print_usage():
    print("usage: camel.py <string>")
    print(
        "<string> should be camelCase in the following format: methodeShouldDoSomethingIfConditionsAreMet"
    )
    print("example: python camel.py baluShouldBeSuper)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    converted = camel_to_words_with_should(sys.argv[1])
    print(converted)
    generate_display_name_and_copy_to_clipboard(converted)
