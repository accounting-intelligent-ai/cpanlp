Formal Accounting
===============================================

In accounting, the formal language component refers to the specific language and rules used to communicate financial information. This includes standardized accounting principles, concepts, and terminology, as well as financial reporting formats such as balance sheets, income statements, and cash flow statements.

.. image:: https://raw.githubusercontent.com/accounting-intelligent-ai/cpanlp/main/cpanlp.png
   :align: center
   :width: 250
   :height: 100
   :alt: logo

.. image:: https://img.shields.io/static/v1?label=pypi&message=v1.2.51&color=blue
   :target: https://pypi.org/project/cpanlp/
   :alt: PyPI - Python Version

.. image:: https://static.pepy.tech/badge/cpanlp/week
   :target: https://pepy.tech/project/cpanlp
   :alt: Downloads

This Python package displays the application of formal accounting. `Read the Docs Tutorial <https://www.cpanlp.com/>`__.

📚 `docs/ <https://github.com/accounting-intelligent-ai/cpanlp>`_
    A basic Sphinx project lives in ``docs/``. All the ``*.rst`` make up sections in the documentation.
⚙️ `.readthedocs.yaml <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/.readthedocs.yaml>`_
    Read the Docs Build configuration is stored in ``.readthedocs.yaml``.
⚙️ `docs/conf.py <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/docs/conf.py>`_
    Both the configuration and the folder layout follow Sphinx default conventions. You can change the `Sphinx configuration values <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_ in this file
📍 `docs/requirements.txt <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/docs/requirements.txt>`_ and `docs/requirements.in <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/docs/requirements.in>`_
    Python dependencies are `pinned <https://docs.readthedocs.io/en/latest/guides/reproducible-builds.html>`_ (uses `pip-tools <https://pip-tools.readthedocs.io/en/latest/>`_). Make sure to add your Python dependencies to ``requirements.txt`` or if you choose `pip-tools <https://pip-tools.readthedocs.io/en/latest/>`_, edit ``docs/requirements.in`` and remember to run ``pip-compile docs/requirements.in``.
💡 `docs/api.rst <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/docs/api.rst>`_
    By adding our example Python module ``lumache`` in the reStructuredText directive ``:autosummary:``, Sphinx will automatically scan this module and generate API docs.
💡 `docs/usage.rst <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/docs/usage.rst>`_
    Sphinx can automatically extract API documentation directly from Python modules, using for instance the ``:autofunction:`` directive.
💡 `lumache.py <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/lumache.py>`_
    API docs are generated for this example Python module - they use *docstrings* directly in the documentation, notice how this shows up in the rendered documentation.
🔢 Git tags versioning
    We use a basic versioning mechanism by adding a git tag for every release of the example project. All releases and their version numbers are visible on `example-sphinx-basic.readthedocs.io <https://example-sphinx-basic.readthedocs.io/en/latest/>`__.
📜 `README.rst <https://github.com/readthedocs-examples/example-sphinx-basic/blob/main/README.rst>`_
    Contents of this ``README.rst`` are visible on Github and included on `the documentation index page <https://example-sphinx-basic.readthedocs.io/en/latest/>`_ (Don't Repeat Yourself).
⁉️ Questions / comments
    If you have questions related to this example, feel free to can ask them as a Github issue `here <https://github.com/readthedocs-examples/example-sphinx-basic/issues>`_.


Example Project usage
---------------------

This project has a standard Sphinx layout which is built by Read the Docs almost the same way that you would build it locally (on your own laptop!).

You can build and view this documentation project locally - we recommend that you activate `a local Python virtual environment first <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment>`_:

.. code-block:: console

    # Install required Python dependencies
    pip install scipy
    pip install numpy
    pip install pandas
    
    # Run the install command
    pip install cpanlp


You can also build the documentation locally with ``make``:

.. code-block:: console

    # Enter the Sphinx project
    cd docs/
    
    # Build with make
    make html
    
    # Open with your preferred browser, pointing it to the documentation index page
    firefox _build/html/index.html


Using the example in your own project
-------------------------------------

If you are new to Read the Docs, you may want to refer to the `Read the Docs User documentation <https://docs.readthedocs.io/>`_.

If you are copying this code in order to get started with your documentation, you need to:

#. place your ``docs/`` folder alongside your Python project. If you are starting a new project, you can adapt the `pyproject.toml` example configuration.
#. use your existing project repository or create a new repository on Github, GitLab, Bitbucket or another host supported by Read the Docs
#. copy ``.readthedocs.yaml`` and the ``docs/`` folder into your project.
#. customize all the files, replacing example contents.
#. add your own Python project, replacing the ``pyproject.toml`` configuration and ``lumache.py`` module.
#. rebuild the documenation locally to see that it works.
#. *finally*, register your project on Read the Docs, see `Importing Your Documentation <https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_.


Module
----------------------

.. list-table:: cpanlp main module
   :widths: 25 25 50
   :header-rows: 1

   * - Category
     - Module
     - Example
   * - **Accounting**
     - Asset
     - ``Intangible Asset``
   * - 
     - Liability
     - ``Financial Liability``
   * - 
     - Equity
     - ``Share``
   * - 
     - Income
     - ``Revenue``
   * - 
     - Cashflow
     - ``Cashflow``
   * - 
     - Policy
     - ``DividendPolicy``
   * - 
     - Report
     - ``IncomeSmoothing``
   * - **Audit**
     - Audit
     - ``Audit Opinion``
   * - **Financial Management**
     - Incentive
     - ``Promotion Incentive``
   * - 
     - Scheme
     - ``Ponzi``
   * - **Tax**
     - Tax on Behavior
     - ``TransactionTax``
   * - 
     - Tax on Income
     - ``PersonalIncomeTax``
   * - 
     - Tax on Property
     - ``RealEstateTax``
   * - **Corporate Law**
     - Contract
     - ``Lease``
   * - 
     - Control
     - ``Voting Power``
   * - 
     - Entity
     - ``LLC``
   * - 
     - Provision
     - ``SayOnPay``
   * - **Strategy**
     - 
     - ``Long Term Strategy``