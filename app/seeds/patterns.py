from app.models import db, Pattern, environment, SCHEMA
from sqlalchemy.sql import text

def seed_patterns():
    demos_pattern = Pattern(
      pattern_title="Test Pattern",
      title_image="image.com",
      difficulty="easy"
    )
