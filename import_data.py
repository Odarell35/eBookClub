""" sql connection """
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('instance/eBook_db.db')
    cur = conn.cursor()

    cur.execute("UPDATE books SET img_link = '../../static/styles/images/Warlord.jpeg' WHERE id = 40;")
conn.commit()
cur.close()
conn.close()

