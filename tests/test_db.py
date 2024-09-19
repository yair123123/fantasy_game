import pytest

from repository.database import create_tables, drop_all_tables


@pytest.fixture(scope='module')
def setup_database():
    create_tables()
    yield
    drop_all_tables()
def test_database(setup_database):
    pass