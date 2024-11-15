import pytest
import camel
import pyperclip 

def test_camel_to_words_with_should():
    expected = 'method() should do something if conditions are met'
    actual = camel.camel_to_words_with_should('methodShouldDoSomethingIfConditionsAreMet')
    assert expected == actual

def test_generate_display_name_and_copy_to_clipboard():
    expected = '@DisplayName("balu() should be ok")'
    camel.generate_display_name_and_copy_to_clipboard('balu() should be ok')
    actual = pyperclip.paste()
    assert expected == actual

