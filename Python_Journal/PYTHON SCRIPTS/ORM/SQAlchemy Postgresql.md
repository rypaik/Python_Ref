# SQAlchemy Postgresql

[SQLAlchemy ORM — a more “Pythonic” way of interacting with your database](https://medium.com/dataexplorations/sqlalchemy-orm-a-more-pythonic-way-of-interacting-with-your-database-935b57fd2d4d)

[Using PostgreSQL through SQLAlchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/)

[SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

[https://docs.sqlalchemy.org/en/14/index.html](https://docs.sqlalchemy.org/en/14/index.html)

[Automatically generating SQLAlchemy models — #22](https://medium.com/lambert-labs/automatically-generating-sqlalchemy-models-22-37d5959e22f9?source=read_next_recirc---------0---------------------9a469e54_af20_4643_a338_a6bcb9767ded----------)

```python
.
├── config.py
├── .env
├── modules
└──
```

[https://github.com/ag2816/TorontoWalks/blob/master/torontowalks/models.py](https://github.com/ag2816/TorontoWalks/blob/master/torontowalks/models.py)

RAW SQL with

```python
from sqlalchemy import create_engine


db = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME}')


# create main table
db.execute("""
CREATE TABLE IF NOT EXISTS points_of_interest (poi_id BIGSERIAL PRIMARY KEY,
    name text,
    build_year text, demolished_year text,
    address text, latitude float, longitude float,
    source text, external_url text, details text,
    image_url text, heritage_status text, current_use text,
    poi_type text)
""")

# create architectural styles TABLE
db.execute("""
CREATE TABLE IF NOT EXISTS architectural_styles (poi_id int,style text
)
 """)

# create architects TABLE
db.execute("""
CREATE TABLE IF NOT EXISTS architects (poi_id int ,
        architect_name text
)
""")

# create categories TABLE
db.execute("""
CREATE TABLE IF NOT EXISTS poi_categories (poi_id int,
    category text
)
""")
```

SQLAlchemy ORM

Creating Tables as Classes

```python
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backreffrom sqlalchemy.sql import *


# Tables as Classes
Base = declarative_base()class PointsOfInterest(Base):
    __tablename__ = "points_of_interest"
    poi_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)
...
```

Creating the foreign key tables

```python
from sqlalchemy import PrimaryKeyConstraintclass ArchitecturalStyles(Base):
    __tablename__="architectural_styles"
    __table_args__ = (
        PrimaryKeyConstraint('poi_id', 'style'),
    )
    poi_id =Column(Integer)
    style = Column(String)
```

One to Many Relationship Pattern / Foreign Key

```python
class ArchitecturalStyles(Base):
    __tablename__="architectural_styles"
    __table_args__ = (
        PrimaryKeyConstraint('poi_id', 'style'),
    )
    poi_id =Column(Integer,ForeignKey('points_of_interest.poi_id'))
    #Defining the Foreign Key on the Child Table
    style = Column(String)




class PointsOfInterest(Base):
    __tablename__ = "points_of_interest"
    poi_id = Column(Integer, Sequence('poi_id_seq'), primary_key=True)
    ...
    details = Column(String)
    #Defining One to Many relationship
    styles = relationship('ArchitecturalStyles', backref = 'points_of_interest',lazy=True,cascade="all, delete-orphan")
```

Execute Table Creation

```python
engine = connect_db()
PointsOfInterest.__table__.create(bind=engine, checkfirst=True)
```

Full Table Creation Code

```python
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backreffrom sqlalchemy.sql import *
import os
from dotenv import load_dotenv, find_dotenvload_dotenv(find_dotenv())
# load environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
DB_USER=os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DEBUG= os.getenv("DEBUG")
DB_NAME=os.getenv("DB_NAME")
DB_SERVICE=os.getenv("DB_SERVICE")
DB_PORT=os.getenv("DB_PORT")
DB_IP=os.getenv("DB_IP")def connect_db():
    #_load_db_vars()
    # create db create_engine
    db = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_NAME}')
    return dbBase = declarative_base()class PointsOfInterest(Base):
    __tablename__ = "points_of_interest"
    poi_id = Column(Integer, Sequence('poi_id_seq'), primary_key=True)
    name = Column(String)
    build_year = Column(String)
    demolished_year = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    external_url = Column(String)
    image_url = Column(String)
    heritage_status = Column(String)
    current_use = Column(String)
    poi_type = Column(String)
    source = Column(String)
    details = Column(String)
    #Defining One to Many relationships with the relationship function on the Parent Table
    styles = relationship('ArchitecturalStyles', backref = 'points_of_interest',lazy=True,cascade="all, delete-orphan")
    architects = relationship('Architects', backref = 'points_of_interest', lazy=True,cascade="all, delete-orphan")
    categories = relationship('POICategories', backref = 'points_of_interest', lazy=True,cascade="all, delete-orphan")class ArchitecturalStyles(Base):
    __tablename__="architectural_styles"
    __table_args__ = (
        PrimaryKeyConstraint('poi_id', 'style'),
    )
    poi_id =Column(Integer,ForeignKey('points_of_interest.poi_id'))
    #Defining the Foreign Key on the Child Table
    style = Column(String)class Architects(Base):
    __tablename__="architects"
    __table_args__ = (
        PrimaryKeyConstraint('poi_id', 'architect_name'),
    )
    poi_id= Column(Integer,ForeignKey('points_of_interest.poi_id'))
    architect_name = Column(String)class POICategories(Base):
    __tablename__="poi_categories"
    __table_args__ = (
        PrimaryKeyConstraint('poi_id', 'category'),
    )
    poi_id =Column(Integer,ForeignKey('points_of_interest.poi_id'))
    category = Column(String)engine = connect_db()
PointsOfInterest.__table__.create(bind=engine, checkfirst=True)
ArchitecturalStyles.__table__.create(bind=engine, checkfirst=True)
Architects.__table__.create(bind=engine, checkfirst=True)
POICategories.__table__.create(bind=engine, checkfirst=True)
```

## Using SQL Alchemy ORM

**Inserting Rows**

Now that my classes were defined, I could use them in other modules to help load data. As usual, the first step is to import the necessary classes, including our new class definitions (PointsOfInterest etc) and establish a session:

The following function saves data from a dataframe to the database.

```python
from models import connect_db, PointsOfInterest, ArchitecturalStyles, Architects,POICategories

db=connect_db() #establish connection

Session = session maker(bind=db)

session = Session()
```

Updates three tables: points_of_interest, architectural_styles, architects
In this case, each Point of Interest only has only architectural style, so I define an instance of the ArchitecturalStyles class ( style=ArchitecturalStyles(style=row['Style'])) and then append that to the Point of Interest class ( poi.styles.append(style) . Now when I commit this transaction, the entry in ArchitecturalStyles will automatically be assigned the new poi_id generated in the main table)
Similarly, there may be many architects, so I loop through the list and append one or more Architects instances to the Point of Interest

def save_to_database_ORM(session):

for index, row in bld_df.iterrows():        poi_dict={'name': row['Name'],address=row['Street']}

...        poi = PointsOfInterest(**poi_dict )        # define style (in ArchitecturalStyles class)
style=ArchitecturalStyles(style=row['Style'])
poi.styles.append(style)

\# architects (can be multiple)
for company in row['Companies']:
architect = Architects(architect_name= company)
poi.architects.append(architect)

session.add(poi)
session.commit()

Accessing data

More details can be found in the help docs, but here are a few quick tips on accessing data through SQLAlchemy ORM:

Get Count of rows in table

# get the count

session.query(PointsOfInterest).count()

get an object by primary key

poi= session.query(PointsOfInterest).get(30)

filter on particular column/value

session.query(PointsOfInterest).filter(PointsOfInterest.build_year=='1905')

load to pandas dataframe

df = pd.read_sql(session.query(PointsOfInterest).statement, session.bind)

access linked table — because of the defined relationship, you can access a styles and architects list for each PointsOfInterest object

poi= session.query(PointsOfInterest).get(30)

for y in poi.architects:
print(y.architect_name)

delete entry (cascades to linked tables, so if this point has an associated entry in the Architects table, it will be deleted too)

poi_to_delete = session.query(PointsOfInterest).filter(PointsOfInterest.poi_id==).first()

session.delete(poi_to_delete)

session.commit()

