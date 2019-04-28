from setuptools import setup

setup(
    name='CourtFinder',
    packages=['CourtFinder'],
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'flask-security',
        'mysqlclient',
        'googlemaps',
    ]
)
