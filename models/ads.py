from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from datetime import datetime
from models.base import Base


class Ads(Base):
    __tablename__ = "ads"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    link_url = Column(String(500), nullable=True)
    position = Column(String(50), nullable=True)  # 廣告位置，如：homepage, sidebar 等
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Ads(id={self.id}, title='{self.title}', is_active={self.is_active})>"

