# SQLAlchemy with Postgres

Connnecting

establishing a connection with the PostgreSQL database by creating an engine object using the create_engine() function of SQLAlchemy.

```python
from sqlalchemy import create_engine

engine = create_engine(dialect+driver://username:password@host:port/database_name)
```

**Parameters:**

- **dialect –** Name of the DBMS. The dialect is the system SQLAlchemy uses to communicate with various types of DBAPIs and databases like PostgreSQL, MySQL, MS SQL, etc.
- **driver –** Name of the DB API that moves information between SQLAlchemy and the database.
- **Username** – Name of the admin
- **Password** – Password of the admin
- **host** – Name of the host in which the database is hosted
- **port** – port number through which the database can be accessed
- **database_name**– Name of the database

Hashing Password with urlib

```python
import urllib.parse
 
urllib.parse.quote_plus("your_password")
```

\#TODO:

Try Using .env password with dotenv module

---

Psycopg2

PostgreSQL supports a list of python drivers like psycopg2, psycopg, py8000, asyncpg, and psycopg2cffi, which facilitates communication between the database and SQLAlchemy.

```python
from sqlalchemy import create_engine
 
engine = create_engine('postgresql+psycopg2://user:password\
@hostname/database_name')
```

Connecting to Postgres with Psycopg2

```python
import psycopg2
 
# declare the connection string specifying
# the host name database name use name
# and password
conn_string = "host='host_name' dbname='database_name'\
user='user_name' password='your_password'"
 
# use connect function to establish the connection
conn = psycopg2.connect(conn_string)
```

