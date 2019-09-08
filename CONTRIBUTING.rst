Contributor's Guide
===================

Contributions are always welcome and greatly appreciated!

Code contributions
------------------

We love pull requests from everyone! Here's a quick guide to improve the code:

1. Fork `the repository <https://github.com/affo/affo-email-service>`_ and clone the fork.
2. Create a virtual environment using your tool of choice (e.g. ``virtualenv``, ``conda``, etc).
3. Install development dependencies:

::

    pip install -r requirements.txt
    pip install -r requirements-test.txt

4. Make sure all tests pass:

::

    python setup.py test

5. Start making your changes to the **master** branch (or branch off of it).
6. Make sure all tests still pass:

::

    python setup.py test

7. Add yourself to ``AUTHORS.rst``.
8. Commit your changes and push your branch to GitHub.
9. Create a `pull request <https://help.github.com/articles/about-pull-requests/>`_ through the GitHub website.


Documentation improvements
--------------------------

We could always use more documentation, whether as part of the
introduction/examples/usage documentation or API documentation in docstrings.

Documentation is written in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_
and use `Sphinx <http://sphinx-doc.org/index.html>`_ to generate the HTML output.

Once you made the documentation changes locally, run the documentation generation::

    python setup.py build_sphinx


Bug reports
-----------

When `reporting a bug <https://github.com/affo/affo-email-service/issues>`_
please include:

    * Operating system name and version.
    * `affo-email-service` version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Feature requests and feedback
-----------------------------

The best way to send feedback is to file an issue on
`Github <https://github.com/affo/affo-email-service/issues>`_. If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
