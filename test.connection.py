import pyodbc

server = 'LAPTOP-54KE79QD\\MSSQLSERVER01'
database = 'DictionaryDB'

try:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server};DATABASE={database};"
        f"Trusted_Connection=yes;Encrypt=no;"
    )
    print("Kết nối thành công!")
except pyodbc.Error as e:
    print(f"Lỗi kết nối: {e}")