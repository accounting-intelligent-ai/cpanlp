Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install cpanlp

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``Sale()`` class:


The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import cpanlp as p
>>> sale1 = p.Sale(quarter="Q4",amount=93.4,unit="billion dollars",growth_rate=13%,year=2022,segment="North America")
['shells', 'gorgonzola', 'parsley']

Features
----------------

For example:

>>> gold_asset = p.Asset(account="gold", debit=1000,date="2023-01-01")
>>> print(gold_asset.bubble)