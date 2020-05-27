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
This works exactly like the `mssql+pyodbc` dialect as described in the [SQLAlchemy documentation here](https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc).
To create a connection using this simply use the `mssql+turbodbc` protocol.

For example:

```python
engine = create_engine('mssql+turbodbc://scott:tiger@mydsn')
```

For more information please see the [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc).
