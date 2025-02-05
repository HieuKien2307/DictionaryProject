from database import get_connection

def report_word_usage():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("""
        SELECT w.word, ud.view_count, ud.search_count
        FROM Words w
        JOIN UserDictionary ud ON w.word_id = ud.word_id
    """)
    results = cursor.fetchall()
    conn.close()

    for row in results:
        print(f"Từ: {row[0]}, Lượt xem: {row[1]}, Lượt tìm kiếm: {row[2]}")
def report_most_searched_words():
    """Thống kê các từ được tìm kiếm nhiều nhất."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("""
        SELECT w.word, COUNT(ws.action) AS search_count
        FROM Words w
        JOIN WordStats ws ON w.word_id = ws.word_id
        WHERE ws.action = 'search'
        GROUP BY w.word
        ORDER BY search_count DESC
    """)

    results = cursor.fetchall()
    conn.close()

    if results:
        print("\nTừ được tìm kiếm nhiều nhất:")
        for row in results:
            print(f"Từ: {row[0]} | Số lần tìm kiếm: {row[1]}")
    else:
        print("Chưa có thống kê tìm kiếm.")
