import datetime as datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, VARCHAR, Date, Boolean, Float, TIMESTAMP
from sqlalchemy.orm import declarative_base
Base = declarative_base()


SQLALCHEMY_DATABASE_URI = f"postgresql://test1_user:qwerty123!@52.78.214.236:5432/test1"


class Currency(Base):
    __tablename__ = 'currency2'
    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    currency = Column(VARCHAR(50), nullable=False)
    value = Column(Float, nullable=False)
    currate_date = Column(TIMESTAMP, nullable=False, index=True)


engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_local = SessionLocal()

new_record = Currency(
    currency='EUR',
    value=2.222,
    currate_date=datetime.datetime.utcnow()
)
new_record2 = Currency(
    currency='RUB',
    value=3.333,
    currate_date=datetime.datetime.utcnow()
)

session_local.add(new_record)
session_local.add(new_record2)

session_local.commit()
