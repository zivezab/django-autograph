import os

from setuptools import setup, find_packages
from distutils.core import Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(DATABASES={'default': {'NAME': ':memory:',
            'ENGINE': 'django.db.backends.sqlite3'}},
            INSTALLED_APPS=('autograph',))
        from django.core.management import call_command
        call_command('test', 'autograph')


setup(
    name='autograph',
    version='1.0.0',
    author='Zive Lai',
    author_email='zive.lai@gmail.com',
    packages=find_packages(exclude=['autograph_test']),
    url='https://github.com/zivezab/django-autograph/',
    description='A Django application for managing signature/autograph data.',
    long_description=open(os.path.join(os.getcwdu(), 'README.md')).read(),
    install_requires = ['django >= 1.4.5', 'south >= 0.8.1', 'pil >= 1.1.7'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Bug Tracking',
    ],
    cmdclass={'test': TestCommand},
)