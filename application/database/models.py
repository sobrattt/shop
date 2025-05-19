from sqlalchemy import Column, String, Integer,Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship


class BaseModel(DeclarativeBase):
    pass

class Account(BaseModel):
    __tablename__ = "Accounts"
    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    email = Column(String, unique=True, nullable=True)

class Item(BaseModel):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    shop_name = Column(Text, nullable=False)
    item_link = Column(Text, nullable=False, unique=True)
    item_price = Column(Text, nullable=False)
    item_name = Column(Text, nullable=False)
    images = relationship("Image", back_populates="item", cascade="all, delete-orphan")

class Image(BaseModel):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    item_image = Column(Text, nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", back_populates="images")

