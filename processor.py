import mysql.connector
from db import insert_item

def process_queue(queue, conn):
    cursor = conn.cursor()
    processed_count = 0
    skipped_count = 0
    
    while not queue.is_empty():
        item = queue.dequeue()
        try:
            insert_item(cursor, item)
            conn.commit()
            processed_count += 1
            print(f"[✓] Stored: {item['archive_id']}")
            
        except mysql.connector.IntegrityError:
            conn.rollback()
            skipped_count += 1
            print(f"[-] Skipped (already exists): {item['archive_id']}")
            
        except mysql.connector.Error as err:
            conn.rollback()
            print(f"[X] Failed to store {item['archive_id']}: {err}")

    cursor.close()
    print(f"\nTotal new items: {processed_count} | Duplicates skipped: {skipped_count}")
    return processed_count