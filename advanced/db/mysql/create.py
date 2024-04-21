# https://pypi.org/project/mysql-connector-python/
# https://docs.sqlalchemy.org/en/20/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector
# pip install SQLAlchemy
# pip install mysql-connector-python
from sqlalchemy.ext.asyncio import create_async_engine
engine = create_async_engine("mysql+mysqlconnector://root:123456@localhost:3306/lilutest")

