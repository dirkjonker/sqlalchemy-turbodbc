"""This test needs to connect to an actual server.

Set the environment variable TEST_SA_CONNSTR to something like:

mssql+turbodbc://username:pwd@localhost:1433/test?driver=FreeTDS
"""

import os

import pytest
from sqlalchemy import create_engine


@pytest.mark.skipif(os.environ.get('TEST_SA_CONNSTR') is None,
                    reason="No environment variable for test db connection")
class TestUnicode:

    @pytest.fixture
    def connection(self):
        """Connection fixture to ensure rollback in case of failures."""
        connstr = os.environ.get('TEST_SA_CONNSTR')
        engine = create_engine(connstr)
        cnxn = engine.connect()
        tx = cnxn.begin()
        yield cnxn
        tx.rollback()
        cnxn.close()
        engine.dispose()

    def test_sa_insert_unicode_emoji(self, connection):
        """Test SQLAlchemy connection insert emoji."""

        text = u'test 1 2 3 \U0001F602 foo bar'
        connection.execute("CREATE TABLE dbo.test_unicode (val NVARCHAR(100))")
        connection.execute("INSERT INTO dbo.test_unicode (val) VALUES (?)", (text,))
        result = connection.execute("SELECT * FROM dbo.test_unicode")
        rows = result.fetchall()

        assert rows[-1][0] == text
