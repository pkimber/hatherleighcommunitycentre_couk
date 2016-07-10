hatherleighcommunitycentre.co.uk
********************************

.. important:: To deploy this project, use the branches listed in
               ``requirements/branch.txt``.  Use
               https://github.com/mdinsmore/dev-scripts/blob/master/src/set-branches
               to set the branches.

Development
===========

Install
-------

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-hatherleighcommunitycentre_couk
  source venv-hatherleighcommunitycentre_couk/bin/activate

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

https://www.kbsoftware.co.uk/docs/
