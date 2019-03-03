# LogSaveSublimePlugin
A Sublime Text Plugin which records each save to a log file. *Currently supports Sublime Text 2 on linux/macOS.*

## How it works
The **LogSave** plugin records each time you save using the `cmd+s` or `ctrl+s` command. It writes to a file called *sublime_log.txt*. Here's an example of a log:

    Sunday, 03. March 2019 03:20:58AM:	File: LogsavePlugin.py
    line insertions: 124	line deletions: 39

## How to set it up
If you are experienced with Sublime Text plugins, the `LogsavePlugin.py` is the file which contains the actual plugin class. However, to automatically set up the **LogSave** plugin with the `cmd+s`/`ctrl+s` keyboard shortcut, follow these steps:
* Download or clone this repository.
* In your command line tool, go to the directory of the downloaded repository.
* Run `python setupLogsave.py`.
  * If any errors occur, make sure that you have Sublime Text 2, and that the `LogSavePlugin.py` file is in the same directory as the setup file.

## How to use it
**LogSave** only runs on files in directories with a specific log file. If you would like **LogSave** to record in a certain directory, first initalize an empty text file called `sublime_log.txt` in that directory.
