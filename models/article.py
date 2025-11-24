from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base


class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text, nullable=True)
    summary = Column(String(500), nullable=True)
    image_url = Column(String(500), nullable=True)
    author = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey("article_categories.id"), nullable=True, index=True)
    is_active = Column(Boolean, default=True)
    view_count = Column(Integer, default=0)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 關聯
    category = relationship("ArticleCategory", back_populates="articles")
    
    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}', is_active={self.is_active})>"

