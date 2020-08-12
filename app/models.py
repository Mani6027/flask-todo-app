from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.orm import relationship

DB = SQLAlchemy()

TASK_STATUS = ENUM('completed', 'not-completed')

# Model for user.
class User(UserMixin, DB.Model):
    __tablename__ = 'account'

    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)


# Model for user's task.
class Todo(DB.Model):
    __tablename__ = 'todo'

    id = Column(UUID(as_uuid=True), primary_key=True)
    task_name = Column(Text, nullable=False)
    status = Column(TASK_STATUS, nullable=False)
    email = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
