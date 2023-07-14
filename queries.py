# pylint:disable=C0111,C0103



def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = '''SELECT DISTINCT OrderDetails.OrderID, ContactName, FirstName
FROM OrderDetails
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
JOIN Customers ON Customers.CustomerID = Orders.CustomerID
ORDER BY OrderDetails.OrderID'''

    db.execute(query)
    detailed_order = db.fetchall()
    return detailed_order

def spent_per_customer(db):

    query = '''SELECT Customers.ContactName, ROUND(SUM(OrderDetails.Quantity * OrderDetails.UnitPrice), 2) AS TotalAmount
            FROM Customers
            JOIN Orders ON Customers.CustomerID = Orders.CustomerID
            JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
            GROUP BY Customers.ContactName
            ORDER BY TotalAmount ASC;'''

    db.execute(query)
    detailed_order = db.fetchall()
    return detailed_order

def best_employee(db):

    query = """SELECT Employees.FirstName, Employees.LastName, SUM(OrderDetails.Quantity * OrderDetails.UnitPrice) AS TotalSales
        FROM Employees
        JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID
        JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        GROUP BY Employees.FirstName, Employees.LastName
        ORDER BY TotalSales DESC
        LIMIT 1"""
    db.execute(query)
    orders = db.fetchone()
    return orders

def orders_per_customer(db):

    query = '''SELECT Customers.ContactName, COUNT(Orders.OrderID) AS number_of_orders
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.ContactName
ORDER BY number_of_orders ASC;'''
    db.execute(query)
    orders  = db.fetchall()
    return orders
