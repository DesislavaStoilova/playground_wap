**Project Overview**

This project automates testing of various pages on the UI Testing Playground. It uses Selenium WebDriver, pytest, and Allure for reporting. The automation covers testing of different interactions such as load delays, mouse hover actions, overlapped elements, and more.



**Instalation steps:**

Clone the Repository
Create and activate a Virtual Environment
Run the following command to create a virtual environment
```bash
python -m venv venv
```
Run the following command activate it
```bash
source venv/bin/activate
```
Install Requirements
Install all required dependencies listed in the requirements.txt file:
```bash
pip install -r requirements.txt or pip3 install -r requirements.txt
```
Run the tests
To run tests using pytest and allure, use the following command:
```bash
pytest --alluredir=reports/allure-results
```
Open the generated report
To open the generated allure report run the following command:
```bash
allure serve reports/allure-results
```


**Project structure:**

```bash
├── config/
│   ├── config.yaml
│   └── configuration.py
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── load_delay_page.py
│   ├── mouse_over_page.py
│   ├── overlapped_elements_page.py
│   ├── sample_app_page.py
│   └── text_input_page.py
├── reports/
├── tests/
│   ├── base_test.py
│   ├── test_load_delay.py
│   ├── test_mouse_over.py
│   ├── test_overlapped_element.py
│   ├── test_sample_app.py
│   └── test_text_input.py
├── utils/
│   └── locators.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```







**Video:**
<p class="has-line-data" data-line-start="56" data-line-end="57"><a href="https://github.com/user-attachments/assets/9928ac19-98b2-405d-9f11-637e96408a15">https://github.com/user-attachments/assets/9928ac19-98b2-405d-9f11-637e96408a15</a></p>
