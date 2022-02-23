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

In a separate shell, execute the following commands to load the data

`python transform.py` <- This transforms the data into 3 files we will use to bulk import

You will need the sqlite3 command line utility to complete the import step.  If you don't have it installed try installing it with the following commands:

Linux: `apt -y update && apt -y install sqlite3`

Mac: `Ships with machine :)`

Windows: download and install from `https://www.sqlite.org/download.html`

Enter the sqlite3 CLI and import the data by using the following commands:

```
sqlite3 app.db
sqlite> .mode ascii
sqlite> .separator "\t" "\n"
sqlite> .import company.csv company
sqlite> .import operator.csv operator
sqlite> .import relationship.csv company_operator
```
Ignore the `UNIQUE constraint failed` errors.  This just logs dupes getting cleaned out.
Note: This may be an oversight since the rows themselves are not duplicates, but I was instructed to use nm_socio as a unique key.  

Note `sqlite>` is just an illustration of the shell cursor.  It is not part of the command.

<h3>Example URLs to exercise the API</h3>

`http://127.0.0.1:5000/OperatorsByCompanyRegistrationId?RegistrationId=15103882000198`

`http://127.0.0.1:5000/CompaniesByOperatorName?OperatorName=TUANE%20SOUZA%20DE%20BRITO`

`http://127.0.0.1:5000/CompaniesAssociatedByOperator?RegistrationId=15103882000198`

<h3>Extra</h3>
The requested endpoints can have their data queried in multiple ways.
In app.py, I left the more performant queries in place and commented out the slower approach that utilizes joins.
The two queries might have similar performance on postgresql or other heavier databases because their optimizers
might create its own query execution plan, but since this toy project uses sqlite, I tinkered with the queries myself.