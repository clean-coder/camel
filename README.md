# Camel
* convert long names of JUnit5 tests into a camel case like name embedded into a @Displayname()
* the name of the test must have the format xxxShouldBexxxx" e.g. "baluShouldBeSuper"`

## example
* `"baluShouldBeSuper"` will be transformed into `@DisplayName("balu() should be super")`
* the new test name is automatically copied in the clipboard

## run project
* with uv
  * `uv run python camel.py "baluShouldBeSuper"`
* with standard python and pip
  * `pip install pyperclip`
  * `python3 camel.py "baluShouldBeSuper"`

## run (local) tests
* with uv
  * `uv run pytest`
* with standard python and pip
  * `pytest`