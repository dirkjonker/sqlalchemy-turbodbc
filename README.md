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
To create a connection using this simply use the `mssql+turbodbc` protocol.

For example:

```python
engine = create_engine('mssql+turbodbc://scott:tiger@mydsn')
```

For more information please see the SQLAlchemy documentation.
http://docs.sqlalchemy.org/en/rel_1_1/core/engines.html#microsoft-sql-server
