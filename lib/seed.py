#!/usr/bin/env python3

from models import Company, Dev, Freebie, session

company1 = Company(name="TechCorp2025", founding_year=2025)
company2 = Company(name="WolfTech", founding_year=2020)

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

freebie1 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sneakers", value=5, dev=dev2, company=company2)


session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()
