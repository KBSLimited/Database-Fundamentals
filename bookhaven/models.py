from sqlalchemy import create_engine, Column, Integer, String, Decimal, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Create a base class for declarative models
Base = declarative_base()

# Define the Authors table
class Author(Base):
    __tablename__ = 'authors'
    
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=True)

    # Relationship to Book
    books = relationship('Book', back_populates='author')

# Define the Books table
class Book(Base):
    __tablename__ = 'books'
    
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.author_id'), nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    published_year = Column(Integer, nullable=False)
    price = Column(Decimal(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    # Relationship to Author and Transaction
    author = relationship('Author', back_populates='books')
    transactions = relationship('Transaction', back_populates='book')

# Define the Customers table
class Customer(Base):
    __tablename__ = 'customers'
    
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(15), nullable=True)
    address = Column(String(255), nullable=True)

    # Relationship to Transaction
    transactions = relationship('Transaction', back_populates='customer')

# Define the Transactions table
class Transaction(Base):
    __tablename__ = 'transactions'
    
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.book_id'), nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Decimal(10, 2), nullable=False)

    # Relationships to Customer and Book
    customer = relationship('Customer', back_populates='transactions')
    book = relationship('Book', back_populates='transactions')
