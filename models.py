from sqlalchemy.orm import relationship
from extensions import db


company_operator = db.Table('company_operator',
    db.Column('company_id', db.ForeignKey('company.id'), primary_key=True),
    db.Column('operator_id', db.ForeignKey('operator.id'), primary_key=True)
)


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    registration_id = db.Column(db.Integer, index=True)
    name = db.Column(db.String(128))
    state = db.Column(db.String(2))
    operators = relationship('Operator', secondary=company_operator, backref='companies')


class Operator(db.Model):
    __operator__ = 'operator'
    id = db.Column(db.Integer, primary_key=True)
    is_person = db.Column(db.Boolean)
    registration_id = db.Column(db.Integer)
    role_code = db.Column(db.Integer)
    role_description = db.Column(db.String(128))
    name = db.Column(db.String(128), index=True)
