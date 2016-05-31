"""
Flask-JSONWrap

Wraps a Flask app such that all errors returned are JSON-API compatible,
rather than being HTML.
"""
from setuptools import setup, find_packages


setup(
    name='Flask-JSONWrap',
    description='Make a Flask app JSON API friendly.',
    long_description=__doc__,
    url='http://github.com/daroot/flask-jsonwrap/',
    version='1.0.1',
    author='Dan Root',
    author_email='rootdan@gmail.com',
    license='WTFPL',

    packages=find_packages(exclude=['doc', 'test']),
    setup_requires=['pytest-runner'],
    install_requires=[
        'Flask',
    ],
    tests_require=['pytest'],
    zip_safe=False,
    include_package_data=True,

    platforms='any',

    keywords=['flask', 'jsonapi'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
