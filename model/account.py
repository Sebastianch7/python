from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, BigInteger
from config.db import engine, metadata

modelAccount = Table("accounts", metadata, 
                Column("numberid", BigInteger, nullable=True, primary_key=True),
                Column("name", String(255), nullable=True),
                Column("accountid", BigInteger, nullable=True),
                Column("current", BigInteger, nullable=True),
                )

metadata.create_all(engine)