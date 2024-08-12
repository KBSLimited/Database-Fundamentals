+----------------+        +----------------+        +----------------+
|    Authors     |        |     Books      |        |   Customers    |
+----------------+        +----------------+        +----------------+
| PK author_id   |<-----+ | PK book_id     |        | PK customer_id |
| first_name     |        | title          |        | first_name     |
| last_name      |        | FK author_id   |        | last_name      |
| birth_date     |        | isbn           |        | email          |
+----------------+        | published_year |        | phone_number   |
                         | price          |        | address        |
                         | stock_quantity |        +----------------+
                         +--------+-------+
                                  |
                                  |
                                  |
                                  |
                         +--------v-------+
                         |  Transactions  |
                         +----------------+
                         | PK transaction_id |
                         | FK customer_id    |
                         | FK book_id        |
                         | transaction_date  |
                         | quantity          |
                         | total_amount      |
                         +------------------+

                         Explanation
                         Authors Table:
                         
                         Primary Key: author_id
                         Attributes: first_name, last_name, birth_date
                         Relationships:
                         Books: One-to-Many (One author can write multiple books)
                         Books Table:
                         
                         Primary Key: book_id
                         Foreign Key: author_id (references Authors.author_id)
                         Attributes: title, isbn, published_year, price, stock_quantity
                         Relationships:
                         Authors: Many-to-One (Multiple books can be written by one author)
                         Transactions: One-to-Many (One book can appear in multiple transactions)
                         Customers Table:
                         
                         Primary Key: customer_id
                         Attributes: first_name, last_name, email, phone_number, address
                         Relationships:
                         Transactions: One-to-Many (One customer can make multiple transactions)
                         Transactions Table:
                         
                         Primary Key: transaction_id
                         Foreign Keys: customer_id (references Customers.customer_id), book_id (references Books.book_id)
                         Attributes: transaction_date, quantity, total_amount
                         Relationships:
                         Customers: Many-to-One (Many transactions can be associated with one customer)
                         Books: Many-to-One (Many transactions can be associated with one book)                        