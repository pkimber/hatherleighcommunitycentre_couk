hatherleighcommunitycentre.co.uk
********************************

.. important:: To deploy this project, use the following branches:

::

  # base
  1136-delete-image-from-library
  # block
  1136-delete-image-from-library
  # cms
  1043-convert-from-cms-models-to-block
  # compose
  1136-delete-image-from-library

After deploy::

  django-admin.py migrate --noinput
  django-admin.py init_app_compose

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

  ./init_dev.sh

Release and Deploy
==================

https://www.pkimber.net/open/
