import pyodbc

def get_connection():
    server = 'LAPTOP-54KE79QD\\MSSQLSERVER01'  # Thay bằng server của bạn
    database = 'DictionaryDB'
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection=yes;"
            f"Encrypt=no;"
        )
        return conn
    except pyodbc.Error as e:
        print(f"Lỗi kết nối database: {e}")
        return None
