#!/usr/bin/env python3

from sqlalchemy import create_engine

from models import Company, Dev, Freebie, session

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    import ipdb; ipdb.set_trace()

companies = session.query(Company).all()
for company in companies:
    print(company.name, company.devs)

devs = session.query(Dev).all()
for dev in devs:
    print(dev.name, dev.companies)