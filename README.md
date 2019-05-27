# sqlalchemy-turbodbc
SQLAlchemy connector/dialect for Turbodbc.

Currently only MS SQL Server is supported, I currently have no plans
to support other databases, but feel free to fork this repository or create
pull requests.

This software is in Alpha state, and not tested very well. Please report bugs
using the issue tracker in Github.


## Installation
You can simply use
`pip install sqlalchemy-turbodbc`
to install the dialect.


## Usage
This should work exactly like the `mssql+pyodbc` dialect as described in the [SQLAlchemy documentation here](https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc).
To create a connection using this simply use the `mssql+turbodbc` protocol.

For example:

```python
engine = create_engine('mssql+turbodbc://scott:tiger@mydsn')
```

For more information please see the SQLAlchemy documentation
https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc
