from .db import db, environment, SCHEMA, add_prefix_for_prod


class Pattern(db.Model):
    __tablename__='patterns'

    if environment == 'production':
        __table_arga__ = {'schema' : SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    pattern_title=db.Column(db.String(100), nullable=False)
    