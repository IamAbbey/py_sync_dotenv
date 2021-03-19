Python Sync Dotenv ♻️
=====================

.. image:: https://img.shields.io/pypi/v/py\_sync\_dotenv.svg :target: https://pypi.python.org/pypi/py\_sync\_dotenv

.. image:: https://img.shields.io/travis/IamAbbey/py\_sync\_dotenv.svg :target: https://travis-ci.com/IamAbbey/py\_sync\_dotenv

.. image:: https://readthedocs.org/projects/py-sync-dotenv/badge/?version=latest :target: https://py-sync-dotenv.readthedocs.io/en/latest/?version=latest :alt: Documentation Status



Python Sync Dotenv is a Python package for synchronizing ``.env`` files
across projects using command-line interfaces.

-  Free software: MIT license
-  Documentation: https://py-sync-dotenv.readthedocs.io.

Installation
------------

.. code:: bash

    $ pip install py-sync-dotenv

Usage
-----

-  By default, py-sync-dotenv tries to locate the source .env file with
   the name **.env** from the current working directory.

   .. code:: bash  
   
    $ py-sync-dotenv

-  This behavior can be modified by providing the source .env file path
   using the ``-s, --source`` option.

   .. code:: bash     
    

    $ py-sync-dotenv -s .env.source     

    #OR

    $ py-sync-dotenv --source .env.source

-  Another option that can be supplied is the ``-d, --destination-env`` which is used to provide the path to the destination .env file. The below commands synchronizes the source .env file with the specified 
   destination env file - *.env.dev*
   
   .. code:: bash      

     $ py-sync-dotenv -d .env.dev     
 
     #OR     

     $ py-sync-dotenv --destination-env .env.dev``

-  Likewise, there is the ``-ds, --destination-envs`` option which is used to provide the **directory** containing the destination .env file(s). The below commands synchronizes the source .env file with all the
   .env files contained in the specified **directory**.
   

   .. code:: bash      

    $ py-sync-dotenv -ds dev_envs/     

    #OR     

    $ py-sync-dotenv --destination-envs dev_envs/``

-  Futhermore, to all the above options, you can specify the ``--just-variable`` flag to indicates to the 
   engine to synchronize just the variables.
   

   .. code:: bash     

    $ py-sync-dotenv -d .env.dev --just-variables     

    # Source --------------------> destination     

    # SQL_HOST=127.0.0.1 --------> SQL_HOST=     

    # SQL_PORT=5432 --------> SQL_PORT=

Command
-------

-  The ``watch`` command can be used to auto synchronize the source .env
   file [on file changed/modified] with the specified destination
   file(s).
   

   .. code:: bash      

    $ py-sync-dotenv -s .env.source -d .env.dev watch


-  Coupled with the ``watch`` command is the ``--show-logs`` flag, which is used to show file changes logs as they occur.
   

   .. code:: bash     

     $ py-sync-dotenv -d .env.dev watch --show-logs

Options
-------

+-------------+---------------------------+-------------------------------------------------------------------------------+
| Type        | Option                    | Description                                                                   |
+=============+===========================+===============================================================================+
| FILE        | -s, --source              | Source ``.env`` file to use in populating other .env files [default: .env].   |
+-------------+---------------------------+-------------------------------------------------------------------------------+
| FILE        | -d, --destination-env     | ``.env`` file for destination stage.                                          |
+-------------+---------------------------+-------------------------------------------------------------------------------+
| DIRECTORY   | -ds, --destination-envs   | Directory path to ``.env`` files for destination stage.                       |
+-------------+---------------------------+-------------------------------------------------------------------------------+

Flags
-----

+--------+--------------------+-------------------------------------------------------------------------------+
| Type   | Flag               | Description                                                                   |
+========+====================+===============================================================================+
| FLAG   | --just-variables   | indicates to the engine to synchronize just the variables.                    |
+--------+--------------------+-------------------------------------------------------------------------------+
| FLAG   | --show-logs        | show file changes logs as they occur. To be used with the ``watch`` command   |
+--------+--------------------+-------------------------------------------------------------------------------+
| FLAG   | --help             | Show this message and exit.                                                   |
+--------+--------------------+-------------------------------------------------------------------------------+

Commands
--------

+-----------+-----------+---------------------------------------------------------------------------------------------------------------------------------------+
| Type      | Command   | Description                                                                                                                           |
+===========+===========+=======================================================================================================================================+
| COMMAND   | watch     | indicates to the engine to auto synchronize the source .env file [on file changed/modified] with the specified destination file(s).   |
+-----------+-----------+---------------------------------------------------------------------------------------------------------------------------------------+

Credits
-------

This package was created with Cookiecutter_ and the cookiecutter-pypackage_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter 
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage