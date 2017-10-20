SublimeLinter-contrib-yamllint
================================

[![Build Status](https://travis-ci.org/thomasmeeus/SublimeLinter-contrib-yamllint.svg?branch=master)](https://travis-ci.org/thomasmeeus/SublimeLinter-contrib-yamllint)

This linter plugin for [SublimeLinter][docs] provides an interface to [yamllint](https://github.com/thomasmeeus/SublimeLinter-contrib-yamllint). It will be used with files that have the "yaml" syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `yamllint` is installed on your system. To install `yamllint`, do the following:

1. Install [Python3](https://www.python.org/downloads/) and pip. Python3 is required by `yamllint`

1. Install `yamllint` by typing the following in a terminal:
   ```
   [sudo] pip3 install yamllint
   ```


**Note:** This plugin requires `yamllint` 1.9 or later.

### Linter configuration
In order for `yamllint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `yamllint`, you can proceed to install the SublimeLinter-contrib-yamllint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `yamllint`. Among the entries you should see `SublimeLinter-contrib-yamllint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
Check the [Yamllint docs](https://yamllint.readthedocs.io/en/latest/) for more information about all settings. I suggest to create the file `~/.config/yamllint/config` to override specific settings.

```
extends: default

rules:
  line-length:
    max: 600
```


## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
