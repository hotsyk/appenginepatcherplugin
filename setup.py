try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='appenginepatcherplugin',
    version='0.2',
    url='http://github.com/hotsyk/appenginepatcherplugin/tree/master',
    author='Volodymyr Hotsyk',
    author_email = 'gotsyk+nose@gmail.com',
    description = 'Appengine patch nose plugin',
    install_requires='nose',
    license = 'GNU LGPL',
    keywords = 'test unittest nose nosetests plugin gae appenginepatch',
    py_modules = ['appenginepatcherplugin'],
    entry_points = {
        'nose.plugins.0.10': [
            'appenginepatcherplugin = appenginepatcherplugin:AppenginePatcher'
            ]
        }

    )
