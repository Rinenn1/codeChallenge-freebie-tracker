from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


#freebies table
class Freebies(Base):
    __tablename__='freebies'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer())

    dev_id = Column(Integer(), ForeignKey('devs.id'))
    dev = relationship('Dev', back_populates='freebies', foreign_keys="[Freebies.dev_id]")

    company_id = Column(Integer(), ForeignKey('companies.id'))
    company = relationship('Company', back_populates='freebies', foreign_keys="[Freebies.company_id]")

    def __repr__(self):
        return f"<Freebies {self.item_name} {self.value}>"
    
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"


#companies table
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebies', back_populates='company')
    devs = relationship('Dev', secondary='freebies', viewonly=True)

    def __repr__(self):
        return f'<Company {self.name}>'
    
    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year.asc()).first()
    
    def give_freebie(self, dev, item_name, value):
        freebie = Freebies(
            item_name = item_name,
            value = value,
            dev = dev,
            company = self
        )
        return freebie

#devs table
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebies', back_populates='dev')
    companies = relationship('Company', secondary='freebies', viewonly=True)

    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, recipient_dev, freebie):
        if freebie.dev_id != self.id:
            raise ValueError("Cannot give away a freebie that doesn't belong to you")
        
        freebie.dev = recipient_dev
        return True
    
    