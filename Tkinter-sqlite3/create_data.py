# import sqlite3
#
# # Connect to the SQLite database (creates a new database if it doesn't exist)
# conn = sqlite3.connect('login_credentials.db')
#
# # Create a cursor object to execute SQL queries
# cursor = conn.cursor()
#
# # Create a table to store email and password
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     email TEXT NOT NULL,
#                     password TEXT NOT NULL
#                 )''')
#
# # Commit changes and close the connection
# conn.commit()
# conn.close()
#---------------------------------------------------------------------

#
# import sqlite3
#
# conn=sqlite3.connect("login_credentials.db")
#
# # insert query
# # insert into student (st_id,st_name,st_class,st_email) VALUES
# ins='''
#     insert into users (email,password) VALUES
#     ('ankitshukla231211@gmail.com','ankit231001')
# '''
#
# # run/execute query
# conn.execute(ins)
#
# # to change the query using of commit() function
# conn.commit()
#
# # close connection
# conn.close()
#---------------------------------------------------------------------

'''
 PYTHON SQLITE

 DELETE QUERY FROM DATABASE
 *

'''


# [1] this for delete query from table from database

import sqlite3

def delete_user(email):
    conn = sqlite3.connect('requestsuit/login_credentials.db')
    cursor = conn.cursor()

    # Delete a user based on their email
    cursor.execute("DELETE FROM users WHERE email=?", (email,))

    conn.commit()
    conn.close()

# Example usage: delete a user with a specific email
delete_user('')
#---------------------------------------------------------------------


