from sqlalchemy import create_engine, orm
from models import Company, Operator
from csv import DictReader


def get_session():
    return orm.sessionmaker(bind=create_engine('sqlite:///app.db'))()


if __name__ == '__main__':
    with get_session() as session, open('ReceitaFederal_QuadroSocietario.csv') as fh:
        reader = DictReader(fh, delimiter='\t')
        i = 0
        for row in reader:
            company = session.query(Company).filter_by(registration_id=row['nr_cnpj']).first()
            if not company:
                company = Company(
                    registration_id=row['nr_cnpj'],
                    name=row['nm_fantasia'],
                    state=row['sg_uf']
                )
                session.add(company)
            operator = Operator(
                is_person=row['in_cpf_cnpj'] == '2',
                registration_id=row['nr_cpf_cnpj_socio'],
                role_code=row['cd_qualificacao_socio'],
                role_description=row['ds_qualificacao_socio'],
                name=row['nm_socio']
            )
            company.operators.append(operator)
            session.add(operator)
            session.add(company)
            i += 1
            if i == 10000:
                break
        session.commit()
