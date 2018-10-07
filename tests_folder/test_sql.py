import pyodbc

pyodbc.pooling = False


def test_sql(app_config):
    conn = pyodbc.connect(app_config.connections['sql_local'])
    cursor = conn.cursor()
    cursor.execute("SELECT FirstName, LastName "
                   "FROM [Northwind].[dbo].[Employees] "
                   "WHERE EmployeeID = 7")
    first_name, last_name = cursor.fetchone()
    conn.close()
    assert first_name == 'Robert' and last_name == 'King'
