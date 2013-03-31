import sublime
import sublime_plugin
import os.path
import platform
import re


class WordpressDbSwitcherCommand(sublime_plugin.WindowCommand):
    def run(self, extensions=[]):
        if not self.window.active_view():
            return
        self.populate_db_list()
        self.show_db_list()

    def extract_wp_db_defs(self):
        db_names = []

        with open('c:\users\huntly\desktop\wp-config-sample.php') as wp_config:
            file_contents = wp_config.read()
        wp_config.close()

        repatt = '(?:\/\/)?(define\(\'DB_NAME\'.*)'
        dbs = re.findall(repatt, file_contents)

        for db in dbs:
            dbrepat = "define\('DB_NAME\',\s+'([^']*)'\);(\s\/\/(.*))?"
            match = re.search(dbrepat, db)

            if match.group(3) is not None:
                db_names.append("%s - %s" % (match.group(1), match.group(3)))
            else:
                db_names.append(match.group(1))

        return db_names

    def populate_db_list(self):
        if len(self.dblist) is 0:
            self.dblist = self.extract_wp_db_defs()

    def show_db_list(self):
        self.window.show_quick_panel(self.dblist,
                                     self.panel_done,
                                     sublime.MONOSPACE_FONT)

    def panel_done(self, selected):
        if 0 > selected < len(self.dblist):
            return

        dbname = self.dblist[selected].split(' ')[0]
        self.dblist = []  # clear the list

        self.switch_active_database(dbname)

    def switch_active_database(self, dbname):
        file_path = 'c:\users\huntly\desktop\wp-config-sample.php'
        wp_config = open(file_path, 'r+')
        file_contents = wp_config.read()

        #Comment out all uncommented db
        uncommentedDB = r'([^\/\/])define\(\'DB_NAME\''
        commentedDB = r"\1//define('DB_NAME'"
        file_contents = re.sub(uncommentedDB,
                               commentedDB,
                               file_contents)

        commentedDB = r'\/\/define\(\'DB_NAME\',\s+\'%s\'' % dbname
        uncommentedDB = "define('DB_NAME', '%s'" % dbname
        file_contents = re.sub(commentedDB,
                               uncommentedDB,
                               file_contents)
        wp_config.truncate()
        wp_config.write(file_contents)
        wp_config.close()
