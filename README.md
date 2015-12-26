# Sublime Text WordPress Dev Plugin #

Simple plugin for [Sublime Text](http://www.sublimetext.com/ "Sublime Text") which adds a few commands that may be handy for people building sites with WordPress.

## Install ##
Take the easy route and use [Package Control](http://wbond.net/sublime_packages/package_control).  If you're not already using it, you want to jump on that band wagon!

If you're hardcore or want to hack away on this plugin, clone this repo or download it.  Then simply move the *WordPressDev* folder into your Sublime Text plugins directory.

Once you've downloaded it or got it via Package Control, you want to tell it the location of your `wp-config.php` file.  To do this, go to the  _Preferences -> Package Settings -> WordPressDev_ menu and edit your *User* settings.  In that file add the following:
``` json
{
    //Path to where your wp-config.php file resides
    "wp_config_file": "/var/www/wordpressdir/wp-config.php"
}
```

Make sure to change `"wp_config_file"` to the full path to your `wp-config.php` file!

_You can also now access your `wp-config.php` without setting anything in Sublime Text. See below._

## Commands ##
Commands listed here can be found in the command pallet prefixed with ```WordPress: ``` or they can be accessed from the _Tools ->  WordPress_ menu

### Open Config File ###
Allows you to quickly view/edit your WordPress config file. Default shortcut is ```ctrl+alt+o```

### Open Config File for Parent WP Install ###

Allows you to open the config file in the relative root of your WordPress install.

No default shortcut. You can access this command through the _Tools ->  WordPress_ menu or using the command palette


### Toggle Debug ###
Allows you to quickly toggle the ```WP_DEBUG``` variable.

### Switch Database ###
If you like to keep separate databases for each site you build you can build up a list like this in your wp-config file:

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

### WordPress Doc Lookup ###
Opens up the WordPress codex reference seraching for the highlighted text
The default shortcut for this command is ```ctrl+m, ctrl+w```

### PHP Doc Lookup ###
Opens up the PHP docs searching for the highlighted text
The default shortcut for this command is ```ctrl+m, ctrl+p```
