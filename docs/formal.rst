Formal language
=====

Double-entry accounting
------------

the concept of debits and credits is central to accounting, and the rules governing their application can be viewed as a type of formal language.

>>> pip install cpanlp

Cash Basis accounting
----------------

The formal language of the cash basis accounting method includes the recognition of revenue when cash is received and the recognition of expenses when cash is paid out. This method is simple and straightforward, making it popular with small businesses and individuals who do not have complex accounting needs.
To retrieve a list of random ingredients,
you can use the ``Sale()`` class:


The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

For example:

>>> import cpanlp as p
>>> sale1 = p.Sale(quarter="Q4",amount=93.4,unit="billion dollars",growth_rate=13%,year=2022,segment="North America")
['shells', 'gorgonzola', 'parsley']

Accrual Basis Accounting
----------------

The formal language of the accrual basis accounting method includes the recognition of revenue when it is earned, regardless of whether or not the cash has been received, and the recognition of expenses when they are incurred, regardless of whether or not the cash has been paid out.

For example:

>>> gold_asset = p.Asset(account="gold", debit=1000,date="2023-01-01")
>>> print(gold_asset.bubble)

GAAP
----------------

The formal language of GAAP includes standardized financial reporting formats such as balance sheets, income statements, and cash flow statements, as well as specific terms and concepts such as assets, liabilities, equity, revenues, expenses, and gains/losses. GAAP also includes specific rules and guidelines for how financial information should be recorded and reported, including rules related to depreciation, inventory valuation, and revenue recognition.

IFRS
----------------

The formal language of IFRS includes standardized financial reporting formats such as balance sheets, income statements, and cash flow statements, as well as specific terms and concepts such as assets, liabilities, equity, revenues, expenses, and gains/losses. 