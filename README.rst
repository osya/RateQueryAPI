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

    git clone http://valeriy@stash.denovolab.com/scm/rqa/alpha
    cd alpha
    pip install -r requirements/dev.txt
    python manage.py server


Deployment
----------

In your production environment, make sure the ``RATE_QUERY_API_ENV`` environment variable is set to ``"prod"``.

Using
-----

You can execute the following curls and get result:
curl http://149.56.132.178:5000/api/v1/GetVendorsForDestination/US%20Virgin%20Islands%20Proper
curl http://149.56.132.178:5000/api/v1/GetVendorRate/US%20Virgin%20Islands%20Proper

Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


