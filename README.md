# Web automation

The following project automates the testing process to order items from a website with cart and general data.

## Installation

Use a virtualenv to install the dependencies.

```bash
pip install -r requirements.txt
```

## Usage
Just run
```pytest``` from the project root directory.

## Project structure

The project is structured as follows:

```bash
├── README.md
├── pom: Page Object Model files. Each page has its own class. Also, top banner is included since it's common in all pages.
│   ├── __init__.py
│   ├── cart_page.py
│   ├── ...
├── singleton: Singleton pattern implementation. It's used to create a single instance of the webdriver.
├── test: Test files. Currently only one UAT test has been implemented. It uses fixtures for some common operations like Login.
├── webdriver: Webdriver files. It has options to support Chrome, Firefox and IE.
├── requirements.txt: Python dependencies.
├── conftest.py: Pytest configuration file. Paths and instances are setup here for the whole session
├── util: Resources and utilities.
```

## Patterns used:
* Singleton
* Page Object Model