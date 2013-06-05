django-autograph
================
Store signature in JSON format into db.
Functional code based on http://keith-wood.name/signature.html#java


Requirements
------------

1. jQuery Signature by kbwood (Keith Wood)
::

  https://github.com/kbwood/signature
  
2. Django 1.4+
3. South
4. Python Imaging Library (PIL)
  
  
Settings
--------

settings.py
::
  
  INSTALLED_APPS = (
      ...
      'autograph',
      ...
  )
  
Testing
-------
::
  
  python manage.py test autograph
  
  
Contact
-------
https://github.com/zivezab/django-autograph/issues
