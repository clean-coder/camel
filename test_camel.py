import pytest
import camel

def test_camel_to_words_with_should():
    expected = 'method() should do something if conditions are met'
    actual = camel.camel_to_words_with_should('methodShouldDoSomethingIfConditionsAreMet')
    assert expected == actual



