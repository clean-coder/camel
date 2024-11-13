# clipboard: https://note.nkmk.me/en/python-pyperclip-usage/
import pyperclip 
import sys 

def camel_to_words(s: str) -> str:
    res = ""
    for c in s:
        if c.isupper():
            res += " " + c.lower()
        else:
            res += c
    return res

def camel_to_words_with_should(s: str) -> str:
    function, description = s.split("Should")
    res = ""
    for c in description:
        if c.isupper():
            res += " " + c.lower()
        else:
            res += c
    return function + "() should" + res 


if len(sys.argv) != 2:
    print("usage: camel.py <string>")
    print('<string> should be camelCase in the following format: methodeNameShouldDoSomethingIfConditionsAreMet')
    print('example: python camel.py isUserMemberOfTeamsShouldReturnTrueIfUserIsMemberOfTeams)')
    sys.exit(1)

converted = camel_to_words_with_should(sys.argv[1])
#converted = camel_to_words(sys.argv[1])
print(converted)
pyperclip.copy(f'@DisplayName("{converted}")')
