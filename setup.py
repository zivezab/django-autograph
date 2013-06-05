from distutils.core import setup
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
    packages=['autograph'],
    author='Zive Lai',
    author_email='zive.lai@gmail.com',
    url='https://github.com/zivezab/django-autograph/',
    description='A Django application for managing signature/autograph data.',
    long_description=open("README.md").read(),
    install_requires = ['django >= 1.4.5', 'south >= 0.8.1', 'pil >= 1.1.7'],
    cmdclass={'test': TestCommand},
)