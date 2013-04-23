# Sublime Text 2 WordPress Dev Plugin #

Simple plugin for [Sublime Text 2](http://www.sublimetext.com/2 "Sublime Text 2") which adds a few commands that may be handy for people building sites with wordpress.

## Install ##
Take the easy route and use [Package Control](http://wbond.net/sublime_packages/package_control).  If you're not already using it, you want to jump on that band wagon!

If you're hardcore or want to hack away on this plugin, clone this repo or download it.  Then simply move the *WordPressDev* folder into your Sublime Text plugins directory.

You'll also want to edit the settings file: *WordPressDev.sublime-settings* and give the plugin the path to your config file.

## Commands ##
Commands listed here can be found in the command pallet prefixed with ```WordPress: ``` or they can be accessed from the _Tools ->  WordPress_ menu

### Open Config File ###
Allows you to quickly view/edit your wordpress config file. Default shortcut is ```ctrl+alt+o```

### Toggle Debug ###
Allows you to quickly toggle the ```WP_DEBUG``` variable.

### Switch Database ###
If you like to keep seperate databases for each site you build you can build up a list like this in your wp-config file:

``` php
//define('DB_NAME', 'wp_bootstrap_theme'); //bootstrap test
define('DB_NAME', 'wp_default');
//define('DB_NAME', 'wp_fbtest'); //My FB API tests
//define('DB_NAME', 'wp_huntlywebsite'); //mywebsite
//define('DB_NAME', 'wp_multi'); //Multisite install
//define('DB_NAME', 'wp_rgt'); //Responsive grid test
```

Activating the DB Switch command will bring up the quick search dialog allowing you to quickly select the database you want.
*Note* the comments after the definitions are optional.  From my list above this is how the quick search list will look:

```
wp_bootstrap_theme - bootstrap test
wp_default
wp_fbtest - My FB API tests
wp_huntlywebsite - mywebsite
wp_multi - Multisite install
wp_rgt - Responsive grid test
```

The default shortcut for this command is ```ctrl+alt+w```
