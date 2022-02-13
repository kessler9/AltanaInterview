# AltanaInterview

<h3>Installation Instructions:</h3>

If you don't already have virtualenv installed, run:

`python3 -m pip install --user virtualenv`

Copy ReceitaFederal_QuadroSocietario.csv into the source directory

In source directory, run:

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`flask run` <-- this creates a sqlite database and starts the API

In a separate shell, execute the following to load some data

`python import.py`

<h3>Example URLs to exercise the API</h3>

`http://127.0.0.1:5000/OperatorsByCompanyRegistrationId?RegistrationId=15103882000198`

`http://127.0.0.1:5000/CompaniesByOperatorName?OperatorName=TUANE%20SOUZA%20DE%20BRITO`

`http://127.0.0.1:5000/CompaniesAssociatedByOperator?RegistrationId=15103882000198`

