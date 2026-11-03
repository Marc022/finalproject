import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",           
        database="archive_db"  
    )

def insert_item(cursor, item):
    sql = """
        INSERT INTO archive_items (archive_id, filename, size_bytes, checksum)
        VALUES (%s, %s, %s, %s)
    """
    values = (item["archive_id"], item["filename"], item["size_bytes"], item["checksum"])
    cursor.execute(sql, values)