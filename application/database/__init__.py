from .models import Account, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from application.config import DATABASE_URI

engine = create_engine(DATABASE_URI)
BaseModel.metadata.create_all(engine)

session = Session(engine)

