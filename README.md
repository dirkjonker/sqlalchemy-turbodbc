# sqlalchemy-turbodbc
SQLAlchemy connector/dialect for connecting to MS SQL Server using Turbodbc.

Currently only MS SQL Server is supported, there are no plans
to support other databases, but I welcome any pull requests that add support for more databases.

Please report bugs using the issue tracker in Github.

If you want to take ownership of this repository and package, please open an issue!


## Installation
You can simply use
`pip install sqlalchemy-turbodbc`
to install the dialect.


## Usage
This works similar to the `mssql+pyodbc` dialect as described in the [SQLAlchemy documentation here](https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc).
To create a connection using this library, use the `mssql+turbodbc` protocol. It is recommended to set up your database connection as a DSN (Data Source Name) in your ODBC configuration, as described in the [Turbodbc documentation](https://turbodbc.readthedocs.io/en/latest/pages/databases/mssql.html).

Connecting using an ODBC DSN (Data Source Name):

```python
engine = create_engine('mssql+turbodbc://scott:tiger@mydsn')
```

Connecting without a DSN:
```python
engine = create_engine("mssql+turbodbc://scott:tiger@myhost:port/databasename?driver=SQL+Server+Native+Client+10.0")
```

For more information please see the [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc).

Note: using a PyODBC connection string is not currently supported.
