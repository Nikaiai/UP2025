from flask import Flask, render_template, abort
import mysql.connector

app = Flask(__name__)

# Настройка подключения к базе данных
db_config = {
    'host': 'localhost',
    'user': 'adr',  # замените на ваше имя пользователя
    'password': 'adr',  # замените на ваш пароль
    'database': 'ComputerStore'  # замените на имя вашей базы данных
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers')
def customers():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Получение данных из таблицы customers
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('customers.html', rows=rows)


@app.route('/orders')
def orders():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Получение данных из таблицы Orders
    cursor.execute("SELECT * FROM Orders")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('orders.html', rows=rows)


@app.route('/categories')
def categories():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Получение данных из таблицы Categories
    cursor.execute("SELECT * FROM Categories")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('categories.html', rows=rows)


@app.route('/orderdetails')
def orderdetails():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Получение данных из таблицы OrderDetails
    cursor.execute("SELECT * FROM OrderDetails")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('orderdetails.html', rows=rows)


@app.route('/products')
def products():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Получение данных из таблицы Products
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('products.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)

