# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thelogrus']

package_data = \
{'': ['*']}

install_requires = \
['dateutils>=0.6.12,<0.7.0', 'pyaml>=21.10.1,<22.0.0']

entry_points = \
{'console_scripts': ['human-time = thelogrus.time:human_time_converter']}

setup_kwargs = {
    'name': 'thelogrus',
    'version': '0.6.1',
    'description': 'The Logrus is a collection of random utility functions',
    'long_description': '# logrus\n\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n[![GitHub stars](https://img.shields.io/github/stars/unixorn/thelogrus.svg)](https://github.com/unixorn/thelogrus/stargazers)\n[![Code Climate](https://codeclimate.com/github/unixorn/thelogrus/badges/gpa.svg)](https://codeclimate.com/github/unixorn/thelogrus)\n[![Issue Count](https://codeclimate.com/github/unixorn/thelogrus/badges/issue_count.svg)](https://codeclimate.com/github/unixorn/thelogrus)\n\n<!-- START doctoc generated TOC please keep comment here to allow auto update -->\n<!-- DON\'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->\n## Table of Contents\n\n- [Installation](#installation)\n- [License](#license)\n- [Included Commands](#included-commands)\n  - [human-time](#human-time)\n- [Included functions](#included-functions)\n  - [thelogrus.cli](#thelogruscli)\n    - [exec_subcommand(unfound)](#exec_subcommandunfound)\n    - [find_subcommand(args)](#find_subcommandargs)\n    - [is_program(name)](#is_programname)\n    - [run(command)](#runcommand)\n  - [thelogrus.logging](#thelogruslogging)\n    - [getCustomLogger(name, logLevel)](#getcustomloggername-loglevel)\n  - [thelogrus.time](#thelogrustime)\n    - [humanTime(seconds)](#humantimeseconds)\n  - [thelogrus.utils](#thelogrusutils)\n    - [mkdir_p(path)](#mkdir_ppath)\n    - [obfuscateString(snippet, showLength=5, smear=\'*\')](#obfuscatestringsnippet-showlength5-smear)\n    - [squashDicts(*dict_args)](#squashdictsdict_args)\n  - [thelogrus.yaml](#thelogrusyaml)\n    - [readYamlFile(path: str)](#readyamlfilepath-str)\n  - [writeYamlFile(path: str, data)](#writeyamlfilepath-str-data)\n\n<!-- END doctoc generated TOC please keep comment here to allow auto update -->\n\nThe logrus is a collection of random utility functions. Nothing in here is all that special, they\'re just yet another implementation of functions I\'ve rewritten at every job to use in various utility scripts. By open sourcing them now, I\'m hoping to not have to write them yet again.\n\nAnd yes, the name is from Zelazny\'s Amber series.\n\n## Installation\n\n`pip install thelogrus`\n\n## License\n\nApache 2.0 license.\n\n## Included Commands\n\n### human-time\n\nTakes a value in seconds either from stdin or as arg 1 and converts it to a more meat-friendly format using the `humanTime` function.\n\n`human-time 1234` will print "20 minutes, 34 seconds"\n\n## Included functions\n\n### thelogrus.cli\n\n#### exec_subcommand(unfound)\n\nCreates a `git`-style driver command. If your script is named `foo`, and is run as `foo bar baz` and there is an executable in your `$PATH` named `foo-bar`, it will call `foo-bar` with `baz` as the command-line argument.\n\n`unfound` is an optional argument that should be a function pointer and will be called if `exec_subcommand` can\'t find a suitable subcommand. Mainly useful for you to have a custom usage message.\n\nExample usage:\n\n```python\n#!/usr/bin/env python3\n#\n# Test script for thelogrus\n#\n# Confirms that thelogrus.cli.exec_subcommand works as expected\n#\n# Copyright 2019, Joe Block <jpb@unixorn.net>\n\nimport sys\nfrom thelogrus.cli import exec_subcommand\n\n\ndef _usage(message):\n  \'\'\'\n  Custom usage printer\n  \'\'\'\n  print("%s" % sys.argv[0])\n  print("Called as %s" % (\' \'.join(sys.argv)))\n  print("Oh look, a custom usage message.")\n  print("Attempted to find an executable using all the permutations of %s with no luck." % \'-\'.join(sys.argv))\n  print("%s" % message)\n\n\nif __name__ == \'__main__\':\n  exec_subcommand(unfound=_usage)\n```\n\n#### find_subcommand(args)\n\nGiven a list [\'foo\',\'bar\', \'baz\'], attempts to create a command name in the format `foo-bar-baz`. If that command exists, we run it. If it doesn\'t, we check to see if `foo-bar` exists, in which case we run `foo-bar baz`. We keep slicing chunks off the end of the command name and adding them to the argument list until we find a valid command name we can run.\n\nThis allows us to easily make git-style command drivers where for example we have a driver script, `foo`, and subcommand scripts `foo-bar` and `foo-baz`, and when the user types `foo bar foobar` we find the foo-bar script and run it as `foo-bar foobar`\n\nExample usage:\n\n```python\n#!/usr/bin/env python3\n\nimport os\nimport subprocess\nimport sys\nfrom thelogrus.cli import find_subcommand\n\n\ndef subcommander_driver():\n  \'\'\'\n  Process the command line arguments and run the appropriate subcommand.\n\n  We want to be able to do git-style handoffs to subcommands where if we\n  do `foo blah foo bar` and the executable foo-blah-foo exists, we\'ll call\n  it with the argument bar.\n\n  We deliberately don\'t do anything with the arguments other than hand\n  them off to the foo subcommand. Subcommands are responsible for their\n  own argument parsing.\n  \'\'\'\n  try:\n    (command, args) = find_subcommand(sys.argv)\n\n    # If we can\'t construct a subcommand from sys.argv, it\'ll still be able\n    # to find this driver script, and re-running ourself isn\'t useful.\n    if os.path.basename(command) == sys.argv[0]:\n      print("Could not find a subcommand for %s" % \' \'.join(sys.argv))\n      sys.exit(1)\n  except Exception as e:\n    print(str(e))\n    sys.exit(1)\n  subprocess.check_call([command] + args)\n\n\nif __name__ == \'__main__\':\n  subcommander_driver()\n```\n\n#### is_program(name)\n\nSearch for a given program in `$PATH`, and return `True` if it exists and is executable.\n\n#### run(command)\n\nRuns a command (either a str or list) and returns its `stdout`.\n\n### thelogrus.logging\n\n#### getCustomLogger(name, logLevel)\n\nReturns a custom logger with nicely formatted output.\n\n### thelogrus.time\n\n#### humanTime(seconds)\n\nTakes a value in seconds, returns it in meat-friendly format. `humanFriendlyTime(8675309)` would return "100 days 9 hours 48 minutes 29 seconds".\n\n### thelogrus.utils\n\n#### mkdir_p(path)\n\nos module doesn\'t have a `mkdir -p` equivalent so added one.\n\n#### obfuscateString(snippet, showLength=5, smear=\'*\')\n\nTakes a string, chops off showLength characters from the beginning and end and replaces everything else with the `smear` character. Really only useful for displaying just enough of a credential in a log to show it\'s using the correct credential, but not revealing the actual credential.\n\n#### squashDicts(*dict_args)\n\nReturn a dict that is all the dict_args squashed together.\n\n### thelogrus.yaml\n\n#### readYamlFile(path: str)\n\nReturn the data structure contained in a YAML file\n\nArgs:\n    path (str): Path to read from\n\nReturns:\n    Data decoded from YAML file content\n\n### writeYamlFile(path: str, data)\n\nWrites a data structure or object into a YAML file\n\nArgs:\n    path (str): Path to data file\n    data (any): Data to convert and write\n',
    'author': 'Joe Block',
    'author_email': 'jpb@unixorn.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/unixorn/thelogrus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
