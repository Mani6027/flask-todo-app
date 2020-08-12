from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ENUM, UUID
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from uuid import uuid4

DB = SQLAlchemy()

TASK_STATUS = ENUM('completed', 'not-completed')

# Model for user.
class User(UserMixin, DB.Model):
    __tablename__ = 'account'

    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)


# Model for user's task.
class Todo(DB.Model):
    __tablename__ = 'todo'

    id = Column(UUID(as_uuid=True), primary_key=True)
    task_name = Column(String, nullable=False)
    status = Column(TASK_STATUS, nullable=False)
    email = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)