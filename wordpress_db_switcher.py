import sublime
import sublime_plugin
import os.path
import platform
import re


class WordpressOpenConfigCommand(sublime_plugin.WindowCommand):
    def run(self):
        s = sublime.load_settings("WordpressDbSwitcher.sublime-settings")
        config_file_location = s.get("wp_config_file")
        self.window.open_file(config_file_location)


class WordpressDbSwitcherCommand(sublime_plugin.WindowCommand):
    def run(self, extensions=[]):
        if not self.window.active_view():
            return

        s = sublime.load_settings("WordpressDbSwitcher.sublime-settings")
        self.dblist = []
        self.config_file_location = s.get("wp_config_file")
        self.populate_db_list()
        self.show_db_list()

    def extract_wp_db_defs(self):
        db_names = []

        try:

            with open(self.config_file_location, 'r') as wp_config:
                file_contents = wp_config.read()
            wp_config.close()

            repatt = '(?:\/\/)?(define\(\'DB_NAME\'.*)'
            dbs = re.findall(repatt, file_contents)

            for db in dbs:
                dbrepat = "define\('DB_NAME\',\s+'([^']*)'\);(\s\/\/(.*))?"
                match = re.search(dbrepat, db)

                if match.group(3) is not None:
                    db_names.append("%s - %s" %
                                   (match.group(1), match.group(3)))
                else:
                    db_names.append(match.group(1))
        except IOError:
            #Open the settings file
            dir_name = os.path.join(sublime.packages_path(),
                                    'WordpressDbSwitcher')
            self.window.open_file(os.path.join(dir_name,
                                               'WordpressDbSwitcher' +
                                               '.sublime-settings'))

            db_names.append("wp-config file doesn't exist, " +
                            'check your settings')

        return db_names

    def populate_db_list(self):
        if len(self.dblist) is 0:
            self.dblist = self.extract_wp_db_defs()

    def show_db_list(self):
        window = sublime.active_window()
        window.show_quick_panel(self.dblist,
                                self.panel_done,
                                sublime.MONOSPACE_FONT)

    def panel_done(self, selected):
        if 0 > selected < len(self.dblist):
            return

        dbname = self.dblist[selected].split(' ')[0]
        del self.dblist[:]  # clear the list

        self.switch_active_database(dbname)

    def switch_active_database(self, dbname):
        try:
            with open(self.config_file_location, 'r') as wp_config:
                file_contents = wp_config.read()
            wp_config.close()

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

            with open(self.config_file_location, 'w') as wp_config:
                wp_config.write(file_contents)
            wp_config.close()
        except IOError:
            print "Cannot open file, check settings"
            #file doesn't exist, user has already been warned
