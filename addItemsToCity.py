import sqlite3
 
con = sqlite3.connect('city.db')
 
cursorObj = con.cursor()

cursorObj.execute('create table if not exists Street(id integer, name text)')
 
data = [(1, "Улица Ярославская"), (2, "Улица Петина"), (3, "Окружное шоссе"), (4, "Улица Новгородска"), (5, "Пошехонское шоссе")]
 
cursorObj.executemany("INSERT INTO Street VALUES(?, ?)", data)
 
con.commit()