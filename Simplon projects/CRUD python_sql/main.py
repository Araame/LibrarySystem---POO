import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",  
    password="Dieng",  
    database="testdb"
)
# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")




def create_user(name, email, age):
    cursor = connection.cursor()
    query = """
    INSERT INTO users (name, email, age) VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, email, age))
    connection.commit()
    print(f"User {name} added successfully.")


def read_users():
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def update_user(user_id, name=None, email=None, age=None):
    cursor = connection.cursor()
    updates = []
    if name:
        updates.append(f"name = '{name}'")
    if email:
        updates.append(f"email = '{email}'")
    if age:
        updates.append(f"age = {age}")
    
    if updates:
        query = f"UPDATE users SET {', '.join(updates)} WHERE id = {user_id}"
        cursor.execute(query)
        connection.commit()
        print(f"User with ID {user_id} updated successfully.")


def delete_user(user_id):
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print(f"User with ID {user_id} deleted successfully.")

delete_user(1)
read_users()

connection.close()
if not connection.is_connected():
    print("MySQL connection closed.")