import pytest
from my_plat.app import app as flask_app


@pytest.fixture
def app():
    return flask_app
