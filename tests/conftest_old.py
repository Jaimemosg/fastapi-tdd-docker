import os

import pytest
from starlette.testclient import TestClient

from app import main_old
from app.config import Settings, get_settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    # set up
    main_old.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main_old.app) as test_client:

        # testing
        yield test_client

    # tear down
