===============================
Rate Query API
===============================

This app implements HTTP wrapper for Telnet commands. Telnet commands hardcoded in the view methods
(in the get_vendors_for_destination() and in the get_vendor_rate())

Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export RATE_QUERY_API_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/osya/RateQueryAPI
    cd RateQueryAPI
    pip install -r requirements/dev.txt
    bower install
    python manage.py server

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Deployment
----------

In your production environment, make sure the ``RATE_QUERY_API_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


