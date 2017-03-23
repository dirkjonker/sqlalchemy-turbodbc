try:
    from unittest.mock import patch
except ImportError:
    # python 2
    from mock import patch

from sqlalchemy.engine import url
from sqlalchemy_turbodbc.connector import TurbodbcConnector



TURBO_OPTIONS = 'sqlalchemy_turbodbc.connector.make_options'


def test_connect_no_dsn():
    """Test a connection without DSN."""
    u = url.make_url('mssql+turbodbc://user:pass@host:1433/testdb?driver=Foo')
    with patch(TURBO_OPTIONS) as mock_opts:
        connection = TurbodbcConnector().create_connect_args(u)

    assert connection == [[], {
        'uid': 'user', 'pwd': 'pass', 'database': 'testdb', 'driver': 'Foo',
        'server': 'host', 'port': 1433,
        'turbodbc_options': mock_opts.return_value
    }]
    mock_opts.assert_called_with(prefer_unicode=True)


def test_connect_dsn():
    """Test a dsn connection."""
    u = url.make_url('mssql+turbodbc://user:pass@mydsn')
    with patch(TURBO_OPTIONS) as mock_opts:
        connection = TurbodbcConnector().create_connect_args(u)

    assert connection == [['mydsn'], {
        'uid': 'user', 'pwd': 'pass',
        'turbodbc_options': mock_opts.return_value
    }]
    mock_opts.assert_called_with(prefer_unicode=True)


def test_connect_dsn_with_options():
    """Test additional options for Turbodbc in the query string."""
    u = url.make_url('mssql+turbodbc://user:pass@mydsn/?use_async_io=true'
                     '&parameter_sets_to_buffer=1000')
    with patch(TURBO_OPTIONS) as mock_opts:
        connection = TurbodbcConnector().create_connect_args(u)

    assert connection == [['mydsn'], {
        'uid': 'user', 'pwd': 'pass',
        'turbodbc_options': mock_opts.return_value
    }]
    mock_opts.assert_called_with(
        prefer_unicode=True, parameter_sets_to_buffer=1000, use_async_io=True)
