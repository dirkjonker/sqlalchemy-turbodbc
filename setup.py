import sys
from setuptools import setup, find_packages


test_requirements = ['pytest']

if sys.version_info < (3, 3):
    test_requirements.append('mock')


setup(
    name='sqlalchemy_turbodbc',
    version='0.1.0',
    description='SQLAlchemy dialect for Turbodbc',
    author='Dirk Jonker',
    author_email='dirkjonker@gmail.com',
    url='https://github.com/dirkjonker/sqlalchemy-turbodbc',
    download_url='https://github.com/dirkjonker/sqlalchemy-turboodbc/tarball/0.1.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(),
    entry_points={
        'sqlalchemy.dialects':
            ['mssql.turbodbc = sqlalchemy_turbodbc.dialect:MSDialect_turbodbc']
    },
    license='MIT',
    install_requires=[
        'sqlalchemy',
        'turbodbc>=1.1.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=test_requirements
)
