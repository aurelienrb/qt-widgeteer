# Choosing an automation test stack

## Goals

- Generate a test report file in PDF format
  - HTML reports are convenient for immediate reading, but are not ideal for long term archiving or printing
  - PDF files are needed when archiving (as evidence for regulation purpose) or sharing the test results is necessary
  - So if the main output is in HTML, its conversion to PDF must generate a PDF with decent readability
- Make it fairly easy to link each test case with a high level requirement
  - Such requirements must be readable by non technical people
- Allow to specify the system requirements in Markdown files redable by both non technical humans and IA agents

## Technical options

### Writing and running the test suite

- Behave / PyTest
  - Python library
  - Pros: Test case can be written as separate feature files with high level of abstraction
  - Cons: more glue code to write (but IA can greatly help generate all the boiler plate)
- Robot Framework
  - Framework built on top of Python
  - Pros: Allows to create a custom language (DSL) to express test cases in terms close to the business language
  - Cons: New syntax to learn
- [Karate](https://docs.karatelabs.io/)
  - In Java
  - Pros: reduce the "glue" code between BDD features and implementation code
  - Cons: the BDD logic is expressed in low level implementation details not suited for non technical persons

### GUI automation

- SPIX
  - Based on XML RPC, compatible by design with Robot Framework?
  - Supports both Qt Widgets and QML/QtQuick
- Qt Widgeteer
  - Restricted to Qt Widgets only
  - Based on QTest: can face some limitations with context menus
- pyautogui

