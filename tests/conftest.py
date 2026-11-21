from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


ORIGINAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture
def client():
    activities.clear()
    activities.update(deepcopy(ORIGINAL_ACTIVITIES))

    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(deepcopy(ORIGINAL_ACTIVITIES))
