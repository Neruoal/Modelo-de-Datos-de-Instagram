from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
    
class OrderLine(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.order_id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }
    
class Order(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.customer.id'), nullable=False)
    total_amount: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    order_status_id: Mapped[int] = mapped_column(ForeignKey('order_status.order_status_id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "customer_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }
