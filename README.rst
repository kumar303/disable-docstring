==================
Disable Docstrings
==================

This is a Nose_ plugin that tells unittest not to use test docstrings as
test names. Instead it uses the name of the test itself.

Install::

  pip install disabledoc

Usage::

  nosetests -v --disable-docstring

.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
