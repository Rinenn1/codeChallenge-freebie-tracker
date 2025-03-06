# #!/usr/bin/env python3


from models import Base, Company, Dev, Freebies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database engine and session
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Companies
company1 = Company(name="TechStar", founding_year=2022)
company2 = Company(name="WolfTech", founding_year=2012)

# Devs
dev1 = Dev(name="John Stewart")
dev2 = Dev(name="Peter Calvin")

# Adding the companies and devs to the session
session.add_all([company1, company2, dev1, dev2])
session.commit()

# Freebies
freebie1 = Freebies(item_name="Jordans", value=20, company=company1, dev=dev1)
freebie2 = Freebies(item_name="Asus Gaming Laptop", value=200, company=company2, dev=dev2)


session.add_all([freebie1, freebie2])
session.commit()


print(freebie1.print_details())


print(dev1.received_one("Jordans"))
print(dev1.received_one("T-shirt"))


dev1.give_away(dev2, freebie1)
session.commit()


print(freebie1.dev.name) 


oldest = Company.oldest_company()
print(oldest.name) 