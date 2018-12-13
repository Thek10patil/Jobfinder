import sqlite3

conn = sqlite3.connect('user_info.db')


c.execute("""CREATE TABLE user(
				user_id
				first_name text

		)


	""")