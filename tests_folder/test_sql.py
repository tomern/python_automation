import pyodbc


def test_sql(app_config):
    conn = pyodbc.connect(app_config.connections['sql_local'])
    cursor = conn.cursor()
    cursor.execute("SELECT FirstName as name FROM [Northwind].[dbo].[Employees] WHERE EmployeeID = 7")
    row = cursor.fetchone()
    conn.close()
    assert 'Robert' == row[0]
