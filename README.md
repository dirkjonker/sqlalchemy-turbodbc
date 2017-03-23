# sqlalchemy-turbodbc
SQLAlchemy connector/dialect for Turbodbc.

Currently only MS SQL Server is supported, I currently have no plans
to support other databases, but feel free to fork this repository or create
pull requests.

This software is in Alpha state, and not tested very well. Please report bugs
using the issue tracker in Github.


## Installation
Currently sqlalchemy-turbodbc requires the unreleased 1.1.0 version of Turbodbc,
which you will need to build and install yourself according to the instructions
on the Turbodbc repository: https://github.com/blue-yonder/turbodbc#development-version

Then, for now you can use
`pip install https://github.com/dirkjonker/sqlalchemy-turbodbc/archive/master.tar.gz`
to install the dialect. When Turbodbc 1.1.0 is released, this package will be
uploaded to pypi as a wheel.


## Usage
To create a connection using this simply use the `mssql+turbodbc` protocol.

For example:

```python
engine = create_engine('mssql+turbodbc://scott:tiger@mydsn')
```

For more information please see the SQLAlchemy documentation.
http://docs.sqlalchemy.org/en/rel_1_1/core/engines.html#microsoft-sql-server
