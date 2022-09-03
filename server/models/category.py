from db import db


class CategoryModel(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    products = db.relationship("ProductsModel", backref="category", lazy="select")
