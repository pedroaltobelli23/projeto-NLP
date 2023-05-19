import sqlite3

#setting sqlite3 database
teste_db = "teste.db"
prod_db = "prod.db"

con = sqlite3.connect(prod_db)

cur = con.cursor()

# cur.execute('''
#     CREATE TABLE IF NOT EXISTS videos (
#     video_id TEXT PRIMARY KEY NOT NULL,
# 	title TEXT NOT NULL,
#     tags TEXT NOT NULL,
#     transcript TEXT NOT NULL
# );           
# ''')

a = cur.execute('''SELECT count(*) from videos''')
for row in a:
    print(row)
    
con.commit()
con.close()
