from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 创建数据库引擎，这里以 SQLite 为例
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

# 创建 Session 类型
Session = sessionmaker(bind=engine)


# 创建一个新的 session 实例
session = Session()

try:
    # 添加新用户
    new_user = User(name="Alice", age=30)
    session.add(new_user)
    
    new_user = User(name="Bob", age=30)
    session.add(new_user)
    
    # 假设我们还要更新另一个用户的信息
    user = session.query(User).filter_by(name="Bob").first()
    if user:
        user.age = 28
    # 提交事务
    session.commit()
    print("Transaction committed successfully.")
except Exception as e:
    # 如果在事务过程中出现错误，回滚所有更改
    session.rollback()
    print("Transaction failed. Rolled back.", str(e))
finally:
    # 关闭 session
    session.close()
