import json
from flask import Flask, request
from models import Company, Operator, company_operator
from extensions import db
# from sqlalchemy.orm import aliased
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route("/OperatorsByCompanyRegistrationId", methods=['GET'])
def operators_by_company_registration_id():
    operators = (
        Operator.query
        .join(company_operator)
        .join(Company)
        .filter(Company.registration_id == request.args['RegistrationId'])
    )
    print(operators)
    return json.dumps([
        {"id": operator.id, "name": operator.name}
        for operator in operators.all()
    ])


@app.route("/CompaniesByOperatorName", methods=['GET'])
def companies_by_operator_name():
    # companies = (
    #     Company.query
    #     .join(company_operator)
    #     .join(Operator)
    #     .filter(Operator.name == request.args['OperatorName'])
    # )
    companies = Company.query.filter(Company.id.in_(
        select(company_operator.c.company_id).where(company_operator.c.operator_id.in_(
            select(Operator.id).where(Operator.name == request.args['OperatorName'])
        ))
    ))
    print(companies)
    return json.dumps([
        {"id": company.id, "name": company.name}
        for company in companies.all()
    ])


@app.route("/CompaniesAssociatedByOperator", methods=['GET'])
def companies_associated_by_operator():
    # company_operator_2 = aliased(company_operator)
    # Company1 = aliased(Company)
    # Company2 = aliased(Company)
    # companies = (
    #     Company2.query
    #     .join(company_operator)
    #     .join(Operator)
    #     .join(company_operator_2)
    #     .join(Company1)
    #     .distinct(Company2.id)
    #     .filter(Company1.registration_id == request.args['RegistrationId'])
    # )
    companies = Company.query.filter(Company.id.in_(
        select(company_operator.c.company_id).where(company_operator.c.operator_id.in_(
            select(company_operator.c.operator_id).where(company_operator.c.company_id.in_(
                select(Company.id).where(Company.registration_id == request.args['RegistrationId'])
            ))
        ))
    )).distinct()
    print(companies)
    return json.dumps([
        {"id": company.id, "name": company.name}
        for company in companies.all()
    ])
