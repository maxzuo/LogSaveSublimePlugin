"""
A Sublime Text Plugin which will help log
each time you write to a file and what changes
were made.

Author: Max Zuo
"""


import sublime, sublime_plugin, os
from datetime import datetime
import difflib
class LogsaveCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		name = self.view.file_name()
		if name != None:
			directory = name[:name.rfind("/")]
			self.save(name, directory)
		else:
			self.view.run_command('save')
			name = self.view.file_name()
			directory = name[:name.rfind("/")]
			self.save(name, directory, new_save=True)


	def save(self, name, directory, new_save=False):
		if os.path.isdir(directory) and os.path.isfile("%s/sublime_log.txt" % directory):
			contents = []
			lines = str(self.view.substr(sublime.Region(0, self.view.size())))
			newContents = lines.split("\n")
			oldContents = []
			if not new_save:
				with open(name, "r") as f:
					oldContents = map(lambda x: x[:-1] if (x[-1] == "\n") else x, f.readlines())
			with open("%s/sublime_log.txt" % directory, "a") as f:
				diff = difflib.ndiff(filter(lambda x: x != "", oldContents), filter(lambda x: x != "", newContents))
				now = datetime.now().strftime("%A, %d. %B %Y %I:%M:%S%p")
				insertions = len(filter(lambda (x, y): y.startswith("+"), enumerate(diff)))
				diff = difflib.ndiff(filter(lambda x: x != "", oldContents), filter(lambda x: x != "", newContents))
				deletions = len(filter(lambda (x, y): y.startswith("-"), enumerate(diff)))
				diff = difflib.ndiff(filter(lambda x: x != "", oldContents), filter(lambda x: x != "", newContents))
				for i, line in enumerate(diff): print line
				if insertions != 0 or deletions != 0:
					if not new_save:
						changes = "%s:\tFile: %s\nline insertions: %d\tline deletions: %d\n" % (now, name, insertions, deletions)
					else:
						changes = "%s: New File Created: %s\nline insertions: %d\n" % (now, name, insertions)
					f.write(changes)

		self.view.run_command('save')