import sys
from setuptools import setup, find_packages


test_requirements = ['pytest']

if sys.version_info < (3, 3):
    test_requirements.append('mock')


long_description = """
# sqlalchemy-turbodbc

SQLAlchemy connector/dialect for connecting to MS SQL Server using Turbodbc.

This works exactly like the `mssql+pyodbc` dialect as described in the [SQLAlchemy documentation here](https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc).
To create a connection using this simply use the `mssql+turbodbc` protocol.

For example:

```python
engine = create_engine('mssql+turbodbc://scott:tiger@mydsn')
```

For more information please see the [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc).
"""


setup(
    name='sqlalchemy_turbodbc',
    version='0.1.1',
    description='SQLAlchemy dialect for Turbodbc',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dirk Jonker',
    author_email='dirkjonker@gmail.com',
    url='https://github.com/dirkjonker/sqlalchemy-turbodbc',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Database',
    ],
    keywords='sql server sqlalchemy turbodbc mssql',
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
