import pytest
from .helpers.api_helper import OrangeHRMApi

BASE_URL = "https://opensource-demo.orangehrmlive.com"
CLIENT_ID = "ĐIỀN_CLIENT_ID"
CLIENT_SECRET = "ĐIỀN_CLIENT_SECRET"

@pytest.fixture(scope="session")
def api():
    return OrangeHRMApi(BASE_URL, CLIENT_ID, CLIENT_SECRET)

def test_get_user_info(api):
    data = api.get_user_info(limit=1)
    assert "data" in data

def test_create_user(api):
    result, status = api.create_user(username="NamQA", password="P@ssw0rd2025")
    assert status == 201