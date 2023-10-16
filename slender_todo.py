import sqlite3

class Slender_Todo:
	def __init__(self):
		self.connection = sqlite3.connect("notes-todo.db")
		self.curser = self.connection.cursor()

		# sqlite automatically creates a "primary key integer autoincrement" column called rowid
		# so we only create these two cols
		self.curser.execute("CREATE TABLE IF NOT EXISTS todo (status TEXT, note TEXT)")

	def select_all(self):
		# we have to explicitly include rowid otherwise it won't show up
		res = self.curser.execute("SELECT rowid, * FROM todo")
		print(res.fetchall())

	def add(self, note):
		# doing it this way instead of text formatting to avoid sql injection attacks
		data = ("not done", note)

		self.curser.execute("""
			INSERT INTO todo (status, note)
			VALUES (?, ?)
		""", data)
		self.connection.commit()
