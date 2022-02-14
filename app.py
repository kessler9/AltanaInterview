import json
from flask import Flask, request
from models import Company, Operator
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route("/OperatorsByCompanyRegistrationId", methods=['GET'])
def operators_by_company_registration_id():
    sub = Company.query.filter_by(registration_id=request.args['RegistrationId']).with_entities(Company.id).subquery()
    operators = Operator.query.filter(Operator.companies.any(Company.id.in_(sub))).all()
    return json.dumps([
        {"id": operator.id, "name": operator.name}
        for operator in operators
    ])


@app.route("/CompaniesByOperatorName", methods=['GET'])
def companies_by_operator_name():
    sub = Operator.query.filter_by(name=request.args['OperatorName']).with_entities(Operator.id).subquery()
    companies = Company.query.filter(Company.operators.any(Operator.id.in_(sub))).all()
    return json.dumps([
        {"id": company.id, "name": company.name}
        for company in companies
    ])


@app.route("/CompaniesAssociatedByOperator", methods=['GET'])
def companies_associated_by_operator():
    sub = Company.query.filter_by(registration_id=request.args['RegistrationId']).with_entities(Company.id).subquery()
    operators = Operator.query.filter(Operator.companies.any(Company.id.in_(sub))).with_entities(Operator.id).subquery()
    companies = Company.query.filter(Company.operators.any(Operator.id.in_(operators)))
    return json.dumps([
        {"id": company.id, "name": company.name}
        for company in companies
    ])
