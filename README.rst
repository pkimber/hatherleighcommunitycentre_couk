hatherleighcommunitycentre.co.uk
********************************

Development
===========

Install
-------

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-hatherleighcommunitycentre_couk
  source venv-hatherleighcommunitycentre_couk/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
-------

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
-----

::

  init_dev.sh

Release and Deploy
==================

https://www.pkimber.net/open/
