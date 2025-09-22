import pytest, json, importlib.resources as res

@pytest.fixture(scope="session")
def config():
    with res.files("utils").joinpath("config.json").open("r", encoding="utf-8") as f:
        return json.load(f)