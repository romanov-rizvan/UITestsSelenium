# UITestsSelenium

## Prepare to run tests:

### Clone repo:

```commandline
git clone https://github.com/romanov-rizvan/UITestsSelenium.git
```

### Go to folder and create virtual environment:
```commandline
cd UITestsSelenium
python -m venv venv
```

### Activate virtual environment and install requirements:
```commandline
venv\Scripts\activate
pip install -r requirements.txt
```

## Run tests and get report:
### Activate virtual environment and install requirements:
```commandline
venv\Scripts\activate
```
### Run tests:
```commandline
pytest -v -s .\Tests\ --alluredir .\Allure\
```
### Generate Allure report:
```commandline
allure serve .\Allure\
```
