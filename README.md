# playground_wap


Instalation steps:
1. Clone the Repository
2. Create and activate a Virtual Environment
  - Run the following command to create a virtual environment
     python -m venv venv
  - Run the following command activate it
     source venv/bin/activate
3. Install Requirements
  - Install all required dependencies listed in the requirements.txt file:
     pip install -r requirements.txt or pip3 install -r requirements.txt
4. Run the tests
  - To run tests using pytest and allure, use the following command:
     pytest --alluredir=reports/allure-results
5. Open the generated report
 - To open the generated allure report run the following command:
     allure serve reports/allure-results   



     
