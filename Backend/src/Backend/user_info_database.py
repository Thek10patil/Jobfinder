import sqlite3

conn = sqlite3.connect('user_info.db')

c = conn.cursor();

c.execute("""CREATE TABLE user(
				user_id NOT NULL integer PRIMARY KEY,
				first_name text,
				last_name text,
				contact_number integer,
				email_id text,
				gender text,

				PRIMARY KEY(user_id)
								);
		""");

conn.commit();

conn.close();