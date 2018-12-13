import sqlite3

conn = sqlite3.connect('user_login.db')

c = conn.cursor();

c.execute("""CREATE TABLE user_login(
				user_id NOT NULL integer ,
				user_name NOT NULL text PRIMARY KEY,
				password text,
				PRIMARY KEY(user_name)
								);
		""");

conn.commit();

conn.close();