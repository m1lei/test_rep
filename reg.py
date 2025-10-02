from sqlalchemy.orm import Session
from model import User

class UserRepo:
    def __init__(self, session: Session):
        self.session = session

    def add(self, name: str, email: str, password: str):
        user = User(name=name, email=email, password=password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_by_email(self, email):
        return self.session.query(User).filter_by(email=email).first()

    def logout(self, email, password:hash):
        user = self.session.query(User).filter_by(email=email).first()