from sqlalchemy import Column, Integer, String
from database import Base

class WardrobeItem(Base):
    __tablename__ = "wardrobe_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    name = Column(String)
    category = Column(String)
    color = Column(String)
    image_url = Column(String)
    season = Column(String)
    style_tags = Column(String)  # comma-separated tags like "casual,vintage"
