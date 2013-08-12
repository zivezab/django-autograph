django-autograph
================
Store signature in JSON format into db.
Functional code for image generator based on http://keith-wood.name/signature.html#java


Requirements
------------
1. Django 1.4+
2. South
3. Python Imaging Library (PIL)
  
  
Settings
--------
  INSTALLED_APPS = (
    'autograph',
  )

  
Testing
-------
  python manage.py test autograph
  
  
Demo - autograph_test
---------------------
  1. pip install -r requirements.txt
  2. python manage.py syncdb
  3. python manage.py migrate
  4. python manage.py runserver
  
  
Contact
-------
  https://github.com/zivezab/django-autograph/issues
