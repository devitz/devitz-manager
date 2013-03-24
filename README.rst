Devitz Manager
==============

This is the master power manager!

How to start?
-------------

These are the steps to cast the spell:

::
  
  $ git clone git@github.com:devitz/devitz-manager.git devitz_manager
  $ cd devitz_manager/
  $ mkvirtualenv devitz_manager
  $ pip install -r requirements/prod.txt 


And make you own settings, with settings_dev.py file, something like this:

::
  
  # Debug
  
  DEBUG = False
  TEMPLATE_DEBUG = DEBUG


Choose your database and run, run forest, run!