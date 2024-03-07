from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import Date
from .database import Base # database.pyで作成した変数

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Room(Base):
    __tablename__ = 'rooms'

    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, index=True)
    capacity = Column(Integer)

class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, index=True)
    # usersテーブルのuser_idと紐付ける
    # ondelete : 親テーブルのデータが削除されたときの挙動
    # SET NULL : 親テーブルのデータが削除されたとき、子テーブルのデータをNULLにする
    # nullable : Nullを許容するか設定
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
    # roomsテーブルのroom_idと紐付ける
    room_id = Column(Integer, ForeignKey("rooms.room_id", ondelete='SET NULL'), nullable=False)
    booked_num = Column(Integer, nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)