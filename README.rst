fnvstring
=========

**fnvstring** is a hash implementation of the Fowler–Noll–Vo 
**non-cryptographic** function for python 3. 

The main porpuse of this package is return base64 string hashes of a length 
of 11.

To know more about `Fowler–Noll–Vo hash function`_.

Installation
^^^^^^^^^^^^

.. code:: shell

   $ pip install fnvstring

Usage
~~~~~

usage in terminal
-----------------

You can hash any string from terminal just typing

.. code:: shell

   $ fnvstring "Hello World!"
   rzWLzszm9JE

Also you can salt the hasher passing additional string:

.. code:: shell

   $ fnvstring 'Hello World!' 'My custom salt string'
   jq4a08o_O5k



usage in code
-------------

You can instantiate a salted hasher for your convenience

.. code:: python

   from fnvstring import Fvn64SaltedHasher
   my_hasher = Fvn64SaltedHasher(salt='Any$tringYouWant, even none')
   print(my_hasher.hash('Hello World!')) # Must output dcSEMoww20o if you dont change the salt param

   # If you want to use another salt for any reason set the salt param
   my_hasher.hash('Hello World!', salt='Any other salt')

Also you can use the class Fvn64StringHasher with static methods to build your
hashes

.. code:: python

    from fnvstring.hasher import Fvn64StringHasher
    
    # note that salt param is an optional param

    # Using the same salt param must output dcSEMoww20o again
    print(Fvn64StringHasher.as_base64('Hello World!', salt='Any$tringYouWant, even none'))
    
    # Whith none salt will output fDiM9gLdWY4
    print(Fvn64StringHasher.as_base64('Hello World!'))


.. _`Fowler–Noll–Vo hash function`: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_functionhttps://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function