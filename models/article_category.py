from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base


class ArticleCategory(Base):
    __tablename__ = "article_categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True)
    slug = Column(String(100), nullable=True, unique=True, index=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 關聯
    articles = relationship("Article", back_populates="category")
    
    def __repr__(self):
        return f"<ArticleCategory(id={self.id}, name='{self.name}')>"

