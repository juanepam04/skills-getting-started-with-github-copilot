from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activity data before and after each test."""
    original = deepcopy(activities)

    for name in list(activities):
        del activities[name]
    activities.update(deepcopy(original))

    yield

    for name in list(activities):
        del activities[name]
    activities.update(deepcopy(original))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
