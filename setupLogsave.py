import os
"""
A setup python script which will automatically load
the LogsavePlugin into your Sublime Text 2.

Currently only supports for Sublime Text 2.
Support for Sublime Text 3 coming soon.

Author: Max Zuo
"""

from os import path
import sys

def create_folder():
	home = path.expanduser("~")

	if not path.isdir(home + "/Library/Application Support/Sublime Text 2/Packages/"):
		print "Could not find Sublime Text 2 Packages folder. Aborting."
		sys.exit()

	if path.isdir(home + "/Library/Application Support/Sublime Text 2/Packages/LogsavePlugin"):
		return

	os.mkdir(home + "/Library/Application Support/Sublime Text 2/Packages/LogsavePlugin")

def move_file():
	home = path.expanduser("~")

	if not path.isfile("./LogsavePlugin.py"):
		print "Could not find 'LogsavePlugin.py' file. Aborting."
		sys.exit()

	os.rename("./LogsavePlugin.py", "%s/Library/Application Support/Sublime Text 2/Packages/LogsavePlugin%s" % (home, "LogsavePlugin.py"))


def update_keybindings():
	home = path.expanduser("~")
	
	if not path.isfile(home + "/Library/Application Support/Sublime Text 2/Packages/Default/Default (OSX).sublime-keymap"):
		print "Could not find default keyboard bindings. Aborting."
		sys.exit()
	lines = []
	edited = False
	with open(home + "/Library/Application Support/Sublime Text 2/Packages/Default/Default (OSX).sublime-keymap", "r") as f:
		for line in f:
			if "{ \"keys\": [\"super+s\"], \"command\":" in line:
				lines.append("	{ \"keys\": [\"super+s\"], \"command\": \"logsave\" },")
				edited = True
			else:
				lines.append(line)
	if not edited:
		lastOcc = max(index for index, line in enumerate(lines) if ']' in line)
		lines.insert(lastOcc, "	{ \"keys\": [\"super+s\"], \"command\": \"logsave\" }")
	with open(home + "/Library/Application Support/Sublime Text 2/Packages/Default/Default (OSX).sublime-keymap", "w") as f:
		f.writelines(lines)

if __name__ == "__main__":

	# Create Plugin folder
	create_folder()

	# Move file
	move_file()

	# update keybindings to have log save.
	update_keybindings()
