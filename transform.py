from csv import DictReader
from time import time

if __name__ == '__main__':
    ts = time()
    fh = open('ReceitaFederal_QuadroSocietario.csv')
    company_table = open('company.csv', 'w+')
    operator_table = open('operator.csv', 'w+')
    relationship_table = open('relationship.csv', 'w+')
    reader = DictReader(fh, delimiter='\t')
    companies = {}
    operators = {}
    company_id = operator_id = 1
    for row in reader:
        if row['nr_cnpj'] not in companies:
            company_table.write('\t'.join([
                str(company_id),
                row['nr_cnpj'].strip(),
                row['nm_fantasia'].strip(),
                row['sg_uf'].strip()
            ]) + '\n')
            companies[row['nr_cnpj']] = company_id
            company_id += 1
        if row['nm_socio'] not in operators:
            operator_table.write('\t'.join([
                str(operator_id),
                str(1 if row['in_cpf_cnpj'] == '2' else 0),
                row['nr_cpf_cnpj_socio'].strip(),
                row['cd_qualificacao_socio'].strip(),
                row['ds_qualificacao_socio'].strip(),
                row['nm_socio'].strip()
            ]) + '\n')
            operators[row['nm_socio']] = operator_id
            operator_id += 1
        relationship_table.write('\t'.join([str(companies[row['nr_cnpj']]), str(operators[row['nm_socio']])]) + '\n')
    fh.close()
    company_table.close()
    operator_table.close()
    relationship_table.close()
    print(f'Transform completed in {round(time() - ts)}s')
