import sqlite3
import os

class Slender_Todo:
	def __init__(self):
		self.version = 1.1
		self.table_name = "todo"

		# create the directory - this doesn't fail even if it exists (kinda mkdir -p)
		# expanduser is necessary to process relative paths and "~"
		os.makedirs(os.path.expanduser("~/.local/share/todoer"), exist_ok=True)
		path = os.path.expanduser("~/.local/share/todoer/notes-todo.db")
		
		self.connection = sqlite3.connect(path)
		self.curser = self.connection.cursor()

		# sqlite automatically creates a "primary key integer autoincrement" column called rowid
		# so we only create these two cols
		self.curser.execute("CREATE TABLE IF NOT EXISTS todo (status TEXT, note TEXT)")

	def print_version(self):
		print("sl-todoer version {}".format(self.version))

	# helper function to verify that the input given by user is just ids
	# used in make_done and delete functions
	def get_ids(self, argids):
		for id in argids:
			if not id.isnumeric():
				return False

		return [int(id) for id in argids]

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
			print("{}. {}: {}".format(item[0], item[1], item[2]))

	def add(self, argnew):
		sNewItem = ""

		# if the user input was not put between ""
		if len(argnew) > 1:
			sNewItem = " ".join(argnew)
		else:
			sNewItem = argnew[0]

		# doing it this way instead of text formatting to avoid sql injection attacks
		data = ("not done", sNewItem)

		self.curser.execute("""
			INSERT INTO todo (status, note)
			VALUES (?, ?)
		""", data)
		self.connection.commit()

	def make_done(self, argids):
		ids = self.get_ids(argids)

		if ids == False:
			print("Incorrect input. Please input only numeric IDs")
			return -1

		self.curser.executemany("UPDATE todo SET status = 'done' WHERE rowid = ?", ((id,) for id in ids))
		self.connection.commit()

	def delete(self, argids):
		ids = self.get_ids(argids)

		if ids == False:
			print("Incorrect input. Please input only numeric IDs")
			return -1

		self.curser.executemany("DELETE FROM todo WHERE rowid = ?", ((id,) for id in ids))
		self.connection.commit()

	def delete_multi(self, status):
		if status == "all":
			self.curser.execute("DELETE FROM todo")
		elif status == "not-done":
			self.curser.execute("DELETE FROM todo WHERE status = 'not done'")
		elif status == "done":
			self.curser.execute("DELETE FROM todo WHERE status = 'done'")

		self.connection.commit()
