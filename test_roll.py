import pytest

from app import appp


@pytest.fixture()
def client():
    a = appp()
    client = a.test_client()
    yield client


def test_hello_world(client):

    rv = client.get('/')
    assert b'Hello world' in rv.data
