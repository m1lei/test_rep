from model import SessionLocal
from reg import UserRepo
import auth

class DbManager:
    def __init__(self):
        self.repo = None
        pass

    def add(self,name:str,email,password:str ):
        with SessionLocal() as session:
            self.repo = UserRepo(session)
            if self.repo.get_by_email(email):
                return None
            pass_hash = auth.has_password(password)
            new = self.repo.add(name,email,pass_hash)
            return new

    def logout(self, email, password):
        with SessionLocal() as session:
            self.repo = UserRepo(session)
            user = self.repo.get_by_email(email)
            if user is None:
                return None
            return auth.verify_password(user.password, auth.has_password(password))