import sqlite3

class Slender_Todo:
	def __init__(self):
		self.version = 0.1
		self.table_name = "todo"
		self.connection = sqlite3.connect("notes-todo.db")
		self.curser = self.connection.cursor()

		# sqlite automatically creates a "primary key integer autoincrement" column called rowid
		# so we only create these two cols
		self.curser.execute("CREATE TABLE IF NOT EXISTS todo (status TEXT, note TEXT)")

	def print_version(self):
		print("sl-todoer version {}".format(self.version))

	def select_all(self, status):
		# we have to explicitly include rowid otherwise it won't show up
		# TODO: clean up and prettify result printing
		res = None

		if status == "all":
			res = self.curser.execute("SELECT rowid, * FROM todo")
		elif status == "not-done":
			res = self.curser.execute("SELECT rowid, * FROM todo WHERE status = 'not done'")
		elif status == "done":
			res = self.curser.execute("SELECT rowid, * FROM todo WHERE status = 'done'")

		for item in res.fetchall():
			print("{}. {} - {}".format(item[0], item[1], item[2]))

	def add(self, note):
		# doing it this way instead of text formatting to avoid sql injection attacks
		data = ("not done", note)

		self.curser.execute("""
			INSERT INTO todo (status, note)
			VALUES (?, ?)
		""", data)
		self.connection.commit()

	def make_done(self, id):
		self.curser.execute("""
			UPDATE todo
			SET status = 'done'
			WHERE rowid = ?
		""", (id))
		self.connection.commit()

	def delete(self, id):
		self.curser.execute("""
			DELETE FROM todo
			WHERE rowid = ?
		""", (id))
		self.connection.commit()

	def delete_done(self):
		self.curser.execute("""
			DELETE FROM todo
			WHERE status = 'done'
		""")
		self.connection.commit()
