from in_memory_queue import InMemoryQueue
from db import get_connection
from processor import process_queue

def main():  
    uploaded_batch = [
        {"archive_id": "file_001", "filename": "chester bading.zip", "size_bytes": 1024, "checksum": "abc123hash"},
        {"archive_id": "file_002", "filename": "chester badap.png",   "size_bytes": 2048, "checksum": "def456hash"},
        {"archive_id": "file_003", "filename": "chester scandal.mp4",   "size_bytes": 4096, "checksum": "ghi789hash"},
    ]

    queue = InMemoryQueue()
    queue.enqueue_batch(uploaded_batch)
    print(f"Queued {queue.size()} items for processing...\n")

    conn = get_connection()

    try:
        total_stored = process_queue(queue, conn)
        print(f"\nSuccessfully processed and inserted {total_stored} items into MySQL.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()